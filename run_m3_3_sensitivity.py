"""
M3.3 — Sensitivity sweeps for the M3.1 invariance metric.

Hold two extractor knobs at baseline, vary the third across a sensible
range, and record the M3.1 score.  Produces three one-dimensional curves:
score vs onset_delta, score vs fmin, score vs fmax.

Usage:
    python run_m3_3_sensitivity.py

Reads the same six locked milestone cases as M3.1 / M3.2.
"""

import json

from run_m3_1_metric import evaluate_m3_1

BASELINE = {
    "onset_delta": 0.05,
    "fmin": 50,
    "fmax": 16000,
}

SWEEPS = {
    "onset_delta": [0.01, 0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20],
    "fmin":        [30, 40, 50, 60, 80, 100, 120],
    "fmax":        [2000, 3000, 5000, 8000, 12000, 16000],
}


def sweep(param, values):
    rows = []
    for v in values:
        cfg = dict(BASELINE)
        cfg[param] = v
        r = evaluate_m3_1(config=cfg)
        rows.append({"value": v, "score": r["score"],
                     "within_tolerance": r["within_tolerance"],
                     "total_notes": r["total_notes"]})
    return rows


def print_sweep(param, rows):
    print(f"\n{param}  (others at baseline {BASELINE})")
    print(f"  {param:>12s}   score    within / total")
    print(f"  {'-'*12}   ------   --------------")
    best = max(r["score"] for r in rows)
    for r in rows:
        marker = "  <-- peak" if r["score"] == best else ""
        v = r["value"]
        vstr = f"{v:.3f}" if isinstance(v, float) else f"{v}"
        print(f"  {vstr:>12s}   {r['score']:.4f}   "
              f"{r['within_tolerance']:>2d} / {r['total_notes']:<2d}{marker}")


def main():
    print("=" * 70)
    print("M3.3 — Sensitivity sweeps vs M3.1")
    print("=" * 70)

    out = {"baseline": BASELINE, "sweeps": {}}
    for param, values in SWEEPS.items():
        rows = sweep(param, values)
        out["sweeps"][param] = rows
        print_sweep(param, rows)

    with open("m3_3_sensitivity.json", "w") as f:
        json.dump(out, f, indent=2)
    print("\nWrote m3_3_sensitivity.json")


if __name__ == "__main__":
    main()
