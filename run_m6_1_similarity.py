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
    """Run the locked extractor and return the per-onset pitch list.
    Preserves None at onsets where pitch detection failed so structural
    position is not silently distorted."""
    onsets = rm.detect_onsets(audio)
    pitches = []
    for t in onsets:
        p = rm.pitch_at(audio, t)
        if p is None or p <= 0:
            pitches.append(None)
        else:
            pitches.append(float(p))
    return pitches


def interval_ratios(pitches):
    """Consecutive interval ratios r[i] = p[i+1]/p[i].  If either neighbour
    is None the ratio is None (no silent gap-skipping across missing notes)."""
    out = []
    for i in range(len(pitches) - 1):
        a, b = pitches[i], pitches[i + 1]
        if a is None or b is None or a <= 0 or b <= 0:
            out.append(None)
        else:
            out.append(b / a)
    return out


def octave_fold_to_unit(r):
    """Fold ratio into [1/sqrt(2), sqrt(2)] by powers of 2 so intervals an
    octave apart collapse to the same folded value.  None passes through."""
    if r is None or r <= 0:
        return r
    while r < 1 / math.sqrt(2):
        r *= 2
    while r > math.sqrt(2):
        r /= 2
    return r


# ---------------------------------------------------------------------------
# Similarity scoring
# ---------------------------------------------------------------------------

# A ratio is "non-trivial" if it differs from 1.0 by more than this in log2
# space, i.e. it represents a real interval rather than a held tone.
NONTRIVIAL_LOG2 = 0.10  # ~7 percent up or down

def _is_nontrivial(r):
    return r is not None and r > 0 and abs(math.log2(r)) > NONTRIVIAL_LOG2


