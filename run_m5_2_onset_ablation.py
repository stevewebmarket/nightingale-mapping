"""
M5.2 — Onset segmentation ablation.

Diagnostics-driven, not a redesign.  M5.1 showed `polyphonic` is the
only clip with structural data loss: 3 of 8 notes never enter
evaluation because the onset detector finds 5 instead of 8.  This
script compares a small set of onset-detection variants on the full
M4.1 clip set and reports:

  - detected onset count per clip / transform
  - folded score using the unchanged downstream pipeline
  - pitch quality of the detected onsets (median rel error)

Pass condition for M5.2:

  * polyphonic detected onsets move from ~5/8 toward 8/8
  * orchestra / rock / synthetic_just stay close to baseline
  * no per-clip tuning — one config wins or none does

We do *not* lock anything in M5.2.  This is a measurement step.
M5.2 chooses the variant; subsequent milestones lock and re-benchmark.

Usage:
    python run_m5_2_onset_ablation.py
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

# ---------------------------------------------------------------------------
# Onset-detection variants
# ---------------------------------------------------------------------------
# Each variant takes (audio, cfg, n) and returns a list of times.

def v_baseline(audio, cfg, n=NUM_NOTES):
    return librosa.onset.onset_detect(
        y=audio, sr=SR, units="time",
        delta=cfg.get("onset_delta", 0.05), wait=4, backtrack=True
    )[:n]

def v_soft(audio, cfg, n=NUM_NOTES):
    return librosa.onset.onset_detect(
        y=audio, sr=SR, units="time",
        delta=0.02, wait=4, backtrack=True
    )[:n]

def v_softer_short_wait(audio, cfg, n=NUM_NOTES):
    return librosa.onset.onset_detect(
        y=audio, sr=SR, units="time",
        delta=0.01, wait=2, backtrack=True
    )[:n]

def v_no_backtrack(audio, cfg, n=NUM_NOTES):
    return librosa.onset.onset_detect(
        y=audio, sr=SR, units="time",
        delta=cfg.get("onset_delta", 0.05), wait=4, backtrack=False
    )[:n]

def _cqt_env(audio):
    C = np.abs(librosa.cqt(y=audio, sr=SR))
    S = librosa.amplitude_to_db(C, ref=np.max)
    return librosa.onset.onset_strength(sr=SR, S=S)

def v_cqt_flux(audio, cfg, n=NUM_NOTES):
    """Onset envelope from CQT — emphasises harmonic onsets in dense mixes."""
    env = _cqt_env(audio)
    return librosa.onset.onset_detect(
        onset_envelope=env, sr=SR, units="time",
        delta=cfg.get("onset_delta", 0.05), wait=4, backtrack=True
    )[:n]

def v_mel_median(audio, cfg, n=NUM_NOTES):
    """Onset envelope with median aggregation across mel bands —
    softer to broadband transients, more sensitive to tonal onsets."""
    env = librosa.onset.onset_strength(y=audio, sr=SR, aggregate=np.median)
    return librosa.onset.onset_detect(
        onset_envelope=env, sr=SR, units="time",
        delta=cfg.get("onset_delta", 0.05), wait=4, backtrack=True
    )[:n]

def v_cqt_flux_soft(audio, cfg, n=NUM_NOTES):
    """CQT envelope + softer threshold — best of both for dense pitched mixes."""
    env = _cqt_env(audio)
    return librosa.onset.onset_detect(
        onset_envelope=env, sr=SR, units="time",
        delta=0.02, wait=4, backtrack=True
    )[:n]


VARIANTS = [
    ("baseline",         v_baseline),
    ("soft",             v_soft),
    ("softer_short_wait",v_softer_short_wait),
    ("no_backtrack",     v_no_backtrack),
    ("cqt_flux",         v_cqt_flux),
    ("mel_median",       v_mel_median),
    ("cqt_flux_soft",    v_cqt_flux_soft),
]


# ---------------------------------------------------------------------------
# Per-variant evaluation: monkey-patch run_milestones.detect_onsets
# ---------------------------------------------------------------------------

def evaluate_variant(name, fn, clips, cfg):
    """Run the full benchmark with the given onset variant.
    Returns per-clip dict with detected counts + folded scores + pitch quality."""
    original = RM.detect_onsets
    RM.detect_onsets = lambda audio, cfg=cfg, n=NUM_NOTES: fn(audio, cfg, n)
    try:
        out = {}
        for clip_name, audio in clips:
            per_test = {}
            for sfn in (score_pitch_shift, score_time_stretch, score_composition):
                r = sfn(audio, clip_name, cfg)
                test = r["test"]
                expected = EXPECTED_RATIO[test]
                rel_errs = []
                for fold in r["folded"]:
                    if fold is None:
                        continue
                    rel_errs.append(abs(fold - expected) / abs(expected))
                per_test[test] = {
                    "detected": r["total"],
                    "matches":  r["folded_score"],
                    "median_rel_error": float(median(rel_errs)) if rel_errs else None,
                }
            out[clip_name] = per_test
        return out
    finally:
        RM.detect_onsets = original


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

    print("=" * 90)
    print("M5.2 — onset segmentation ablation  (no per-clip tuning)")
    print(f"  base config: {cfg}")
    print("=" * 90)

    all_results = {}
    for vname, vfn in VARIANTS:
        print(f"\n[{vname}]")
        per_clip = evaluate_variant(vname, vfn, clips, cfg)
        all_results[vname] = per_clip

        # Per-clip summary line
        header = f"  {'clip':16s} {'pitch':>10s} {'time':>10s} {'comp':>10s}   {'total':>9s}"
        print(header)
        grand_w, grand_t = 0, 0
        for clip_name in [c for c, _ in clips]:
            t = per_clip[clip_name]
            ds_w = sum(t[k]["matches"]  for k in t)
            ds_t = sum(t[k]["detected"] for k in t)
            grand_w += ds_w; grand_t += ds_t
            print(f"  {clip_name:16s} "
                  f"{t['pitch_shift']['matches']:>3d}/{t['pitch_shift']['detected']:<2d}    "
                  f"{t['time_stretch']['matches']:>3d}/{t['time_stretch']['detected']:<2d}    "
                  f"{t['composition']['matches']:>3d}/{t['composition']['detected']:<2d}    "
                  f"{ds_w:>3d}/{ds_t:<3d}")
        print(f"  {'TOTAL':16s}                                     "
              f"{grand_w:>3d}/{grand_t:<3d}   "
              f"score={grand_w/grand_t:.4f}" if grand_t else "  TOTAL  -")

    # Cross-variant focus on polyphonic detected counts and matches
    print("\n" + "=" * 90)
    print("Polyphonic onset count by variant  (target: detected -> 8 per test, with matches following)")
    print("=" * 90)
    print(f"  {'variant':22s} {'pitch det/match':>18s} {'time det/match':>18s} {'comp det/match':>18s}")
    for vname, _ in VARIANTS:
        t = all_results[vname]["polyphonic"]
        print(f"  {vname:22s} "
              f"{t['pitch_shift']['detected']:>5d} / {t['pitch_shift']['matches']:<5d}     "
              f"{t['time_stretch']['detected']:>5d} / {t['time_stretch']['matches']:<5d}     "
              f"{t['composition']['detected']:>5d} / {t['composition']['matches']:<5d}")

    # Cross-variant grand totals
    print("\n" + "=" * 90)
    print("Grand total by variant  (matches / detected onsets across all clips & transforms)")
    print("=" * 90)
    for vname, _ in VARIANTS:
        per_clip = all_results[vname]
        gw = sum(per_clip[c][k]["matches"]  for c in per_clip for k in per_clip[c])
        gt = sum(per_clip[c][k]["detected"] for c in per_clip for k in per_clip[c])
        print(f"  {vname:22s}  {gw:>4d} / {gt:<4d}   score={gw/gt:.4f}" if gt
              else f"  {vname:22s}  -")

    with open("m5_2_onset_ablation.json", "w") as f:
        json.dump({"config": cfg, "results": all_results}, f, indent=2)
    print("\nWrote m5_2_onset_ablation.json")


if __name__ == "__main__":
    main()
