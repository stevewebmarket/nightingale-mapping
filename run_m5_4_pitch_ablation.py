"""
M5.4 — Pitch-quality / voiced-frame ablation.

Frame-selection problem, not pitch-model redesign.  Same shape as M5.2:
multiple variants, one pre-set pass condition, no per-clip tuning.
The onset detector is left at the M5.3-locked cqt_flux default; only
the pitch-at-onset window strategy varies.

Pre-set pass condition (set BEFORE run):

  1. polyphonic stays 8/8 detected on all three transforms
  2. polyphonic matches improve above 4/24
  3. highenergy improves above 9/24
  4. grand total > 100/144 (0.6944)
  5. orchestra / flute / synthetic do not drop by more than 1 match each
  6. rock regression remains visible (or is genuinely improved)

Variants:

  baseline       current M5.3 pitch_at: window [t-0.15, t+0.25], YIN
                 median over the whole window
  post_delay_1   shifted window [t+0.02, t+0.42] -- skip the transient
  post_delay_2   shifted window [t+0.05, t+0.45] -- larger skip
  short_med      tight window [t+0.02, t+0.18], YIN median
  energy_gated   baseline window, per-frame YIN+RMS, drop frames whose
                 RMS is below 30% of the window peak before taking median
  hybrid_best    window [t-0.05, t+0.35], iteratively trim YIN frames
                 to the tightest cluster (median, then keep frames
                 within 3% of median, repeat 3x) -- robust to outliers

Usage:
    python run_m5_4_pitch_ablation.py
"""

import json
import os
from statistics import median

import numpy as np
import librosa

import run_milestones as RM
from run_milestones import (
    DEFAULT_CONFIG, SR, NUM_NOTES, SHIFT_FACTOR,
    score_pitch_shift, score_time_stretch, score_composition,
)
from run_m4_1_benchmark import synthetic_clip, load_audio_file

EXPECTED_RATIO = {
    "pitch_shift":  SHIFT_FACTOR,
    "time_stretch": 1.0,
    "composition":  SHIFT_FACTOR,
}

YIN_FRAME = 2048
YIN_HOP = 512


# ---------------------------------------------------------------------------
# Pitch-at variants
# ---------------------------------------------------------------------------

def _seg(audio, t_start, t_end):
    s = max(0, int(t_start * SR))
    e = min(len(audio), int(t_end * SR))
    return audio[s:e]


def _yin_window_median(seg, cfg):
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


def p_baseline(audio, t, cfg):
    return _yin_window_median(_seg(audio, t - 0.15, t + 0.25), cfg)


def p_post_delay_1(audio, t, cfg):
    return _yin_window_median(_seg(audio, t + 0.02, t + 0.42), cfg)


def p_post_delay_2(audio, t, cfg):
    return _yin_window_median(_seg(audio, t + 0.05, t + 0.45), cfg)


def p_short_med(audio, t, cfg):
    return _yin_window_median(_seg(audio, t + 0.02, t + 0.18), cfg)


def p_energy_gated(audio, t, cfg):
    seg = _seg(audio, t - 0.15, t + 0.25)
    if len(seg) < YIN_FRAME:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR,
                     frame_length=YIN_FRAME, hop_length=YIN_HOP)
    rms = librosa.feature.rms(y=seg, frame_length=YIN_FRAME,
                              hop_length=YIN_HOP)[0]
    L = min(len(f0), len(rms))
    f0, rms = f0[:L], rms[:L]
    if rms.max() <= 0:
        return None
    thr = 0.3 * rms.max()
    mask = (f0 > cfg.get("fmin", 50)) & (rms >= thr)
    if not mask.any():
        return None
    return float(np.median(f0[mask]))


def p_hybrid_best(audio, t, cfg):
    seg = _seg(audio, t - 0.05, t + 0.35)
    if len(seg) < YIN_FRAME:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR,
                     frame_length=YIN_FRAME, hop_length=YIN_HOP)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) == 0:
        return None
    if len(valid) < 3:
        return float(np.median(valid))
    m = float(np.median(valid))
    for _ in range(3):
        keep = valid[np.abs(valid - m) / m < 0.03]
        if len(keep) < 2:
            break
        m = float(np.median(keep))
    return m


VARIANTS = [
    ("baseline",     p_baseline),
    ("post_delay_1", p_post_delay_1),
    ("post_delay_2", p_post_delay_2),
    ("short_med",    p_short_med),
    ("energy_gated", p_energy_gated),
    ("hybrid_best",  p_hybrid_best),
]


