# NMB3 Block 004 — Interpreter Output

Block:        block_004
Milestone:    M3.1 — invariance metric (closure block)
Policy:       nmb3/nmb3_decision_policy.md (binding)
Plan:         nmb3/nmb3_blocks/block_004_plan.md
Report:       nmb3/nmb3_reports/current_block_report.md
Raw output:   nmb3/nmb3_logs/current_block_output.txt
Runner:       run_nmb3_block_004.py @ canonical 8abed1a
CI run:       id 24934520765, conclusion=success, head=8abed1a
Bot commit:   c0a1b8c

---

## Verdict

**PASS.**

The block's question — *"Does the M3.1 invariance score continue to
track onset_delta in the unmeasured boundary regions {0.01, 0.03,
0.25}, and is the resulting combined sweep consistent with Block 002
and Block 003?"* — is answered cleanly. The three new boundary
values produced finite, in-`[0,1]` scores, the boundary at 0.25
shows a clear and interpretable breakdown of timing tolerance, and
the unified 7-point sweep is internally consistent and consistent
with the prior partial Block 002 evidence and the zero noise floor
established by Block 003.

Independent reproduction: local smoke test in /tmp/vchk and clean
ubuntu-latest GitHub Actions runner produced bit-identical numbers.
This was expected (Block 003 already proved determinism); reporting
it here only to record that the determinism property continues to
hold under a new parameter sweep.

## Evidence

Unified 7-point onset_delta sweep, sorted by onset_delta:

    onset_delta   score    delta vs 0.05   note flips   source
    -----------------------------------------------------------
       0.01      0.8542    -0.0208         -1.0         block_004
       0.03      0.8958    +0.0208         +1.0         block_004  *peak*
       0.05      0.8750    baseline           -         block_002
       0.10      0.7917    -0.0833         -4.0         block_002
       0.15      0.8125    -0.0625         -3.0         block_002
       0.20      0.7917    -0.0833         -4.0         block_002
       0.25      0.7292    -0.1458         -7.0         block_004  *trough*

Sweep range: [0.7292, 0.8958].  Sweep span: 0.1667 = 8 note flips
out of 48.  No score saturated at 0.0 or 1.0.  All scores are in
the closed unit interval.

## Pattern Analysis

1. **Clear boundary breakdown at the loose end (0.25 → 0.7292,
   −7 flips).** This is the worst score in the sweep and is
   monotonically lower than every value to its left in the
   onset_delta-ascending ordering.  Interpretation: a timing
   tolerance that is too loose lets in too many spurious matches
   and the invariance score falls accordingly.  This is the
   behaviour a well-formed timing-tolerance parameter *should*
   produce, and its absence in Block 002 was a real coverage gap.

2. **Mild degradation at the tight end (0.01 → 0.8542, −1 flip).**
   A timing tolerance close to zero loses one note that the
   baseline tolerated.  Mild and interpretable; not a collapse.

3. **Small peak at 0.03 (+1 flip vs baseline).** One note flip is
   the metric's resolution unit (1/48 = 0.0208).  The peak is
   real (infinitely many baseline-stdevs above zero noise floor)
   but small enough that no architectural conclusion should be
   drawn from a single-flip improvement; it is consistent with
   the metric having a mild optimum somewhere between 0.01 and
   0.05 on this sample set.

4. **Mid-range plateau (0.10–0.20 in the −3 to −4 flip band) is
   non-monotonic** (0.10 = 0.7917, 0.15 = 0.8125, 0.20 = 0.7917).
   This was already visible in Block 002.  The 7-point view does
   not resolve that non-monotonicity — it neither explains it nor
   makes it worse.

5. **Overall trend** across the seven points is "score is highest
   in a narrow band around 0.03–0.05 and degrades on both sides,
   with a much steeper drop on the loose side than the tight
   side."  This is the pattern one expects from a real timing-
   tolerance parameter on a real metric.

## Signal-vs-Noise

Block 003 established a population stdev of 0.0000 across 8
bit-identical baseline runs.  Every nonzero delta in the 7-point
table is therefore infinitely many baseline-stdevs above the
noise floor.  No deltas can be attributed to pipeline jitter.

## Risk

- **Scientific risk (low):** the result is internally consistent,
  consistent with prior blocks, and shows no unphysical behaviour
  (no saturation, no out-of-range scores, no NaN, no exception).
- **Process risk (low):** the closure block consumed 1 of 6 loops
  available in this session and 2 of 2 workflow edits (the second
  workflow edit is the block_003 → block_004 swap landed in
  commit 8abed1a).  The session is on track to terminate cleanly
  after the closure recommendation is written.
- **Fake-progress risk (none detected):** the runner imports the
  locked `evaluate_m3_1` hook, varies only onset_delta, and
  references Block 002 values as constants rather than inventing
  fresh numbers.  No surface for metric gaming exists.
- **Coverage risk (now closed for the original plan):** the seven
  onset_delta values originally planned for Block 002 are all
  measured.  The block does NOT close other coverage questions
  (other parameters, other audio types, perceptual validity);
  those were never inside its scope.

## Funding Relevance

Still none claimed and none recommended.  Per Decision Policy,
funding claims remain forbidden under autonomous approval.

## Recommendation Surfaced (NOT a milestone change)

This Interpreter Agent output recommends to Steve, in the
companion file `nmb3/nmb3_reports/m3_1_closure_recommendation.md`,
that M3.1 be considered closable on the strength of Blocks 001
through 004.  That recommendation is for Steve's decision; it is
not a milestone change.