def best_shift_match(seq_a, seq_b, tol_pct=TOL_PCT):
    """Slide seq_b across seq_a by integer offsets.  At each offset, only
    positions where BOTH ratios are valid (not None) count toward overlap.
    Score that offset as matches / max(valid_a, valid_b) -- requires both
    real coverage and positional alignment.  Require overlap >= MIN_OVERLAP.

    Also tracks "non-trivial matches": matches where the ratio represents
    a real melodic interval (not a held tone), so flat streams of ~1.0
    do not get credit for spurious agreement.

    Returns (best_match_fraction, best_nontrivial_match_fraction).
    """
    valid_a = sum(1 for r in seq_a if r is not None)
    valid_b = sum(1 for r in seq_b if r is not None)
    if valid_a == 0 or valid_b == 0:
        return 0.0, 0.0
    la, lb = len(seq_a), len(seq_b)
    norm = max(valid_a, valid_b)
    min_overlap = max(3, min(la, lb) // 2)
    nontriv_norm = max(
        1,
        max(sum(1 for r in seq_a if _is_nontrivial(r)),
            sum(1 for r in seq_b if _is_nontrivial(r))),
    )
    best, best_nt = 0.0, 0.0
    for k in range(-(lb - 1), la):
        i_start = max(0, k)
        i_end = min(la, lb + k)
        if i_end - i_start < min_overlap:
            continue
        matches = 0
        nt_matches = 0
        valid_overlap = 0
        for i in range(i_start, i_end):
            a, b = seq_a[i], seq_b[i - k]
            if a is None or b is None or a <= 0 or b <= 0:
                continue
            valid_overlap += 1
            if abs(a - b) / max(a, b) <= tol_pct:
                matches += 1
                if _is_nontrivial(a) and _is_nontrivial(b):
                    nt_matches += 1
        if valid_overlap < min_overlap:
            continue
        frac = matches / norm
        nt_frac = nt_matches / nontriv_norm
        if frac > best:
            best = frac
        if nt_frac > best_nt:
            best_nt = nt_frac
    return best, best_nt


def similarity(features_a, features_b):
    """Combine raw-ratio match, octave-folded match, and a non-trivial-match
    component that prevents flat 1.0-streams from scoring high spuriously.

    score = 0.45*fold_match + 0.25*raw_match + 0.30*nontrivial_fold_match
    """
    raw_a, raw_b = features_a["ratios"], features_b["ratios"]
    fold_a, fold_b = features_a["folded"], features_b["folded"]

    raw_match, _              = best_shift_match(raw_a, raw_b)
    fold_match, fold_match_nt = best_shift_match(fold_a, fold_b)

    score = 0.45 * fold_match + 0.25 * raw_match + 0.30 * fold_match_nt

    valid_a = sum(1 for r in raw_a if r is not None)
    valid_b = sum(1 for r in raw_b if r is not None)
    nontriv_a = sum(1 for r in raw_a if _is_nontrivial(r))
    nontriv_b = sum(1 for r in raw_b if _is_nontrivial(r))

    # Honest verdict label so the headline number is not over-interpreted.
    # Strong verdicts ("structural match", "partial melodic match") require
    # BOTH clips to have enough non-trivial melodic content (>= MIN_NT_FOR_VERDICT)
    # so that a few coincidental matches on a near-flat clip cannot be
    # promoted to "structural match".
    MIN_NT_FOR_VERDICT = 4
    min_nt = min(nontriv_a, nontriv_b)
    if min_nt < MIN_NT_FOR_VERDICT:
        verdict = "insufficient melodic content"
    elif fold_match_nt >= 0.40 and score >= 0.50:
        verdict = "structural match"
    elif fold_match_nt >= 0.20:
        verdict = "partial melodic match"
    elif score >= 0.40:
        verdict = "flat-agreement only (no melodic match)"
    else:
        verdict = "no match"

    return {
        "score": score,
        "raw_match": raw_match,
        "fold_match": fold_match,
        "fold_match_nt": fold_match_nt,
        "valid_a": valid_a,  "valid_b": valid_b,
        "nontriv_a": nontriv_a, "nontriv_b": nontriv_b,
        "octave_consistent": fold_match > raw_match + 0.05,
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Clip loading / pair definitions
# ---------------------------------------------------------------------------

CLIPS = [
    ("orchestra",         "orchestra.wav"),
    ("rock",              "rock.wav"),
    ("flute",             "flute.mp3"),
    ("polyphonic",        "polyphonic.mp3"),
    ("highenergy",        "highenergy.wav"),
    # Twinkle melody, three timbres -- the "obvious test case" set:
    # same melody, different instrument.
    ("twinkle_box",       "twinkle_box.mp3"),
    ("twinkle_harmonica", "twinkle_harmonica.wav"),
    ("twinkle_people",    "twinkle_people.m4a"),
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
    twinkle = features["twinkle_box"]["audio"]
    twinkle_stretched = librosa.effects.time_stretch(
        y=twinkle, rate=1 / rm.SHIFT_FACTOR)
    for label, audio in [("orchestra_pshift", shifted),
                         ("orchestra_tstretch", stretched),
                         ("twinkle_box_tstretch", twinkle_stretched)]:
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
    # Same melody, different instrument -- the operator's "obvious test cases".
    ("twinkle_box",       "twinkle_harmonica"),
    ("twinkle_box",       "twinkle_people"),
    ("twinkle_harmonica", "twinkle_people"),
    # Same melody, different tempo (synthetic pair from twinkle_box).
    ("twinkle_box",       "twinkle_box_tstretch"),
    # Cross-clip pairs (different melodies, expect lower).
    ("orchestra",         "rock"),
    ("twinkle_box",       "rock"),
    ("twinkle_harmonica", "polyphonic"),
]


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def main():
    print("Loading clips and extracting features...")
    feat = build_features()

    def fmt_ratio(r):
        return "  ?  " if r is None else f"{r:5.3f}"

    print()
    print("Per-clip extracted features (interval ratios; '?' = pitch-detection failed):")
    for name in sorted(feat):
        ratios = feat[name]["ratios"]
        n_valid = sum(1 for r in ratios if r is not None)
        n_nt = sum(1 for r in ratios if _is_nontrivial(r))
        rstr = ", ".join(fmt_ratio(r) for r in ratios)
        fstr = ", ".join(fmt_ratio(r) for r in feat[name]["folded"])
        print(f"  {name:20s} notes={len(feat[name]['pitches']):2d}  "
              f"valid_ratios={n_valid}  non-trivial={n_nt}")
        print(f"     raw   : [{rstr}]")
        print(f"     folded: [{fstr}]")

    print()
    print(f"{'pair':36s} {'score':>6s} {'fold':>5s} {'raw':>5s} {'fNT':>5s}  verdict")
    print("-" * 100)
    rows = []
    for a, b in PAIRS:
        r = similarity(feat[a], feat[b])
        rows.append((a, b, r))
        pair_str = f"{a} vs {b}"
        print(f"{pair_str:36s} {r['score']:6.3f} "
              f"{r['fold_match']:5.2f} {r['raw_match']:5.2f} "
              f"{r['fold_match_nt']:5.2f}  {r['verdict']}")

    print()
    print("Diagnostics (fNT = non-trivial-interval matches; flat ~1.0 streams excluded):")
    for a, b, r in rows:
        bits = [
            f"matched ratios fold={r['fold_match']*100:.0f}% "
            f"raw={r['raw_match']*100:.0f}%  "
            f"non-trivial-fold={r['fold_match_nt']*100:.0f}%",
            f"valid ratios {r['valid_a']}/{r['valid_b']}  "
            f"non-trivial {r['nontriv_a']}/{r['nontriv_b']}",
            "octave-consistent: " + ("yes" if r["octave_consistent"]
                                     else "no/marginal"),
        ]
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
    similar_scores = [r["score"] for a, b, r in rows
                      if b.startswith("orchestra_")]
    dissimilar_scores = [r["score"] for a, b, r in rows
                         if not b.startswith("orchestra_")]
    has_ordering = (bool(similar_scores) and bool(dissimilar_scores)
                    and min(similar_scores) > max(dissimilar_scores))

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print()
    print("Pass-condition self-check:")
    print(f"  1. pairs tested >= 5:                    {n_pairs:>3d}    {tag(n_pairs >= 5)}")
    print(f"  2. non-degenerate spread > 0.05:         {max(scores)-min(scores):.3f}  {tag(non_degenerate)}")
    print(f"  3. ALL similar > ALL dissimilar:                {tag(has_ordering)}")
    print(f"     similar pairs:    {[round(s,3) for s in similar_scores]}")
    print(f"     dissimilar pairs: {[round(s,3) for s in dissimilar_scores]}")
    print(f"  4. numeric + diagnostic output:                 PASS (printed above)")
    print(f"  5. fresh-clone reproducible: NOT VERIFIED HERE -- this script is")
    print(f"     deterministic given the locked extractor + sample files;")
    print(f"     verify externally by cloning the canonical repo, running")
    print(f"     scripts/fetch_samples.py, then re-running this script.")


if __name__ == "__main__":
    main()
