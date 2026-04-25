"""
NMB3 Block 003 -- baseline stability / noise-floor characterisation.

Per nmb3/nmb3_blocks/block_003_plan.md (autonomously approved under
nmb3/nmb3_decision_policy.md):

  Question: Are baseline M3.1 scores stable enough that Block 002
  score deltas can be interpreted as real parameter sensitivity?

This runner invokes the locked M3.1 invariance metric N times with
no parameter changes (run_milestones.DEFAULT_CONFIG verbatim,
onset_delta = 0.05) and characterises the run-to-run distribution
of the score.  It also checks per-case bit-identity across runs and
explicitly compares the observed baseline jitter against the
Block 002 deltas (0.0625 and 0.0833).

No core pipeline code is modified.  No parameter is varied.
"""

from __future__ import annotations

import statistics
from typing import Any

from run_m3_1_metric import evaluate_m3_1
from run_milestones import DEFAULT_CONFIG

N_RUNS = 8
BLOCK_002_DELTAS = (0.0625, 0.0833)
NOTE_RESOLUTION = 1.0 / 48.0


def _case_signature(case_results: list[dict[str, Any]]) -> tuple:
    """Stable hashable signature of per-case verdicts for bit-identity check."""
    sig = []
    for case in case_results:
        sig.append(
            (
                case.get("label") or case.get("name") or "",
                case.get("test") or "",
                case.get("within_tolerance"),
                case.get("total_notes"),
                case.get("raw_score"),
                case.get("folded_score"),
            )
        )
    return tuple(sig)


def main() -> None:
    print("=" * 78)
    print("NMB3 Block 003 -- baseline stability / noise-floor characterisation")
    print("=" * 78)
    print()
    print(f"Plan:        nmb3/nmb3_blocks/block_003_plan.md")
    print(f"Config:      run_milestones.DEFAULT_CONFIG (no overrides)")
    print(f"Repetitions: {N_RUNS}")
    print()

    runs: list[dict[str, Any]] = []
    signatures: list[tuple] = []

    print(f"{'run':>4}   {'score':>8}   {'within / total':>16}")
    print("-" * 78)

    for i in range(1, N_RUNS + 1):
        result = evaluate_m3_1(config=dict(DEFAULT_CONFIG))
        score = float(result["score"])
        total = int(result["total_notes"])
        within = int(result["within_tolerance"])
        sig = _case_signature(result["case_results"])
        runs.append({"score": score, "within": within, "total": total})
        signatures.append(sig)
        print(f"{i:>4}   {score:>8.4f}   {within:>4} / {total:<8}")

    scores = [r["score"] for r in runs]
    mean = statistics.fmean(scores)
    stdev = statistics.pstdev(scores) if len(scores) > 1 else 0.0
    smin = min(scores)
    smax = max(scores)
    span = smax - smin

    distinct_sigs = len(set(signatures))
    bit_identical = distinct_sigs == 1

    print()
    print("Summary statistics:")
    print(f"  mean   = {mean:.4f}")
    print(f"  stdev  = {stdev:.4f}  (population stdev across {N_RUNS} runs)")
    print(f"  min    = {smin:.4f}")
    print(f"  max    = {smax:.4f}")
    print(f"  span   = {span:.4f}  (max - min)")
    print()
    print("Per-case bit-identity check:")
    print(f"  distinct case-result signatures across {N_RUNS} runs: {distinct_sigs}")
    print(f"  bit-identical: {bit_identical}")
    print()
    print("Signal-vs-noise comparison against Block 002 deltas:")
    print(f"  note resolution                  = 1 / 48 = {NOTE_RESOLUTION:.4f}")
    print(f"  baseline span (this block)       = {span:.4f}")
    print(f"  baseline stdev (this block)      = {stdev:.4f}")
    for d in BLOCK_002_DELTAS:
        ratio = (d / stdev) if stdev > 0 else float("inf")
        clearly_above = "yes" if d > max(span, NOTE_RESOLUTION) else "no"
        ratio_str = f"{ratio:>6.2f}" if ratio != float("inf") else "   inf"
        print(
            f"  block_002 delta = {d:.4f}  -> "
            f"delta/stdev = {ratio_str}  "
            f"clearly above baseline jitter? {clearly_above}"
        )
    print()
    print("Interpretation guidance (for the Interpreter Agent):")
    if bit_identical:
        print("  All 8 runs produced bit-identical case-level results and")
        print("  identical scores.  The M3.1 metric pipeline is deterministic")
        print("  under repeated invocation with identical inputs.  The noise")
        print("  floor of the metric itself is therefore zero, and the")
        print("  Block 002 deltas (0.0625 and 0.0833) cannot be attributed to")
        print("  pipeline jitter -- they are real responses to onset_delta.")
    else:
        print("  Runs were NOT bit-identical.  The metric pipeline contains a")
        print("  source of nondeterminism.  See the table above for the")
        print("  observed score distribution and the delta/stdev ratios for")
        print("  the Block 002 deltas.  Interpretation must be done by the")
        print("  Interpreter Agent against nmb3/nmb3_decision_policy.md.")


if __name__ == "__main__":
    main()
