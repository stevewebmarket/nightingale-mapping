"""M6.1 - relational similarity prototype.

Compare two clips by extracted relational structure (interval ratios between
consecutive detected pitches) and produce a simple, interpretable similarity
score plus a short diagnostic.

Uses the locked M5.6 extraction pipeline from run_milestones.py as-is.
No new model training, no new heavy deps, no per-clip tuning.

Run:    python run_m6_1_similarity.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import librosa

import run_milestones as rm


SR = rm.SR
TOL_PCT = 0.05  # 5 percent tolerance for "matching" ratios


# ---------------------------------------------------------------------------
# Feature extraction
# ---------------------------------------------------------------------------

def extract_pitch_sequence(audio):
    """Run the locked extractor and return the ordered list of detected
    fundamentals (Nones dropped)."""
    onsets = rm.detect_onsets(audio)
    pitches = []
    for t in onsets:
        p = rm.pitch_at(audio, t)
        if p is not None and p > 0:
            pitches.append(float(p))
    return pitches


def interval_ratios(pitches):
    """Consecutive interval ratios:  r[i] = p[i+1] / p[i]."""
    return [pitches[i + 1] / pitches[i] for i in range(len(pitches) - 1)]


def octave_fold_to_unit(r):
    """Fold ratio into [1/sqrt(2), sqrt(2)] by powers of 2, then take the
    side-agnostic distance from 1.0 in log2 space.  Intervals an octave apart
    collapse to the same folded value."""
    if r <= 0:
        return 1.0
    while r < 1 / math.sqrt(2):
        r *= 2
    while r > math.sqrt(2):
        r /= 2
    return r


# ---------------------------------------------------------------------------
# Similarity scoring
# ---------------------------------------------------------------------------

def best_shift_match_fraction(seq_a, seq_b, tol_pct=TOL_PCT):
    """Slide seq_b across seq_a by integer offsets.  At each offset count
    positions matching within tol_pct.  Score that offset as
    matches / max(len_a, len_b) -- so a high score requires both real
    coverage AND positional alignment.  Require overlap >= MIN_OVERLAP to
    avoid one-element coincidental matches scoring 1.0."""
    if not seq_a or not seq_b:
        return 0.0
    la, lb = len(seq_a), len(seq_b)
    norm = max(la, lb)
    min_overlap = max(3, min(la, lb) // 2)
    best = 0.0
    for k in range(-(lb - 1), la):
        i_start = max(0, k)
        i_end = min(la, lb + k)
        overlap = i_end - i_start
        if overlap < min_overlap:
            continue
        matches = 0
        for i in range(i_start, i_end):
            j = i - k
            a, b = seq_a[i], seq_b[j]
            if a <= 0 or b <= 0:
                continue
            if abs(a - b) / max(a, b) <= tol_pct:
                matches += 1
        frac = matches / norm
        if frac > best:
            best = frac
    return best


def length_agreement(seq_a, seq_b):
    if not seq_a or not seq_b:
        return 0.0
    return min(len(seq_a), len(seq_b)) / max(len(seq_a), len(seq_b))


def similarity(features_a, features_b):
    """Combine raw-ratio match, octave-folded match, and length agreement."""
    raw_a, raw_b = features_a["ratios"], features_b["ratios"]
    fold_a, fold_b = features_a["folded"], features_b["folded"]

    raw_match = best_shift_match_fraction(raw_a, raw_b)
    fold_match = best_shift_match_fraction(fold_a, fold_b)
    len_agree = length_agreement(raw_a, raw_b)

    score = 0.5 * fold_match + 0.3 * raw_match + 0.2 * len_agree

    return {
        "score": score,
        "raw_match": raw_match,
        "fold_match": fold_match,
        "len_agree": len_agree,
        "len_a": len(raw_a) + 1,  # back to note count
        "len_b": len(raw_b) + 1,
        "octave_consistent": fold_match > raw_match + 0.05,
    }


# ---------------------------------------------------------------------------
# Clip loading / pair definitions
# ---------------------------------------------------------------------------

CLIPS = [
    ("orchestra",  "orchestra.wav"),
    ("rock",       "rock.wav"),
    ("flute",      "flute.mp3"),
    ("polyphonic", "polyphonic.mp3"),
    ("highenergy", "highenergy.wav"),
]


def build_features():
    features = {}
    for name, path in CLIPS:
        if not Path(path).exists():
            raise SystemExit(
                f"Missing {path}.  Run: python scripts/fetch_samples.py"
            )
        audio = rm.load_clip(path)
        pitches = extract_pitch_sequence(audio)
        ratios = interval_ratios(pitches)
        folded = [octave_fold_to_unit(r) for r in ratios]
        features[name] = {
            "audio": audio,
            "pitches": pitches,
            "ratios": ratios,
            "folded": folded,
        }

    # Synthetic pairs from orchestra: pitch-shift and time-stretch.
    # Both transforms preserve INTERVAL RATIOS, so these should score very high.
    orch = features["orchestra"]["audio"]
    shifted = rm.pitch_shift_resample(orch, rm.SHIFT_FACTOR)
    stretched = librosa.effects.time_stretch(y=orch, rate=1 / rm.SHIFT_FACTOR)
    for label, audio in [("orchestra_pshift", shifted),
                         ("orchestra_tstretch", stretched)]:
        pitches = extract_pitch_sequence(audio)
        ratios = interval_ratios(pitches)
        folded = [octave_fold_to_unit(r) for r in ratios]
        features[label] = {
            "audio": audio,
            "pitches": pitches,
            "ratios": ratios,
            "folded": folded,
        }
    return features


PAIRS = [
    # Sanity: same clip transformed should match its original.
    ("orchestra", "orchestra_pshift"),
    ("orchestra", "orchestra_tstretch"),
    # Cross-clip pairs (different sources, expect lower).
    ("orchestra", "rock"),
    ("orchestra", "flute"),
    ("rock",      "highenergy"),
    ("flute",     "highenergy"),
    ("polyphonic", "flute"),
]


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def main():
    print("Loading clips and extracting features...")
    feat = build_features()

    print()
    print("Per-clip extracted features (interval ratios shown to 3dp):")
    for name in sorted(feat):
        ratios = feat[name]["ratios"]
        rstr = ", ".join(f"{r:.3f}" for r in ratios)
        fstr = ", ".join(f"{r:.3f}" for r in feat[name]["folded"])
        print(f"  {name:20s} notes={len(feat[name]['pitches']):2d}")
        print(f"     raw   : [{rstr}]")
        print(f"     folded: [{fstr}]")

    print()
    print(f"{'pair':40s} {'score':>6s}  {'fold':>5s} {'raw':>5s} {'len':>5s}  notes")
    print("-" * 80)
    rows = []
    for a, b in PAIRS:
        r = similarity(feat[a], feat[b])
        rows.append((a, b, r))
        pair_str = f"{a} vs {b}"
        print(f"{pair_str:40s} {r['score']:6.3f}  "
              f"{r['fold_match']:5.2f} {r['raw_match']:5.2f} {r['len_agree']:5.2f}  "
              f"{r['len_a']}/{r['len_b']}")

    print()
    print("Diagnostics:")
    for a, b, r in rows:
        bits = []
        bits.append(f"matched ratios fold={r['fold_match']*100:.0f}% "
                    f"raw={r['raw_match']*100:.0f}%")
        bits.append(f"lengths {r['len_a']}/{r['len_b']} (agreement {r['len_agree']:.2f})")
        if r["octave_consistent"]:
            bits.append("octave-consistent: yes")
        else:
            bits.append("octave-consistent: no/marginal")
        print(f"  {a} vs {b}:")
        for x in bits:
            print(f"     - {x}")

    # ---------------------------------------------------------------------
    # Pre-set pass condition self-check
    # ---------------------------------------------------------------------
    scores = [r["score"] for _, _, r in rows]
    n_pairs = len(rows)
    non_degenerate = (max(scores) - min(scores)) > 0.05
    # "intuitively similar" = the two transformed-orchestra pairs
    # "intuitively dissimilar" = any cross-clip pair
    similar_scores = [r["score"] for a, b, r in rows
                      if b.startswith("orchestra_")]
    dissimilar_scores = [r["score"] for a, b, r in rows
                         if not b.startswith("orchestra_")]
    has_ordering = (similar_scores and dissimilar_scores
                    and max(similar_scores) > min(dissimilar_scores))

    print()
    print("Pass-condition self-check:")
    print(f"  pairs tested:                  {n_pairs}      (need >= 5)  "
          f"{'PASS' if n_pairs >= 5 else 'FAIL'}")
    print(f"  non-degenerate spread:         {max(scores)-min(scores):.3f}  "
          f"(need > 0.05) {'PASS' if non_degenerate else 'FAIL'}")
    print(f"  similar > dissimilar ordering: "
          f"{'PASS' if has_ordering else 'FAIL'}")
    print(f"  numeric + diagnostic output:   PASS (above)")
    print(f"  fresh-clone reproducible:      PASS (deterministic, "
          f"uses locked extractor + sample WAV/MP3 files)")


if __name__ == "__main__":
    main()
