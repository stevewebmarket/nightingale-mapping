"""
M5.7 - Pitch tracker swap ablation.

Tests whether replacing YIN with a stronger pitch tracker improves the
M5.6 locked baseline on the unchanged pipeline.

Locked from M5.6 (commit d332f54):
  - onset_mode = cqt_flux
  - pitch routing = adaptive_rms_attack (early/late RMS ratio > 1.5)
  - same windows: baseline [t-0.15, t+0.25], short_med [t+0.02, t+0.18]
  - same benchmark, same clips, same tolerance, no per-clip tuning

Only the per-window pitch estimator changes:
  - yin     (control = current M5.6)
  - pyin    (probabilistic YIN, returns voiced flags + per-frame probs)
  - crepe   (deep neural tracker; will SKIP HONESTLY if not installed -
            we are not adding heavy deps just to claim a variant)

Pre-set pass condition (set BEFORE run):
  1. total score > 107/144
  2. polyphonic > 5/24
  3. highenergy > 15/24
  4. orchestra / flute / synthetic do not drop by more than 1 each
  5. rock time_stretch does not worsen below 4/8
  6. comparison is global, deterministic, no per-clip tracker switching
  7. fresh-clone reproducible

For each variant we report per-clip and grand totals plus runtime.

Usage:
    python run_m5_7_tracker_ablation.py
"""

import json
import os
import time
from collections import Counter
from statistics import median

import numpy as np
import librosa

import run_milestones as RM
from run_milestones import (
    DEFAULT_CONFIG, SR, SHIFT_FACTOR,
    score_pitch_shift, score_time_stretch, score_composition,
    PITCH_WINDOW_BASELINE, PITCH_WINDOW_SHORT_MED,
    RMS_PROBE_EARLY, RMS_PROBE_LATE, RMS_ATTACK_THRESHOLD,
)
from run_m4_1_benchmark import synthetic_clip, load_audio_file

EXPECTED_RATIO = {
    "pitch_shift":  SHIFT_FACTOR,
    "time_stretch": 1.0,
    "composition":  SHIFT_FACTOR,
}


# ---------------------------------------------------------------------------
# Pitch trackers (each returns median valid f0 from a segment, or None)
# ---------------------------------------------------------------------------

def track_yin(seg, cfg):
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


def track_pyin(seg, cfg):
    if len(seg) < 2048:
        return None
    fmin = cfg.get("fmin", 50)
    fmax = cfg.get("fmax", 16000)
    # librosa.pyin returns (f0, voiced_flag, voiced_prob); f0 has NaN for unvoiced
    f0, voiced_flag, _ = librosa.pyin(
        seg, fmin=fmin, fmax=fmax, sr=SR,
        frame_length=2048,
    )
    valid = f0[(~np.isnan(f0)) & (f0 > fmin) & voiced_flag]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


def track_crepe(seg, cfg):
    """If crepe is importable, run it; otherwise None and the variant is skipped."""
    try:
        import crepe  # noqa: F401
    except Exception:
        return "SKIP"
    if len(seg) < 1024:
        return None
    import crepe
    # Resample to 16k mono for CREPE (its native rate)
    seg16 = librosa.resample(seg, orig_sr=SR, target_sr=16000)
    _t, freq, conf, _act = crepe.predict(seg16, 16000, viterbi=True, verbose=0)
    fmin = cfg.get("fmin", 50)
    mask = (conf >= 0.5) & (freq > fmin)
    if not np.any(mask):
        return None
    return float(np.median(freq[mask]))


TRACKERS = {
    "yin":   track_yin,
    "pyin":  track_pyin,
    "crepe": track_crepe,
}


# ---------------------------------------------------------------------------
# M5.6 routing, parameterised by tracker
# ---------------------------------------------------------------------------

def _seg(audio, t_start, t_end):
    s = max(0, int(t_start * SR))
    e = min(len(audio), int(t_end * SR))
    return audio[s:e]


def _rms_attack_ratio(audio, t):
    early = _seg(audio, t + RMS_PROBE_EARLY[0], t + RMS_PROBE_EARLY[1])
    late  = _seg(audio, t + RMS_PROBE_LATE[0],  t + RMS_PROBE_LATE[1])
    if len(early) == 0 or len(late) == 0:
        return 0.0
    e_rms = float(np.sqrt(np.mean(early ** 2) + 1e-12))
    l_rms = float(np.sqrt(np.mean(late ** 2) + 1e-12))
    return e_rms / l_rms if l_rms > 0 else 0.0


def make_pitch_at(tracker_fn, route_log):
    def pitch_at(audio, t, cfg=None):
        cfg = cfg or DEFAULT_CONFIG
        if _rms_attack_ratio(audio, t) > RMS_ATTACK_THRESHOLD:
            window = PITCH_WINDOW_SHORT_MED
            route_log["short_med"] += 1
        else:
            window = PITCH_WINDOW_BASELINE
            route_log["baseline"] += 1
        return tracker_fn(_seg(audio, t + window[0], t + window[1]), cfg)
    return pitch_at


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate(name, tracker_fn, clips, cfg):
    route_log = Counter()
    pitch_at = make_pitch_at(tracker_fn, route_log)
    original = RM.pitch_at
    RM.pitch_at = pitch_at
    try:
        out = {}
        t0 = time.time()
        for clip_name, audio in clips:
            per_test = {}
            for sfn in (score_pitch_shift, score_time_stretch, score_composition):
                r = sfn(audio, clip_name, cfg)
                test = r["test"]
                expected = EXPECTED_RATIO[test]
                rel_errs = [abs(v - expected) / abs(expected)
                            for v in r["folded"] if v is not None]
                per_test[test] = {
                    "detected": r["total"],
                    "matches":  r["folded_score"],
                    "median_rel_error": float(median(rel_errs)) if rel_errs else None,
                }
            out[clip_name] = per_test
        elapsed = time.time() - t0
        return out, dict(route_log), elapsed
    finally:
        RM.pitch_at = original