# ---------------------------------------------------------------------------
# Evaluation: monkey-patch run_milestones.pitch_at
# ---------------------------------------------------------------------------

def evaluate_variant(name, fn, clips, cfg):
    original = RM.pitch_at
    RM.pitch_at = lambda audio, t, cfg=cfg: fn(audio, t, cfg)
    try:
        out = {}
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
        return out
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

    print("=" * 96)
    print("M5.4 — pitch-quality / voiced-frame ablation  (no per-clip tuning)")
    print(f"  base config: {cfg}")
    print("=" * 96)

    all_results = {}
    for vname, vfn in VARIANTS:
        print(f"\n[{vname}]")
        per_clip = evaluate_variant(vname, vfn, clips, cfg)
        all_results[vname] = per_clip

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

    # Cross-variant focused tables
    print("\n" + "=" * 96)
    print("Polyphonic + Highenergy match counts (the M5.4 targets)")
    print("=" * 96)
    print(f"  {'variant':16s}  {'poly p/t/c':>10s}  {'poly tot':>9s}  "
          f"{'high p/t/c':>10s}  {'high tot':>9s}")
    for vname, _ in VARIANTS:
        p = all_results[vname]["polyphonic"]
        h = all_results[vname]["highenergy"]
        ptot = sum(p[k]["matches"] for k in p)
        htot = sum(h[k]["matches"] for k in h)
        ptc = f"{p['pitch_shift']['matches']}/{p['time_stretch']['matches']}/{p['composition']['matches']}"
        htc = f"{h['pitch_shift']['matches']}/{h['time_stretch']['matches']}/{h['composition']['matches']}"
        print(f"  {vname:16s}  {ptc:>10s}  {ptot:>4d}/24      {htc:>10s}  {htot:>4d}/24")

    print("\n" + "=" * 96)
    print("Rock regression watch + per-clip totals")
    print("=" * 96)
    print(f"  {'variant':16s}  {'rock p/t/c':>14s}  {'orch':>5s} {'flute':>6s} {'synth':>6s}  {'GRAND':>10s}")
    for vname, _ in VARIANTS:
        per = all_results[vname]
        rk = per["rock"]
        def total(c):
            return sum(per[c][k]["matches"] for k in per[c])
        gw = sum(total(c) for c in per)
        gt = sum(per[c][k]["detected"] for c in per for k in per[c])
        rkc = f"{rk['pitch_shift']['matches']}/{rk['time_stretch']['matches']}/{rk['composition']['matches']}"
        print(f"  {vname:16s}  {rkc:>10s}  "
              f"{total('orchestra'):>5d} {total('flute'):>6d} {total('synthetic_just'):>6d}  "
              f"{gw:>4d}/{gt:<4d}={gw/gt:.4f}")

    # Pass condition evaluation
    print("\n" + "=" * 96)
    print("Pass-condition check vs M5.3 baseline (orchestra=24 flute=22 synthetic=23 total=100/144)")
    print("=" * 96)
    for vname, _ in VARIANTS:
        per = all_results[vname]
        poly_det_ok = all(per["polyphonic"][k]["detected"] == 8 for k in per["polyphonic"])
        poly_match = sum(per["polyphonic"][k]["matches"] for k in per["polyphonic"])
        high_match = sum(per["highenergy"][k]["matches"] for k in per["highenergy"])
        orch_match = sum(per["orchestra"][k]["matches"] for k in per["orchestra"])
        flute_match = sum(per["flute"][k]["matches"] for k in per["flute"])
        synth_match = sum(per["synthetic_just"][k]["matches"] for k in per["synthetic_just"])
        gw = sum(per[c][k]["matches"] for c in per for k in per[c])
        gt = sum(per[c][k]["detected"] for c in per for k in per[c])

        c1 = poly_det_ok
        c2 = poly_match > 4
        c3 = high_match > 9
        c4 = gw / gt > 100 / 144
        c5 = (orch_match >= 23) and (flute_match >= 21) and (synth_match >= 22)
        verdict = "PASS" if all([c1, c2, c3, c4, c5]) else "fail"
        flags = "".join("Y" if c else "n" for c in [c1, c2, c3, c4, c5])
        print(f"  {vname:16s}  conditions[1-5]={flags}  poly={poly_match} high={high_match} "
              f"total={gw}/{gt}={gw/gt:.4f}  -> {verdict}")

    with open("m5_4_pitch_ablation.json", "w") as f:
        json.dump({"config": cfg, "results": all_results}, f, indent=2)
    print("\nWrote m5_4_pitch_ablation.json")


if __name__ == "__main__":
    main()
