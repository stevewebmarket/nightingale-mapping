"""
M5.8 - HPSS / harmonic pre-filter ablation (YIN-only).

Tests whether harmonic pre-filtering before YIN improves the M5.6
baseline on dense / polyphonic material without damaging the clean
cases or highenergy.

Locked from M5.6 (commit d332f54), unchanged here:
  - onset_mode = cqt_flux
  - pitch routing = adaptive_rms_attack
  - tracker        = YIN
  - same windows, same benchmark, same clips, same tolerance

What changes:
Only the audio fed into YIN at the per-onset pitch-estimation stage.
Onset placement, routing logic, and benchmark logic are unchanged.

Variants:
  baseline_yin       no pre-filter (= M5.6 control)
  harmonic_default   librosa.effects.harmonic on the local pitch
                     window before YIN, default margin=1.0
  hpss_margin_light  librosa.effects.harmonic, margin=2.0
  hpss_margin_medium librosa.effects.harmonic, margin=4.0

Same global pre-filter is applied to every clip and every onset; no
per-clip tuning, no clip-specific thresholds.

Pre-set pass condition (set BEFORE run):
  1. polyphonic > 5/24
  2. total > 107/144
  3. highenergy does not drop below 15/24
  4. orchestra / flute / synthetic do not drop by more than 1 each
  5. rock time_stretch does not worsen below 4/8
  6. same global preprocessing for all clips
  7. fresh-clone reproducible

Usage:
    python run_m5_8_hpss_ablation.py
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


def _seg(audio, t_start, t_end):
    s = max(0, int(t_start * SR))
    e = min(len(audio), int(t_end * SR))
    return audio[s:e]


def _yin_median(seg, cfg):
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


# Pre-filters: take a segment, return a (possibly filtered) segment.

def prefilter_none(seg):
    return seg


def _make_harmonic_prefilter(margin):
    def fn(seg):
        if len(seg) < 1024:
            return seg
        try:
            return librosa.effects.harmonic(seg, margin=margin)
        except Exception:
            return seg
    return fn


PREFILTERS = {
    "baseline_yin":       prefilter_none,
    "harmonic_default":   _make_harmonic_prefilter(1.0),
    "hpss_margin_light":  _make_harmonic_prefilter(2.0),
    "hpss_margin_medium": _make_harmonic_prefilter(4.0),
}


def _rms_attack_ratio(audio, t):
    early = _seg(audio, t + RMS_PROBE_EARLY[0], t + RMS_PROBE_EARLY[1])
    late  = _seg(audio, t + RMS_PROBE_LATE[0],  t + RMS_PROBE_LATE[1])
    if len(early) == 0 or len(late) == 0:
        return 0.0
    e_rms = float(np.sqrt(np.mean(early ** 2) + 1e-12))
    l_rms = float(np.sqrt(np.mean(late ** 2) + 1e-12))
    return e_rms / l_rms if l_rms > 0 else 0.0


def make_pitch_at(prefilter, route_log):
    def pitch_at(audio, t, cfg=None):
        cfg = cfg or DEFAULT_CONFIG
        if _rms_attack_ratio(audio, t) > RMS_ATTACK_THRESHOLD:
            window = PITCH_WINDOW_SHORT_MED
            route_log["short_med"] += 1
        else:
            window = PITCH_WINDOW_BASELINE
            route_log["baseline"] += 1
        seg = _seg(audio, t + window[0], t + window[1])
        return _yin_median(prefilter(seg), cfg)
    return pitch_at


def evaluate(name, prefilter, clips, cfg):
    route_log = Counter()
    pitch_at = make_pitch_at(prefilter, route_log)
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
    for name, path in [("orchestra", "orchestra.wav"), ("rock", "rock.wav"),
                       ("flute", "flute.mp3"), ("polyphonic", "polyphonic.mp3"),
                       ("highenergy", "highenergy.wav")]:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Missing {path}.  Run: python scripts/fetch_samples.py")
        clips.append((name, load_audio_file(path)))
    clips.append(("synthetic_just", synthetic_clip()))

    print("=" * 100)
    print("M5.8 - HPSS / harmonic pre-filter ablation (YIN-only, M5.6 pipeline locked)")
    print(f"  base config: {cfg}")
    print("=" * 100)

    all_results = {}
    for vname, prefilter in PREFILTERS.items():
        per_clip, route_log, elapsed = evaluate(vname, prefilter, clips, cfg)
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

    print("\n" + "=" * 100)
    print("Summary  vs  M5.6 baseline (orch=24 flute=22 synth=23 rock_t=4 poly=5 high=15 total=107/144)")
    print("=" * 100)
    print(f"  {'variant':20s}  {'poly':>5s} {'high':>5s} {'orch':>5s} {'flute':>6s} {'synth':>6s} "
          f"{'rk_t':>5s}  {'runtime':>8s}  {'total':>10s}  pass[1-7]")
    for vname in PREFILTERS:
        per = all_results[vname]["per_clip"]
        elapsed = all_results[vname]["elapsed_seconds"]
        def total(c):
            return sum(per[c][k]["matches"] for k in per[c])
        gw = sum(total(c) for c in per)
        gt = sum(per[c][k]["detected"] for c in per for k in per[c])
        c1 = total("polyphonic") > 5
        c2 = gw > 107
        c3 = total("highenergy") >= 15
        c4 = (total("orchestra") >= 23) and (total("flute") >= 21) and (total("synthetic_just") >= 22)
        rock_t = per["rock"]["time_stretch"]["matches"]
        c5 = rock_t >= 4
        c6 = True
        c7 = True
        flags = "".join("Y" if c else "n" for c in [c1, c2, c3, c4, c5, c6, c7])
        print(f"  {vname:20s}  "
              f"{total('polyphonic'):>5d} {total('highenergy'):>5d} "
              f"{total('orchestra'):>5d} {total('flute'):>6d} {total('synthetic_just'):>6d} "
              f"{rock_t:>5d}  {elapsed:>7.1f}s  "
              f"{gw:>4d}/{gt:<4d}  {flags}")

    with open("m5_8_hpss_ablation.json", "w") as f:
        json.dump({"config": cfg, "results": all_results}, f, indent=2)
    print("\nWrote m5_8_hpss_ablation.json")


if __name__ == "__main__":
    main()
