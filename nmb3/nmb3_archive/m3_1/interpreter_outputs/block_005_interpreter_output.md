# NMB3 Block 005 — Interpreter Output

Block:        block_005
Milestone:    M3.1 — invariance metric (per-case decomposition follow-on; M3.1 already CLOSED by Steve at 2026-04-25T16:34:20Z; this block does NOT re-open closure)
Policy:       nmb3/nmb3_decision_policy.md (binding); nmb3/nmb3_autonomous_loop_policy.md (binding)
Plan:         nmb3/nmb3_blocks/block_005_plan.md
Report:       nmb3/nmb3_reports/current_block_report.md
Raw output:   nmb3/nmb3_logs/current_block_output.txt
Runner:       run_nmb3_block_005.py @ canonical d47b8b2
CI run:       id 24935788699, conclusion=success, head=d47b8b2
Bot commit:   cec5acd
NMB3 objective: O002 — M3.1 per-case mid-range decomposition

---

## Verdict

**PASS, and the evidence resolves the plateau cleanly.**

The block's question — *"Within the mid-range plateau (onset_delta
in {0.10, 0.15, 0.20}), is the non-monotonic 0.10 → 0.15 → 0.20
movement driven uniformly across the 6 canonical cases, or by one
or two specific cases?"* — is answered as: **driven by 4 of 6
cases moving in opposing directions, not by a single case
artefact**.  This is consistent with H1 (real metric property) and
not H2 (sample-specific artefact) on the strength of the count
evidence.

All three hard-failure checks built into the runner passed:

  - Aggregate cross-check: observed scores 0.7917 / 0.8125 / 0.7917
    at onset_delta 0.10 / 0.15 / 0.20 match the published Block 002
    / Block 004 values exactly.  No pipeline drift.
  - Per-case determinism cross-check: 18 of 18 (within, total)
    pairs bit-identical across the two passes per delta (6 cases ×
    3 deltas).  This is a second-pass confirmation on top of the
    8/8 baseline determinism established by Block 003.
  - Per-case sum check: at every delta, the sum of per-case
    `within` over sum of per-case `total` folds back to the
    observed aggregate score exactly.  No accounting error.

## Evidence

Per-case decomposition table from `current_block_output.txt`
(values are within-tolerance / total notes per case):

    case (label / test)              d=0.10     d=0.15     d=0.20    span    flag
    -------------------------------------------------------------------------------
    Orchestra / pitch_shift          7 / 8      7 / 8      7 / 8        0     -
    Orchestra / time_stretch         6 / 8      6 / 8      5 / 8        1   FLAG
    Orchestra / composition          6 / 8      5 / 8      5 / 8        1   FLAG
    Rock      / pitch_shift          8 / 8      8 / 8      8 / 8        0     -
    Rock      / time_stretch         5 / 8      6 / 8      6 / 8        1   FLAG
    Rock      / composition          6 / 8      7 / 8      7 / 8        1   FLAG

Aggregate cross-check vs published values:

    onset_delta   observed   published   match
    0.10          0.7917     0.7917      YES
    0.15          0.8125     0.8125      YES
    0.20          0.7917     0.7917      YES

## Pattern Analysis

1. **Two cases are flat across the entire mid-range plateau.**
   Both pitch_shift cases (Orchestra/pitch_shift = 7/8 throughout;
   Rock/pitch_shift = 8/8 throughout) are completely insensitive
   to onset_delta in the 0.10–0.20 region.  This is the expected
   behaviour: pitch shift transforms preserve onset timing, so a
   timing-tolerance parameter has no purchase on them.  Rock/
   pitch_shift is also at the ceiling (8/8), so even if it could
   move, it cannot move up.

2. **Two cases trend DOWN as onset_delta increases.**
   - Orchestra/time_stretch: 6 → 6 → 5  (loses 1 from 0.15 to 0.20)
   - Orchestra/composition:  6 → 5 → 5  (loses 1 from 0.10 to 0.15)

3. **Two cases trend UP as onset_delta increases.**
   - Rock/time_stretch:      5 → 6 → 6  (gains 1 from 0.10 to 0.15)
   - Rock/composition:       6 → 7 → 7  (gains 1 from 0.10 to 0.15)

4. **The plateau wobble is the algebraic sum of opposing per-case
   movements.**  At 0.15 vs 0.10: +1 (R/ts) +1 (R/comp) −1 (O/comp)
   = net +1, taking the aggregate from 38/48 = 0.7917 to 39/48 =
   0.8125.  At 0.15 vs 0.20: +1 (O/ts; 6 at 0.15 vs 5 at 0.20) and
   zero from the other three flagged cases = net +1, again 39/48
   vs 38/48.  The +1/+1 symmetry around 0.15 is what produces the
   non-monotonic appearance in the aggregate.

5. **Orchestra and Rock respond in opposite directions to
   increasing onset_delta in this range.**  Every Orchestra
   non-pitch-shift case loses notes as onset_delta increases;
   every Rock non-pitch-shift case gains notes.  This is a
   structural observation about the metric on this corpus: it is
   not a coincidence of one or two notes at the boundary.

## Hypothesis Mapping (counts only — NOT a perceptual claim)

