"""
NMB3 Block 002 runner — onset_delta sweep.

Implements the experiment defined in nmb3/nmb3_blocks/block_002_plan.md:
isolate the onset_delta parameter and measure the M3.1 invariance score
across a fixed sweep of values.  No other parameter is varied.

Sweep:
    onset_delta = [0.05, 0.10, 0.15, 0.20]
    (0.05 is the locked baseline value)

All other config fields are taken verbatim from run_milestones.DEFAULT_CONFIG,
i.e. the same locked extractor used by run_m3_1_metric.py.

Output: a single table written to stdout (the GitHub Actions workflow
captures it via `tee` into nmb3/nmb3_logs/current_block_output.txt).
"""

import os
import sys

from run_m3_1_metric import evaluate_m3_1


ONSET_DELTA_VALUES = [0.05, 0.10, 0.15, 0.20]
BASELINE_VALUE = 0.05


def main():
    for f in ("orchestra.wav", "rock.wav"):
        if not os.path.isfile(f):
            sys.stderr.write(
                f"Missing {f}.  Run: python scripts/fetch_samples.py\n"
            )
            sys.exit(1)

    print("=" * 78)
    print("NMB3 Block 002 — onset_delta sweep (M3.1 invariance metric)")
    print("=" * 78)
    print()
    print("Plan:        nmb3/nmb3_blocks/block_002_plan.md")
    print("Sweep:       onset_delta in", ONSET_DELTA_VALUES)
    print(f"Baseline:    onset_delta = {BASELINE_VALUE} (other params unchanged)")
    print()
    print(f"{'onset_delta':>11s}   {'score':>8s}   {'within / total':>14s}   "
          f"{'delta vs baseline':>17s}")
    print("-" * 78)

    rows = []
    baseline_score = None
    for value in ONSET_DELTA_VALUES:
        result = evaluate_m3_1(config={"onset_delta": value})
        score = result["score"]
        within = result["within_tolerance"]
        total = result["total_notes"]
        if value == BASELINE_VALUE:
            baseline_score = score
        rows.append((value, score, within, total))

    for value, score, within, total in rows:
        if baseline_score is None:
            delta_str = "n/a"
        else:
            delta = score - baseline_score
            tag = "baseline" if value == BASELINE_VALUE else f"{delta:+.4f}"
            delta_str = tag
        print(f"{value:>11.2f}   {score:>8.4f}   "
              f"{within:>5d} / {total:<5d}   {delta_str:>17s}")

    print()
    print("Single-parameter sweep: only onset_delta varied; all other config")
    print("fields are run_milestones.DEFAULT_CONFIG (locked M5.6 extractor).")
    print()
    print("Pass condition (per block_002_plan.md): scores characterise the")
    print("response of the invariance metric to onset_delta.  Interpretation")
    print("is the Interpreter Agent's responsibility -- this runner only")
    print("produces evidence.")


if __name__ == "__main__":
    main()
