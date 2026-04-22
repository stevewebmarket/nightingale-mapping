"""
M3.1 — Audio Transform Invariance Metric

Computes a single invariance score from the existing milestone pipeline:

    score = notes_within_tolerance / total_notes

across the six locked cases (orchestra + rock x pitch shift, time stretch,
composition).  This is the real metric: it grades whether the extractor
preserves pitch-ratio structure across real audio transforms, NOT whether
the system can recover its own synthetic regenerations.

Usage:
    python run_m3_1_metric.py

Pass criteria:
    - Baseline score is stable across repeated runs
    - At least 2 config mutants produce different scores from baseline
"""

import copy
import os
import sys

from run_milestones import (
    DEFAULT_CONFIG, load_clip, compute_milestone_scores,
)


def compute_invariance_score(case_results):
    total_within = sum(c["within_tolerance"] for c in case_results)
    total_notes = sum(c["total_notes"] for c in case_results)
    score = total_within / total_notes if total_notes else 0.0
    return {
        "within_tolerance": total_within,
        "total_notes": total_notes,
        "score": score,
    }


def evaluate_config(orchestra, rock, cfg):
    case_results = compute_milestone_scores(orchestra, rock, cfg)
    summary = compute_invariance_score(case_results)
    return summary, case_results


def main():
    for f in ("orchestra.wav", "rock.wav"):
        if not os.path.isfile(f):
            sys.stderr.write(f"Missing {f}.  Run: python scripts/fetch_samples.py\n")
            sys.exit(1)

    orchestra = load_clip("orchestra.wav")
    rock = load_clip("rock.wav")

    baseline = dict(DEFAULT_CONFIG)
    mut_a = copy.deepcopy(baseline); mut_a["onset_delta"] = 0.20
    mut_b = copy.deepcopy(baseline); mut_b["fmax"] = 4000
    mut_c = copy.deepcopy(baseline); mut_c["tolerance_pct"] = 0.001

    configs = [
        ("baseline                       ", baseline),
        ("mutant_a (onset_delta 0.05->0.20)", mut_a),
        ("mutant_b (fmax 16000->4000)     ", mut_b),
        ("mutant_c (tolerance 1%->0.1%)   ", mut_c),
    ]

    print("=" * 78)
    print("M3.1 — Audio Transform Invariance Metric")
    print("=" * 78)
    print()
    print(f"{'config':36s}  {'score':>8s}   within / total   per-case (folded)")
    print("-" * 78)

    for name, cfg in configs:
        summary, cases = evaluate_config(orchestra, rock, cfg)
        per = "  ".join(f"{c['label'][:4]}/{c['test'][:5]}={c['within_tolerance']}/{c['total_notes']}"
                       for c in cases)
        print(f"{name}  {summary['score']:>8.4f}   "
              f"{summary['within_tolerance']:>3d} / {summary['total_notes']:<3d}        {per}")

    print()
    print("Pass = baseline stable across runs AND >=2 mutants move from baseline.")


if __name__ == "__main__":
    main()
