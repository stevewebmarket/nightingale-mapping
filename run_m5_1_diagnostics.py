"""
M5.1 — Failure diagnostics.

Diagnostics, not heroics.  No tuning, no fixes.  Runs the unchanged
M3.1 / M4.1 pipeline on the same six clips and breaks each case into:

  A. Segmentation       expected vs detected onsets
  B. Pitch validity     valid vs invalid pitch reads
  C. Match classes      matches  /  octave errors  /  other errors
  D. Error magnitude    median + max relative error

"Octave error" = the raw observed/expected ratio is within tol of 2.0
or 0.5 (i.e. the system locked onto a harmonic / sub-harmonic).  These
are the ones octave-folding catches; what's left in `other_errors` is
genuine pitch confusion.

Usage:
    python run_m5_1_diagnostics.py
"""

import json
import os
from statistics import median

import numpy as np
import librosa

from run_milestones import (
    DEFAULT_CONFIG, SR, CLIP_SECONDS, NUM_NOTES, SHIFT_FACTOR,
    score_pitch_shift, score_time_stretch, score_composition,
)
from run_m4_1_benchmark import synthetic_clip, load_audio_file

# What the system *should* see for each test
EXPECTED_RATIO = {
    "pitch_shift":  SHIFT_FACTOR,   # 1.5
    "time_stretch": 1.0,
    "composition":  SHIFT_FACTOR,   # 1.5
}

TOL = 0.01          # match tolerance (same as benchmark)
OCTAVE_TOL = 0.05   # tolerance for "is this an octave error?"


def is_octave_error(expected, observed, tol=OCTAVE_TOL):
    if expected is None or observed is None:
        return False
    if expected == 0 or observed == 0:
        return False
    q = observed / expected
    return abs(q - 2.0) <= tol or abs(q - 0.5) <= tol


def diagnose_case(case_result, expected_notes=NUM_NOTES):
    """case_result is the dict returned by score_pitch_shift/etc."""
    test = case_result["test"]
    expected = EXPECTED_RATIO[test]

    raw = case_result["raw"]
    folded = case_result["folded"]
    detected = case_result["total"]

    valid = 0
    invalid = 0
    matched = 0
    octave_errors = 0
    other_errors = 0
    rel_errors = []

    for r_raw, r_fold in zip(raw, folded):
        if r_raw is None or r_fold is None:
            invalid += 1
            continue
        valid += 1

        # The system's best answer is the folded ratio.
        rel_error = abs(r_fold - expected) / abs(expected)
        rel_errors.append(rel_error)

        if rel_error <= TOL:
            matched += 1
        elif is_octave_error(expected, r_raw):
            # Folding *should* have caught this; if it still missed, the raw
            # ratio is octave-related to expected -> classify as octave error.
            octave_errors += 1
        else:
            other_errors += 1

    return {
        "label":          f"{case_result['label']}_{test.split('_')[0]}",
        "test":           test,
        "expected_notes": expected_notes,
        "detected_notes": detected,
        "missing_notes":  max(0, expected_notes - detected),
        "valid_pitch":    valid,
        "invalid_pitch":  invalid,
        "matches":        matched,
        "octave_errors":  octave_errors,
        "other_errors":   other_errors,
        "median_rel_error": float(median(rel_errors)) if rel_errors else None,
        "max_rel_error":    float(max(rel_errors))    if rel_errors else None,
        "expected_ratio": expected,
        "raw":    [None if v is None else float(v) for v in raw],
        "folded": [None if v is None else float(v) for v in folded],
    }


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

    print("=" * 78)
    print("M5.1 — failure diagnostics  (config unchanged from M3.1 baseline)")
    print(f"  config: {cfg}")
    print(f"  match tol = {TOL}   octave-error tol = {OCTAVE_TOL}")
    print("=" * 78)

    all_diags = []
    for name, audio in clips:
        print(f"\n{name}")
        for fn in (score_pitch_shift, score_time_stretch, score_composition):
            case = fn(audio, name, cfg)
            d = diagnose_case(case, expected_notes=NUM_NOTES)
            all_diags.append(d)
            print(f"  {d['test']}:")
            print(f"    expected={d['expected_notes']} "
                  f"detected={d['detected_notes']} "
                  f"missing={d['missing_notes']}")
            print(f"    valid_pitch={d['valid_pitch']} "
                  f"invalid_pitch={d['invalid_pitch']}")
            print(f"    matches={d['matches']} "
                  f"octave_errors={d['octave_errors']} "
                  f"other_errors={d['other_errors']}")
            mre = d["median_rel_error"]
            xre = d["max_rel_error"]
            print(f"    median_rel_error={mre:.4f} max_rel_error={xre:.4f}"
                  if mre is not None else
                  "    median_rel_error=  -    max_rel_error=  -  ")

    # Per-clip dominant failure mode
    print("\n" + "=" * 78)
    print("Per-clip dominant failure mode")
    print("=" * 78)
    by_clip = {}
    for d in all_diags:
        clip = d["label"].rsplit("_", 1)[0]
        by_clip.setdefault(clip, []).append(d)

    for clip, diags in by_clip.items():
        miss = sum(d["missing_notes"]  for d in diags)
        inv  = sum(d["invalid_pitch"]  for d in diags)
        oct_ = sum(d["octave_errors"]  for d in diags)
        oth  = sum(d["other_errors"]   for d in diags)
        mat  = sum(d["matches"]        for d in diags)
        # Pick dominant non-match class
        bad = {"missing_onsets": miss, "invalid_pitch": inv,
               "octave_errors": oct_, "other_errors": oth}
        dom = max(bad, key=bad.get) if any(bad.values()) else "none"
        print(f"  {clip:18s}  matches={mat:>3d}  "
              f"miss={miss:<2d} invalid={inv:<2d} "
              f"octave={oct_:<2d} other={oth:<2d}   "
              f"-> dominant: {dom}")

    with open("m5_1_diagnostics.json", "w") as f:
        json.dump({"config": cfg, "tol": TOL, "octave_tol": OCTAVE_TOL,
                   "diagnostics": all_diags}, f, indent=2)
    print("\nWrote m5_1_diagnostics.json")


if __name__ == "__main__":
    main()
