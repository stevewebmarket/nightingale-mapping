"""
M4.1 — Expanded benchmark.

Same system, same metric, same 1% tolerance, no per-dataset tuning.
Runs the unchanged M3.1 pipeline on six clips chosen to stress
different failure modes:

  orchestra      baseline harmonic content   (samples-v1 release)
  rock           baseline mixed content      (samples-v1 release)
  flute          clean monophonic            (curated)
  polyphonic     dense polyphonic            (curated)
  highenergy     transient-heavy             (curated)
  synthetic_just ground-truth sine sequence at known just ratios

Synthetic case = 8 pure sine notes at 220 Hz * {1, 9/8, 5/4, 4/3,
3/2, 5/3, 15/8, 2} with 0.5s tone + 0.1s silence each.  Ratio-perfect
anchor: any drop here is a system characteristic, not the audio.

No re-tuning.  The default extractor config from run_milestones is
used unchanged.

Usage:
    python run_m4_1_benchmark.py
"""

import json
import os
import numpy as np
import librosa

from run_milestones import (
    DEFAULT_CONFIG, SR, CLIP_SECONDS,
    score_pitch_shift, score_time_stretch, score_composition,
    load_clip,
)

JUST_RATIOS = [1.0, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8, 2.0]


def synthetic_clip(base_freq=220.0, tone_dur=0.5, gap_dur=0.1):
    """8 pure sine notes at known just-intonation ratios.  Ground-truth anchor."""
    rng = np.random.RandomState(0)
    pieces = []
    for r in JUST_RATIOS:
        t = np.arange(int(SR * tone_dur)) / SR
        # tiny envelope so onset detector sees a transient
        env = np.ones_like(t)
        env[:200] = np.linspace(0, 1, 200)
        env[-200:] = np.linspace(1, 0, 200)
        tone = np.sin(2 * np.pi * base_freq * r * t) * env
        pieces.append(tone.astype(np.float32))
        pieces.append(np.zeros(int(SR * gap_dur), dtype=np.float32))
    audio = np.concatenate(pieces)
    # microscopic noise to avoid degenerate FFTs
    audio += rng.randn(len(audio)).astype(np.float32) * 1e-5
    return audio


def load_audio_file(path):
    y, _ = librosa.load(path, sr=SR, duration=CLIP_SECONDS, mono=True)
    return y


def evaluate_clip(audio, label, cfg):
    out = []
    for fn, test_name in [(score_pitch_shift, "pitch_shift"),
                          (score_time_stretch, "time_stretch"),
                          (score_composition, "composition")]:
        r = fn(audio, label, cfg)
        out.append({
            "label": label, "test": test_name,
            "within": r["folded_score"], "total": r["total"],
        })
    return out


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
                f"Missing {path}.  See scripts/fetch_samples.py for orchestra/rock; "
                f"flute/polyphonic/highenergy ship from samples-v2 release."
            )
        clips.append((name, load_audio_file(path)))
    clips.append(("synthetic_just", synthetic_clip()))

    print("=" * 78)
    print("M4.1 — expanded benchmark  (config unchanged from M3.1 baseline)")
    print(f"  config: {cfg}")
    print("=" * 78)
    print(f"\n{'dataset':22s} {'pitch':>10s} {'time':>10s} {'comp':>10s}   {'total':>9s}   score")
    print("-" * 78)

    all_rows = []
    grand_within = 0
    grand_total = 0

    for name, audio in clips:
        rows = evaluate_clip(audio, name, cfg)
        all_rows.extend(rows)
        wins = {r["test"]: (r["within"], r["total"]) for r in rows}
        ds_within = sum(w for w, _ in wins.values())
        ds_total  = sum(t for _, t in wins.values())
        grand_within += ds_within
        grand_total  += ds_total
        score = ds_within / ds_total if ds_total else 0.0
        print(f"{name:22s} "
              f"{wins['pitch_shift'][0]:>3d}/{wins['pitch_shift'][1]:<2d}    "
              f"{wins['time_stretch'][0]:>3d}/{wins['time_stretch'][1]:<2d}    "
              f"{wins['composition'][0]:>3d}/{wins['composition'][1]:<2d}    "
              f"{ds_within:>3d}/{ds_total:<3d}   {score:.4f}")

    print("-" * 78)
    grand = grand_within / grand_total if grand_total else 0.0
    print(f"{'TOTAL':22s}                                     "
          f"{grand_within:>3d}/{grand_total:<3d}   {grand:.4f}")
    print()
    print("Pass = system runs unchanged on all clips AND results are differentiated.")

    with open("m4_1_results.json", "w") as f:
        json.dump({"config": cfg, "rows": all_rows,
                   "total_within": grand_within, "total_notes": grand_total,
                   "score": grand}, f, indent=2)
    print("Wrote m4_1_results.json")


if __name__ == "__main__":
    main()
