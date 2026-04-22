"""
M3.4 — Focused search in the good region revealed by M3.3.

M3.3 found:
  - onset_delta peaks near 0.05
  - fmin peaks at 30-40 (BEATS baseline at 50)
  - fmax is irrelevant across 2000-16000 on these clips

This script exploits that knowledge: it samples 40 seeded trials over a
narrow box around the joint sweet spot, with fmax pinned at the baseline
value so any score change is attributable only to (onset_delta, fmin).

Usage:
    python run_m3_4_focused_search.py
"""

import json
import random

from run_m3_1_metric import evaluate_m3_1

BASELINE_CONFIG = {
    "onset_delta": 0.05,
    "fmin": 50,
    "fmax": 16000,
}

SEARCH_SPACE = {
    "onset_delta": (0.035, 0.065),
    "fmin": (25, 50),
}
FIXED_FMAX = 16000

N_TRIALS = 40
SEED = 42


def sample_config():
    return {
        "onset_delta": round(random.uniform(*SEARCH_SPACE["onset_delta"]), 3),
        "fmin": random.randint(*SEARCH_SPACE["fmin"]),
        "fmax": FIXED_FMAX,
    }


def fmt_cfg(cfg):
    return f"onset_delta={cfg['onset_delta']:.3f}  fmin={cfg['fmin']:>2d}  fmax={cfg['fmax']}"


def main():
    random.seed(SEED)

    print("=" * 78)
    print(f"M3.4 focused search  |  N_TRIALS={N_TRIALS}  SEED={SEED}")
    print(f"  onset_delta in {SEARCH_SPACE['onset_delta']}")
    print(f"  fmin in {SEARCH_SPACE['fmin']}")
    print(f"  fmax fixed at {FIXED_FMAX}")
    print("=" * 78)

    trials = []
    base = evaluate_m3_1(BASELINE_CONFIG)
    trials.append({
        "label": "baseline",
        "config": BASELINE_CONFIG,
        "score": base["score"],
        "within_tolerance": base["within_tolerance"],
        "total_notes": base["total_notes"],
    })
    print(f"baseline  score={base['score']:.4f}  "
          f"{base['within_tolerance']:>2d}/{base['total_notes']}  {fmt_cfg(BASELINE_CONFIG)}")
    print("-" * 78)

    for i in range(N_TRIALS):
        cfg = sample_config()
        r = evaluate_m3_1(cfg)
        trials.append({
            "label": f"trial_{i+1:02d}",
            "config": cfg,
            "score": r["score"],
            "within_tolerance": r["within_tolerance"],
            "total_notes": r["total_notes"],
        })
        print(f"trial_{i+1:02d}  score={r['score']:.4f}  "
              f"{r['within_tolerance']:>2d}/{r['total_notes']}  {fmt_cfg(cfg)}")

    ranked = sorted(trials, key=lambda x: (-x["score"], x["label"]))
    baseline_score = trials[0]["score"]
    above = [t for t in trials if t["score"] > baseline_score]
    ties  = [t for t in trials if t["score"] == baseline_score and t["label"] != "baseline"]

    print("\n" + "=" * 78)
    print("Top 10")
    print("=" * 78)
    for row in ranked[:10]:
        marker = " *" if row["label"] == "baseline" else "  "
        print(f"{marker}{row['label']:>10s}  score={row['score']:.4f}  "
              f"{row['within_tolerance']:>2d}/{row['total_notes']}  {fmt_cfg(row['config'])}")

    print(f"\nbaseline score: {baseline_score:.4f}")
    print(f"trials above baseline: {len(above)} / {N_TRIALS}")
    print(f"trials tied with baseline: {len(ties)} / {N_TRIALS}")
    if above:
        best = ranked[0]
        print(f"new best: {best['label']}  score={best['score']:.4f}  {fmt_cfg(best['config'])}")
    else:
        print("baseline not beaten in focused region")

    with open("m3_4_results.json", "w") as f:
        json.dump({
            "seed": SEED, "n_trials": N_TRIALS,
            "search_space": SEARCH_SPACE, "fixed_fmax": FIXED_FMAX,
            "baseline_score": baseline_score,
            "trials_above_baseline": len(above),
            "trials_tied": len(ties),
            "ranked": ranked,
        }, f, indent=2)
    print("Wrote m3_4_results.json")


if __name__ == "__main__":
    main()