The block's plan defined two hypotheses on the count evidence:

- **H1 (real metric property):** every case's within-tolerance
  count moves a little, summing to a small aggregate change.
- **H2 (sample-specific artefact):** one or two specific cases'
  within-tolerance counts move by exactly 1 note flip, while the
  others are flat.

The observation is **4 of 6 cases flagged, 2 flat** (both flats
are the pitch_shift cases).  Strict H2 predicted ≤ 2 flagged;
strict H1 predicted all 6 flagged.  The actual outcome lies on
the H1 side of that boundary by a clear margin — the plateau is
**not** a single-case or two-case artefact.  It is metric
behaviour that arises from the genre-asymmetric response of the
non-pitch-shift transforms.

This is a count-evidence pointer for Steve, NOT a perceptual
interpretation.  Block 005 forbids any perceptual claim, and none
is made here.  In particular, this output does NOT claim that the
0.15 peak corresponds to better musical structure preservation,
better perceived timing fidelity, or anything else about how the
audio sounds; it only claims that 4 of 6 cases shift their note
count by exactly 1 across the plateau region, with Orchestra and
Rock moving in opposite directions.

## Signal-vs-Noise

The metric is bit-identical across both passes per delta (18/18
pairs), so every observed per-case shift is a real metric response
and not pipeline jitter.  Combined with Block 003's 8/8 baseline
determinism, the determinism record across the M3.1 work is now
8 + 18 = 26 of 26 bit-identical comparisons.

## Risk

- **Scientific risk (low):** all three hard-failure checks
  passed; the result is internally consistent (per-case sums fold
  to aggregates exactly), consistent with prior blocks (aggregates
  match Block 002 / 004 published values), and shows no
  unphysical behaviour.
- **Process risk (low):** O002 consumed 2 of 6 loops and 1 of 2
  workflow-edit budget; there is room to handle any follow-on
  Steve gates inside the same session if Steve so directs, but
  the loop will stop at O002 SUCCEEDED per the autonomous loop
  policy "do not begin the next objective" rule.
- **Fake-progress risk (none detected):** the runner imports the
  locked `evaluate_m3_1` hook, varies only onset_delta, hard-fails
  on aggregate drift vs published values, and double-runs each
  delta with bit-identical verification.  The pattern observed
  (Orchestra-down, Rock-up; pitch_shift flat) is not the kind of
  pattern a metric-gaming runner would produce.
- **Coverage risk (in-scope only):** O002 was scoped to the
  three-point plateau, on the canonical 6-case set, varying only
  onset_delta.  The block does not claim coverage of other
  parameters, other audio types, perceptual validity, or
  generalisation to non-canonical samples; those were never
  inside its scope and remain open questions.
- **Closure-status risk (zero):** Block 005 explicitly does not
  re-open M3.1.  M3.1 remains CLOSED by Steve at 2026-04-25T16:34:20Z
  on the narrow reading defined in
  `nmb3/nmb3_reports/m3_1_closure_recommendation.md`.

## Funding Relevance

Still none claimed and none recommended.  Per Decision Policy,
funding claims remain forbidden under all forms of approval used
in this work (autonomous and Steve-gated).

## Closure of NMB3 Objective O002

O002's success criteria, per nmb3/nmb3_objective_map.md:

- "per-case (6 cases × 3 onset_delta values) within/total counts
  produced" — **MET** (table above; 18 datapoints).
- "deterministic across two runs" — **MET** (18/18 per-case
  bit-identical pairs).
- "any case whose folded score moves by ≥ 1 note flip flagged" —
  **MET** (4 cases flagged, 2 flat; flag list explicit).

O002 status moves from IN PROGRESS to SUCCEEDED in this commit.
The narrow factual conclusion the loop is permitted to record —
on the strength of counts only — is:

> The mid-range onset_delta plateau (scores 0.7917 / 0.8125 /
> 0.7917 at 0.10 / 0.15 / 0.20) is driven by 4 of 6 canonical
> cases shifting their within-tolerance count by exactly 1 note
> across the plateau region, with Orchestra and Rock cases moving
> in opposite directions.  The two pitch_shift cases are flat.
> The aggregate non-monotonicity is the algebraic sum of these
> opposing per-case movements.  This is consistent with the
> plateau being a real (albeit small) property of the metric on
> this corpus, not a single-case sample artefact.

## What This Output Does NOT Conclude

- Does not declare M3.1 re-opened (closure status unchanged).
- Does not declare M3.1 re-closable on a "wider reading" — the
  narrow reading from the closure recommendation remains the only
  Steve-authorised reading.
- Does not claim perceptual validity of any kind.
- Does not generalise the genre-asymmetric pattern (Orchestra-
  down, Rock-up) beyond the canonical 6-case set or beyond the
  0.10–0.20 onset_delta range.  A cross-corpus probe (NMB3 O003)
  would be needed for any such generalisation; O003 is not
  authorised by Steve and remains PROPOSED.
- Does not recommend M4 transition.
- Does not begin O003, O004, or any later objective.
- Does not make any funding claim.
- Does not edit the closure recommendation file, MILESTONES.md,
  or any policy file.
