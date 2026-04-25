# M3.1 Closure Recommendation

Audience:    Steve.
Author:      NMB3 Interpreter Agent, end of the autonomously-approved
             M3.1 closure session.
Policy:      nmb3/nmb3_decision_policy.md, nmb3/nmb3_autonomous_loop_policy.md
             (both binding).
Status:      RECOMMENDATION ONLY.  No milestone change, no M4, no
             funding claim is made or implied.

---

## TL;DR

**M3.1 may honestly be closed on the evidence of Blocks 001–004.**

The decision is yours.  This file gives you the evidence that
remains in scope, the limits on what closure would mean, and the
explicit list of things that closure would NOT authorise.

## What "M3.1 Closed" Would Mean (Narrow Reading, Recommended)

Closing M3.1 on this evidence authorises exactly the following
claims and nothing more:

1. The M3.1 invariance metric (`evaluate_m3_1` over the canonical
   6-case sample set) is **implemented and runs end-to-end** in
   the canonical pipeline on a clean CI runner.
2. The metric is **deterministic** under repeated invocation with
   identical inputs (Block 003: 8 of 8 bit-identical runs,
   population stdev = 0.0000).
3. The metric is **responsive to a primary timing parameter
   (onset_delta)** across the full 7-point grid originally
   planned for Block 002 (Blocks 002 and 004 combined).  Every
   nonzero delta is infinitely many baseline-stdevs above the
   measured noise floor of zero.
4. The 7-point onset_delta response is **internally consistent
   and free of unphysical behaviour**: no saturation at 0 or 1,
   no out-of-range scores, no NaN, no exception, an interpretable
   breakdown at the loose boundary (0.25 → 0.7292, −7 note flips)
   and only mild degradation at the tight boundary (0.01 →
   0.8542, −1 note flip).

## What "M3.1 Closed" Would NOT Authorise

Closure on this evidence does NOT authorise any of the following:

- Beginning M4 work in any form.  (Decision Policy: M3.1 → M4
  transition is Forbidden Without Steve Approval; it is a
  separate decision from M3.1 closure.)
- Any funding claim, including soft framings such as "metric
  validated" or "milestone achieved" in funder-facing material.
- The claim that the score corresponds to **perceived musical
  structure preservation**.  Blocks 001–004 establish responsiveness
  to a *measured timing parameter*, not perceptual validity.
- Generalisation beyond the canonical 6-case sample set.
- Generalisation to parameters other than onset_delta.
- Any change to `nmb3_decision_policy.md` or
  `nmb3_autonomous_loop_policy.md`.

If closure is granted, please reply with a single line stating
which of these you also do or do not authorise, so the autonomous
loop has unambiguous bounds for the next session.

## Evidence Snapshot

Canonical commit chain for the M3.1 evidence base:

    bfcfc50  Block 002 onset_delta sweep (4 / 7 originally planned)
    488a889  Block 003 baseline stability (8 bit-identical runs)
    c0a1b8c  Block 004 onset_delta closure (3 missing boundary values)

Unified 7-point onset_delta sweep, sorted ascending:

    onset_delta   score    delta vs 0.05   note flips   source
    -----------------------------------------------------------
       0.01      0.8542    -0.0208         -1.0         block_004
       0.03      0.8958    +0.0208         +1.0         block_004
       0.05      0.8750    baseline           -         block_002
       0.10      0.7917    -0.0833         -4.0         block_002
       0.15      0.8125    -0.0625         -3.0         block_002
       0.20      0.7917    -0.0833         -4.0         block_002
       0.25      0.7292    -0.1458         -7.0         block_004

Block 003 noise floor: population stdev = 0.0000 over 8 bit-
identical runs.  Sweep span 0.1667 = 8 note flips out of 48.

## Open Questions That Closure Does Not Resolve

These are not objections to closure -- they are honest pointers
for whatever block you authorise next:

1. **Mid-range non-monotonicity.** Scores at 0.10, 0.15, 0.20 sit
   in the −3 to −4 flip band but are not monotone (0.7917,
   0.8125, 0.7917).  Real or sample-specific?  Would need either
   per-case decomposition or an additional sample set to answer.
2. **Perceptual correspondence.** Whether the score tracks human
   judgements of structural preservation is untested and is the
   strongest single thing that could either ratify or undermine
   the metric's broader meaning.
3. **Other parameters.** Sensitivity to anything other than
   onset_delta is untested.
4. **Cross-corpus generalisation.** Behaviour on samples outside
   the canonical 6-case set is unknown.

## Decision Required From Steve

Please reply with one of:

- "Close M3.1, narrow reading as above.  Do nothing else."
- "Close M3.1, narrow reading as above.  Authorise <specific next
   block>."  (Examples: per-case decomposition of the mid-range
   plateau; a perceptual-validity probe; a second-corpus run.)
- "Do not close M3.1 yet -- I want <specific additional evidence>
   first."
- "Close M3.1 and authorise the M3.1 → M4 transition."  (Note:
  this is two decisions in one; the autonomous loop will treat
  them as such.)

The autonomous loop will not begin any of the above without your
explicit instruction.  Per policy: *"The system must not fill
time by inventing work."*

## Stop

Session terminates here.  No further loop is initiated by the
autonomous system.  No milestone change has been made.  No M4
work has begun.  No funding claim has been recorded.  No policy
file has been edited.

Canonical state at end of session:

    23e18a9  M3.1 autonomous validation session report (prior session)
    8abed1a  Block 004 plan + runner + workflow rewire (this session)
    c0a1b8c  Block 004 bot results (this session)
    (this commit)  Block 004 interpreter output + M3.1 closure recommendation
