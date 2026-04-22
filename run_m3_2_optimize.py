"""
M3.2 — Random search over extractor configs against the M3.1 metric.

Optimizes only extractor knobs (onset_delta, fmin, fmax).  The scoring
tolerance stays fixed at the M3.1 default (1%) so the search cannot game
the metric.  Seeded for reproducibility.

Usage:
    python run_m3_2_optimize.py

Pass criteria:
    1. baseline reproduced inside the optimizer
    2. >= 1 non-baseline config evaluated successfully
    3. ranked leaderboard printed
Strong pass:
    best-found config beats baseline (>0.9167) on the same six cases.
"""

import json
import random

from run_m3_1_metric import evaluate_m3_1

BASELINE_CONFIG = {
    "onset_delta": 0.05,
    "fmin": 50,
    "fmax": 16000,
}

N_TRIALS = 20
SEED = 42


def sample_config():
    while True:
        cfg = {
            "onset_delta": round(random.uniform(0.01, 0.25), 3),
            "fmin": random.randint(30, 120),
            "fmax": random.randint(2000, 16000),
        }
        if cfg["fmin"] < cfg["fmax"]:
            return cfg


def fmt_cfg(cfg):
    return f"onset_delta={cfg['onset_delta']:.3f}  fmin={cfg['fmin']:>3d}  fmax={cfg['fmax']:>5d}"


def main():
    random.seed(SEED)
    trials = []

    base = evaluate_m3_1(config=BASELINE_CONFIG)
    trials.append({
        "label": "baseline",
        "config": BASELINE_CONFIG,
        "score": base["score"],
        "within_tolerance": base["within_tolerance"],
        "total_notes": base["total_notes"],
    })

    print("=" * 80)
    print(f"M3.2 random search  |  N_TRIALS={N_TRIALS}  SEED={SEED}")
    print("=" * 80)
    print(f"baseline   score={base['score']:.4f}  "
          f"{base['within_tolerance']:>2d}/{base['total_notes']}  {fmt_cfg(BASELINE_CONFIG)}")
    print("-" * 80)

    for i in range(N_TRIALS):
        cfg = sample_config()
        r = evaluate_m3_1(config=cfg)
        trials.append({
            "label": f"trial_{i+1:02d}",
            "config": cfg,
            "score": r["score"],
            "within_tolerance": r["within_tolerance"],
            "total_notes": r["total_notes"],
        })
        print(f"trial_{i+1:02d}   score={r['score']:.4f}  "
              f"{r['within_tolerance']:>2d}/{r['total_notes']}  {fmt_cfg(cfg)}")

    ranked = sorted(trials, key=lambda x: (-x["score"], x["label"]))

    print("\n" + "=" * 80)
    print("Top 10 by M3.1 score")
    print("=" * 80)
    for row in ranked[:10]:
        marker = " *" if row["label"] == "baseline" else "  "
        print(f"{marker}{row['label']:>10s}  score={row['score']:.4f}  "
              f"{row['within_tolerance']:>2d}/{row['total_notes']}  {fmt_cfg(row['config'])}")

    best = ranked[0]
    beats = best["score"] > trials[0]["score"]
    ties = best["score"] == trials[0]["score"]
    verdict = "BEATS baseline" if beats else ("TIES baseline" if ties else "below baseline")
    print(f"\nBest: {best['label']}  score={best['score']:.4f}  ({verdict})")

    with open("m3_2_results.json", "w") as f:
        json.dump({
            "seed": SEED,
            "n_trials": N_TRIALS,
            "baseline_score": trials[0]["score"],
            "best": best,
            "ranked": ranked,
        }, f, indent=2)
    print("Wrote m3_2_results.json")


if __name__ == "__main__":
    main()
