"""
NMB3 Block 005 -- M3.1 per-case decomposition of the mid-range
onset_delta plateau.

Per nmb3/nmb3_blocks/block_005_plan.md.  Authorised by Steve in
nmb3/nmb3_decisions.log entries at 2026-04-25T16:34:20Z (Option 2
of the M3.1 closure recommendation, naming O002 explicitly) and
2026-04-25T16:46:06Z ("Execute O002").

Question: Within the mid-range plateau (onset_delta in
{0.10, 0.15, 0.20}, aggregate scores 0.7917 / 0.8125 / 0.7917
from Block 002 + Block 004), is the non-monotonic 0.10 -> 0.15
-> 0.20 movement driven uniformly across the 6 canonical cases,
or by one or two specific cases whose within-tolerance counts
shift?

This runner evaluates the M3.1 invariance metric at each of the
three plateau deltas TWICE, performs a per-case bit-identical
determinism check across the two passes (6 cases x 3 deltas =
18 pairs), cross-checks that the aggregate score at each delta
matches the published Block 002 / Block 004 value, and prints a
per-case decomposition table that the Interpreter Agent can read
directly to decide between H1 (real metric property) and H2
(sample-specific artefact).

No core pipeline code is modified.  No parameter other than
onset_delta is varied.  M3.1 closure is not re-opened; this is
a follow-on within the already-closed milestone.
"""

from __future__ import annotations

import sys
from typing import Any

from run_m3_1_metric import evaluate_m3_1
from run_milestones import DEFAULT_CONFIG  # noqa: F401  (audited as locked)

PLATEAU_DELTAS = (0.10, 0.15, 0.20)

PUBLISHED_AGGREGATE_SCORES = {
    0.10: 0.7917,
    0.15: 0.8125,
    0.20: 0.7917,
}

NOTE_FLIP_FLAG_THRESHOLD = 1


def _run_one(onset_delta: float) -> dict[str, Any]:
    result = evaluate_m3_1(config={"onset_delta": onset_delta})
    return {
        "score": float(result["score"]),
        "within": int(result["within_tolerance"]),
        "total": int(result["total_notes"]),
        "cases": [
            {
                "label": str(c["label"]),
                "test": str(c["test"]),
                "within": int(c["within_tolerance"]),
                "total": int(c["total_notes"]),
            }
            for c in result["case_results"]
        ],
    }


def _case_key(case: dict[str, Any]) -> tuple[str, str]:
    return (case["label"], case["test"])


