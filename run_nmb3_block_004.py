"""
NMB3 Block 004 -- M3.1 closure block: onset_delta boundary coverage.

Per nmb3/nmb3_blocks/block_004_plan.md (autonomously approved as
the final M3.1 closure block).

Question: Does the M3.1 invariance score continue to track onset_delta
in the unmeasured boundary regions {0.01, 0.03, 0.25}, and is the
resulting combined sweep consistent with the partial Block 002
evidence and the zero noise floor established by Block 003?

This runner evaluates the M3.1 invariance metric at the three
boundary onset_delta values that were missing from Block 002, then
prints a single unified table combining:

  - the three new values (0.01, 0.03, 0.25)
  - the four Block 002 values (0.05 baseline, 0.10, 0.15, 0.20)
  - explicit comparison against the Block 003 baseline noise floor
    (population stdev = 0.0000, span = 0.0000, bit-identical 8/8)

The Block 002 values are referenced as constants -- they are not
re-run, both to honour the plan's 'Forbidden Actions' clause and
because re-running them would consume CI budget for no new evidence
(Block 003 proved the pipeline is deterministic).

No core pipeline code is modified.  No parameter other than
onset_delta is varied.
"""

from __future__ import annotations

from typing import Any

from run_m3_1_metric import evaluate_m3_1
from run_milestones import DEFAULT_CONFIG

NEW_ONSET_DELTAS = (0.01, 0.03, 0.25)

BLOCK_002_RESULTS = {
    0.05: {"score": 0.8750, "within": 42, "total": 48},
    0.10: {"score": 0.7917, "within": 38, "total": 48},
    0.15: {"score": 0.8125, "within": 39, "total": 48},
    0.20: {"score": 0.7917, "within": 38, "total": 48},
}

BASELINE_DELTA = 0.05
BLOCK_003_NOISE_STDEV = 0.0000
BLOCK_003_NOISE_SPAN = 0.0000
NOTE_RESOLUTION = 1.0 / 48.0


def _evaluate(onset_delta: float) -> dict[str, Any]:
    config = dict(DEFAULT_CONFIG)
    config["onset_delta"] = onset_delta
    result = evaluate_m3_1(config=config)
    return {
        "score": float(result["score"]),
        "within": int(result["within_tolerance"]),
        "total": int(result["total_notes"]),
    }


def main() -> None:
    print("=" * 78)
    print("NMB3 Block 004 -- M3.1 closure: onset_delta boundary coverage")
    print("=" * 78)
    print()
    print("Plan:        nmb3/nmb3_blocks/block_004_plan.md")
    print(f"New values:  onset_delta in {list(NEW_ONSET_DELTAS)}")
    print("Reference:   onset_delta in [0.05, 0.10, 0.15, 0.20]")
    print("             (Block 002, 4 / 7 originally planned values)")
    print(f"Noise floor: stdev = {BLOCK_003_NOISE_STDEV:.4f},  "
          f"span = {BLOCK_003_NOISE_SPAN:.4f}")
    print("             (Block 003, 8 bit-identical baseline runs)")
    print()

    new_results: dict[float, dict[str, Any]] = {}
    for d in NEW_ONSET_DELTAS:
        new_results[d] = _evaluate(d)

    baseline_score = BLOCK_002_RESULTS[BASELINE_DELTA]["score"]

    combined: list[tuple[float, dict[str, Any], str]] = []
    for d in NEW_ONSET_DELTAS:
        combined.append((d, new_results[d], "block_004"))
    for d, r in BLOCK_002_RESULTS.items():
        combined.append((d, r, "block_002"))
    combined.sort(key=lambda x: x[0])

    print("Unified onset_delta sweep (block_002 + block_004):")
    print()
    print(f"{'onset_delta':>11}   {'score':>7}   {'within / total':>16}   "
          f"{'delta vs 0.05':>14}   {'note flips':>10}   {'source':>10}")
    print("-" * 78)
    for d, r, source in combined:
        delta = r["score"] - baseline_score
        if abs(delta) < 1e-9:
            delta_str = "baseline"
            flips_str = "-"
        else:
            delta_str = f"{delta:+.4f}"
            flips_str = f"{delta / NOTE_RESOLUTION:+.1f}"
        print(f"{d:>11.2f}   {r['score']:>7.4f}   {r['within']:>4} / "
              f"{r['total']:<8}   {delta_str:>14}   {flips_str:>10}   "
              f"{source:>10}")

    print()
    print("Signal-vs-noise check (every nonzero delta vs Block 003 noise floor):")
    if BLOCK_003_NOISE_STDEV == 0.0:
        print("  Baseline stdev is exactly 0.0000 (Block 003).  Every nonzero")
        print("  delta in the table above is therefore infinitely many baseline")
        print("  stdevs above the noise floor and represents real metric")
        print("  response, not pipeline jitter.")
    else:
        for d, r, _ in combined:
            delta = r["score"] - baseline_score
            if abs(delta) < 1e-9:
                continue
            ratio = abs(delta) / BLOCK_003_NOISE_STDEV
            print(f"  onset_delta = {d:.2f}  delta = {delta:+.4f}  "
                  f"|delta| / stdev = {ratio:>6.2f}")

    print()
    print("Boundary-region observations (for the Interpreter Agent):")
    new_scores = [new_results[d]["score"] for d in NEW_ONSET_DELTAS]
    new_min = min(new_scores)
    new_max = max(new_scores)
    in_unit = all(0.0 <= s <= 1.0 for s in new_scores)
    print(f"  new boundary scores: {new_scores}")
    print(f"  new boundary range:  [{new_min:.4f}, {new_max:.4f}]")
    print(f"  all boundary scores in [0.0, 1.0]: {in_unit}")
    if any(s == 0.0 for s in new_scores):
        print("  WARNING: at least one boundary score is exactly 0.0 "
              "(possible saturation / breakdown).")
    if any(s == 1.0 for s in new_scores):
        print("  WARNING: at least one boundary score is exactly 1.0 "
              "(possible saturation at upper bound).")

    all_scores = [r["score"] for _, r, _ in combined]
    sweep_min = min(all_scores)
    sweep_max = max(all_scores)
    print(f"  combined 7-point sweep range: [{sweep_min:.4f}, {sweep_max:.4f}]")
    print(f"  combined 7-point sweep span:  {sweep_max - sweep_min:.4f}")
    print()
    print("Interpretation is the Interpreter Agent's responsibility -- this")
    print("runner only produces evidence.  No M3.1 closure declaration is")
    print("made here; the closure recommendation is written separately to")
    print("nmb3/nmb3_reports/m3_1_closure_recommendation.md after this block.")


if __name__ == "__main__":
    main()