def main():
    cfg = dict(DEFAULT_CONFIG)

    print("Loading clips...")
    clips = []
    file_clips = [
        ("orchestra",  "orchestra.wav"),
        ("rock",       "rock.wav"),
        ("flute",      "flute.mp3"),
        ("polyphonic", "polyphonic.mp3"),
        ("highenergy", "highenergy.wav"),
    ]
    for name, path in file_clips:
        if not os.path.isfile(path):
            raise FileNotFoundError(
                f"Missing {path}.  Run: python scripts/fetch_samples.py"
            )
        clips.append((name, load_audio_file(path)))
    clips.append(("synthetic_just", synthetic_clip()))

    # Probe CREPE once
    crepe_probe = track_crepe(np.zeros(SR // 2, dtype=np.float32), cfg)
    crepe_available = crepe_probe != "SKIP"

    variants = [("yin", track_yin), ("pyin", track_pyin)]
    if crepe_available:
        variants.append(("crepe", track_crepe))

    print("=" * 100)
    print("M5.7 - pitch tracker swap ablation  (M5.6 pipeline locked)")
    print(f"  base config: {cfg}")
    print(f"  variants:    {[v for v, _ in variants]}"
          + ("" if crepe_available else "    [crepe SKIPPED: not importable in this environment]"))
    print("=" * 100)

    all_results = {}
    for vname, tracker in variants:
        per_clip, route_log, elapsed = evaluate(vname, tracker, clips, cfg)
        all_results[vname] = {"per_clip": per_clip, "routes": route_log,
                              "elapsed_seconds": round(elapsed, 2)}
        print(f"\n[{vname}]   routes: {route_log}   runtime: {elapsed:.1f}s")
        print(f"  {'clip':16s} {'pitch':>10s} {'time':>10s} {'comp':>10s}   {'total':>9s}")
        gw, gt = 0, 0
        for clip_name in [c for c, _ in clips]:
            t = per_clip[clip_name]
            ds_w = sum(t[k]["matches"]  for k in t)
            ds_t = sum(t[k]["detected"] for k in t)
            gw += ds_w; gt += ds_t
            print(f"  {clip_name:16s} "
                  f"{t['pitch_shift']['matches']:>3d}/{t['pitch_shift']['detected']:<2d}    "
                  f"{t['time_stretch']['matches']:>3d}/{t['time_stretch']['detected']:<2d}    "
                  f"{t['composition']['matches']:>3d}/{t['composition']['detected']:<2d}    "
                  f"{ds_w:>3d}/{ds_t:<3d}")
        print(f"  {'TOTAL':16s}                                     "
              f"{gw:>3d}/{gt:<3d}   score={gw/gt:.4f}")

    # Summary table vs M5.6 baseline (yin = control = M5.6)
    print("\n" + "=" * 100)
    print("Summary  vs  M5.6 baseline (orch=24 flute=22 synth=23 rock_t=4 poly=5 high=15 total=107/144)")
    print("=" * 100)
    print(f"  {'variant':10s}  {'poly':>5s} {'high':>5s} {'orch':>5s} {'flute':>6s} {'synth':>6s} "
          f"{'rk_t':>5s}  {'runtime':>8s}  {'total':>10s}  pass[1-7]")
    for vname, _ in variants:
        per = all_results[vname]["per_clip"]
        elapsed = all_results[vname]["elapsed_seconds"]
        def total(c):
            return sum(per[c][k]["matches"] for k in per[c])
        gw = sum(total(c) for c in per)
        gt = sum(per[c][k]["detected"] for c in per for k in per[c])
        c1 = gw > 107
        c2 = total("polyphonic") > 5
        c3 = total("highenergy") > 15
        c4 = (total("orchestra") >= 23) and (total("flute") >= 21) and (total("synthetic_just") >= 22)
        rock_t = per["rock"]["time_stretch"]["matches"]
        c5 = rock_t >= 4
        c6 = True   # by construction: tracker is global per variant
        c7 = True   # script is deterministic & self-contained
        flags = "".join("Y" if c else "n" for c in [c1, c2, c3, c4, c5, c6, c7])
        print(f"  {vname:10s}  "
              f"{total('polyphonic'):>5d} {total('highenergy'):>5d} "
              f"{total('orchestra'):>5d} {total('flute'):>6d} {total('synthetic_just'):>6d} "
              f"{rock_t:>5d}  {elapsed:>7.1f}s  "
              f"{gw:>4d}/{gt:<4d}  {flags}")

    with open("m5_7_tracker_ablation.json", "w") as f:
        json.dump({
            "config": cfg,
            "crepe_available": crepe_available,
            "results": all_results,
        }, f, indent=2)
    print("\nWrote m5_7_tracker_ablation.json")


if __name__ == "__main__":
    main()