def main() -> int:
    print("=" * 78)
    print("NMB3 Block 005 -- M3.1 per-case decomposition of the "
          "mid-range plateau")
    print("=" * 78)
    print()
    print("Plan:        nmb3/nmb3_blocks/block_005_plan.md")
    print(f"Deltas:      onset_delta in {list(PLATEAU_DELTAS)}")
    print("Runs:        2 per delta (6 total) for determinism cross-check")
    print("Published:   aggregate score at "
          f"{list(PLATEAU_DELTAS)} = "
          f"{[PUBLISHED_AGGREGATE_SCORES[d] for d in PLATEAU_DELTAS]}")
    print("             (Block 002 + Block 004 reference)")
    print()

    runs: dict[float, list[dict[str, Any]]] = {}
    for d in PLATEAU_DELTAS:
        runs[d] = []
        for run_index in (1, 2):
            print(f"  running onset_delta={d:.2f}  pass {run_index}/2 ...",
                  flush=True)
            runs[d].append(_run_one(d))
    print()

    hard_failures: list[str] = []

    print("Aggregate cross-check vs published Block 002 / Block 004 values:")
    print(f"  {'onset_delta':>11}   {'observed':>9}   {'published':>9}   "
          f"{'match':>6}")
    print("  " + "-" * 52)
    for d in PLATEAU_DELTAS:
        observed = runs[d][0]["score"]
        published = PUBLISHED_AGGREGATE_SCORES[d]
        match = abs(round(observed, 4) - published) < 1e-9
        print(f"  {d:>11.2f}   {observed:>9.4f}   {published:>9.4f}   "
              f"{'YES' if match else '*NO*':>6}")
        if not match:
            hard_failures.append(
                f"aggregate score at onset_delta={d:.2f} = {observed:.4f} "
                f"does not match published {published:.4f}"
            )
    print()

    print("Determinism cross-check (per-case bit-identical across the two "
          "passes):")
    determinism_pairs_total = 0
    determinism_pairs_match = 0
    for d in PLATEAU_DELTAS:
        cases_run1 = runs[d][0]["cases"]
        cases_run2 = runs[d][1]["cases"]
        if len(cases_run1) != len(cases_run2):
            hard_failures.append(
                f"determinism: at onset_delta={d:.2f}, run 1 has "
                f"{len(cases_run1)} cases but run 2 has {len(cases_run2)}"
            )
            continue
        for c1, c2 in zip(cases_run1, cases_run2):
            determinism_pairs_total += 1
            if (_case_key(c1) == _case_key(c2)
                    and c1["within"] == c2["within"]
                    and c1["total"] == c2["total"]):
                determinism_pairs_match += 1
            else:
                hard_failures.append(
                    f"determinism regression: onset_delta={d:.2f} case "
                    f"{_case_key(c1)} run 1={(c1['within'], c1['total'])} "
                    f"vs run 2={(c2['within'], c2['total'])}"
                )
    print(f"  bit-identical (within, total) pairs: "
          f"{determinism_pairs_match} / {determinism_pairs_total}")
    if determinism_pairs_match == determinism_pairs_total:
        print("  -> PASS: every case is bit-identical across both passes")
    else:
        print("  -> *FAIL*: at least one per-case mismatch (see hard failures)")
    print()

    print("In-range check: every observed aggregate score in [0.0, 1.0]:")
    for d in PLATEAU_DELTAS:
        for run_index, run in enumerate(runs[d], start=1):
            in_range = 0.0 <= run["score"] <= 1.0
            print(f"  onset_delta={d:.2f}  pass {run_index}/2  "
                  f"score={run['score']:.4f}  in [0,1]: "
                  f"{'YES' if in_range else '*NO*'}")
            if not in_range:
                hard_failures.append(
                    f"out-of-range score at onset_delta={d:.2f} pass "
                    f"{run_index}: {run['score']}"
                )
    print()

    case_keys: list[tuple[str, str]] = [
        _case_key(c) for c in runs[PLATEAU_DELTAS[0]][0]["cases"]
    ]

    per_case: dict[tuple[str, str], dict[float, dict[str, int]]] = {
        k: {} for k in case_keys
    }
    for d in PLATEAU_DELTAS:
        for c in runs[d][0]["cases"]:
            per_case[_case_key(c)][d] = {
                "within": c["within"],
                "total": c["total"],
            }

    print("Per-case decomposition (6 cases x 3 deltas; values are "
          "within / total notes):")
    print()
    delta_headers = "   ".join(f"{'d=' + format(d, '.2f'):>11}"
                               for d in PLATEAU_DELTAS)
    print(f"  {'case (label / test)':<28}  {delta_headers}   "
          f"{'within span':>11}   {'flag':>4}")
    print("  " + "-" * (30 + len(delta_headers) + 22))

    flagged_cases: list[tuple[str, str, int]] = []
    for key in case_keys:
        label, test = key
        row_values = []
        within_values: list[int] = []
        total_values: list[int] = []
        for d in PLATEAU_DELTAS:
            entry = per_case[key][d]
            row_values.append(f"{entry['within']:>4} / {entry['total']:<4}")
            within_values.append(entry["within"])
            total_values.append(entry["total"])
        if len(set(total_values)) != 1:
            hard_failures.append(
                f"case {key} has inconsistent total_notes across deltas: "
                f"{total_values}"
            )
        within_span = max(within_values) - min(within_values)
        flag = "FLAG" if within_span >= NOTE_FLIP_FLAG_THRESHOLD else "-"
        if flag == "FLAG":
            flagged_cases.append((label, test, within_span))
        case_str = f"{label} / {test}"
        if len(case_str) > 28:
            case_str = case_str[:25] + "..."
        row_cells = "   ".join(f"{v:>11}" for v in row_values)
        print(f"  {case_str:<28}  {row_cells}   {within_span:>11d}   "
              f"{flag:>4}")
    print()

    print("Per-case sum check (folded aggregate must equal sum of per-case "
          "within over sum of per-case total):")
    for d in PLATEAU_DELTAS:
        sum_within = sum(per_case[k][d]["within"] for k in case_keys)
        sum_total = sum(per_case[k][d]["total"] for k in case_keys)
        folded = sum_within / sum_total if sum_total else 0.0
        observed = runs[d][0]["score"]
        match = abs(folded - observed) < 1e-9
        print(f"  onset_delta={d:.2f}  sum_within={sum_within:>3}  "
              f"sum_total={sum_total:>3}  folded={folded:.4f}  "
              f"observed={observed:.4f}  match: "
              f"{'YES' if match else '*NO*'}")
        if not match:
            hard_failures.append(
                f"per-case sum at onset_delta={d:.2f} folds to {folded:.4f} "
                f"but observed aggregate is {observed:.4f}"
            )
    print()

    print("Decomposition summary (for the Interpreter Agent):")
    print(f"  total cases:            {len(case_keys)}")
    print(f"  flagged cases (within span >= {NOTE_FLIP_FLAG_THRESHOLD}): "
          f"{len(flagged_cases)}")
    if flagged_cases:
        print("  flagged case list:")
        for label, test, span in flagged_cases:
            print(f"    - {label} / {test}  within span = {span}")
    else:
        print("  flagged case list: (none)")
    print()
    print("Hypothesis-mapping note (counts only -- not a perceptual claim):")
    if len(flagged_cases) == 0:
        print("  Zero flagged cases at threshold 1: no per-case within count")
        print("  moved by 1 across the 3 deltas, yet the aggregate scores")
        print("  differ.  This would be impossible if both runs are correct,")
        print("  so a zero-flag outcome triggers the hard-failure check above")
        print("  and should not appear in a passing run.")
    elif len(flagged_cases) <= 2:
        print(f"  {len(flagged_cases)} flagged case(s) -- consistent with H2")
        print("  (sample-specific artefact: the plateau wobble is driven by")
        print("  a small number of specific cases at the tolerance boundary).")
    else:
        print(f"  {len(flagged_cases)} flagged cases -- consistent with H1")
        print("  (real metric property: the wobble reflects movement across")
        print("  many cases, summing to a small aggregate change).")
    print("  This is a count-evidence pointer for Steve / the Interpreter")
    print("  Agent, NOT a perceptual interpretation.  Block 005 forbids any")
    print("  perceptual claim.")
    print()

    if hard_failures:
        print("HARD FAILURES detected -- this run does NOT satisfy block_005:")
        for hf in hard_failures:
            print(f"  - {hf}")
        print()
        print("Per the plan's Stop Conditions, halt and report.")
        return 1

    print("Block 005 produced its evidence cleanly.  Interpretation is the")
    print("Interpreter Agent's responsibility -- this runner only produces")
    print("evidence.  No perceptual claim is made.  No M3.1 re-opening is")
    print("implied (M3.1 remains CLOSED by Steve at 2026-04-25T16:34:20Z).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
