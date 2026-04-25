Block ID:
block_005

Current Milestone:
M3.1 — invariance metric (per-case decomposition follow-on; M3.1
already CLOSED by Steve at 2026-04-25T16:34:20Z on the narrow
reading; this block resolves the mid-range plateau pattern within
the already-closed milestone and does NOT re-open closure).

Approval Status:
STEVE-APPROVED via nmb3/nmb3_decisions.log entry at
2026-04-25T16:34:20Z (Option 2 of the M3.1 closure recommendation
in nmb3/nmb3_reports/m3_1_closure_recommendation.md, with O002
named explicitly), with execution authorised by Steve's
"Execute O002" string at 2026-04-25T16:46:06Z (recorded in the
same log).  This is a Steve-approved block, not an autonomously-
approved one; the loop is executing inside the bounded shape of
NMB3 objective O002.

One Question to Answer:
Within the mid-range plateau (onset_delta in {0.10, 0.15, 0.20},
aggregate scores 0.7917 / 0.8125 / 0.7917 from Block 002 + Block
004), is the non-monotonic 0.10 -> 0.15 -> 0.20 movement driven
uniformly across the 6 canonical cases, or by one or two specific
cases whose within-tolerance counts shift?

Why This Matters:
The +1 / -1 wobble at 0.15 (relative to 0.10 and 0.20) is the
only un-explained feature of the 7-point M3.1 sweep.  Two
hypotheses are consistent with the aggregate evidence so far:

  H1 (real metric property): every case's within-tolerance count
      moves a little, summing to a small aggregate change.  Under
      H1, the plateau is a property of the metric on this corpus
      and would be expected to recur on similar corpora.

  H2 (sample-specific artefact): one or two specific cases'
      within-tolerance counts move by exactly 1 note flip, while
      the others are flat.  Under H2, the plateau is a coincidence
      of which specific notes are at the tolerance boundary in
      those particular cases, not a metric property.

This block does not declare which hypothesis is correct as a
matter of perception or musical structure -- it produces the
per-case decomposition that lets Steve choose between H1 and H2
on the strength of the count evidence, and nothing more.

Allowed Actions:
- Run the M3.1 invariance metric for onset_delta in
  {0.10, 0.15, 0.20}, twice each (6 runs total)
- Use run_milestones.DEFAULT_CONFIG for every other field
- For each run, log per-case (label, test, within_tolerance,
  total_notes) for all 6 cases
- Verify per-case bit-identical (within, total) across the two
  runs at each delta (a 6 x 3 second-pass determinism check on
  top of the 8/8 baseline determinism established by Block 003)
- Compute per-case "within count span" across the 3 deltas
  (max within - min within), and flag any case whose span >= 1
- Cross-check that the aggregate score at each of the 3 deltas
  matches the Block 002 / Block 004 published values
  (0.7917, 0.8125, 0.7917 at 0.10 / 0.15 / 0.20 respectively);
  any mismatch is a pipeline-drift signal and is reported as
  a hard failure
- Print a single per-case table that the Interpreter Agent can
  read directly to decide between H1 and H2

Forbidden Actions:
- Changing any pipeline parameter except onset_delta
- Modifying any core pipeline code
- Running any onset_delta value not in {0.10, 0.15, 0.20}
  (the four values outside the plateau region are referenced
  from Blocks 002 and 004, not re-run)
- Declaring perceptual interpretation of the plateau (H1 vs H2 is
  a claim about counts, not about perception)
- Re-opening M3.1 closure (already CLOSED by Steve)
- Recommending M4 transition
- Beginning any M4 work
- Making any funding claim
- Editing nmb3_decision_policy.md or nmb3_autonomous_loop_policy.md
- Editing MILESTONES.md
- Editing nmb3/nmb3_reports/m3_1_closure_recommendation.md

Required Commands:
- python scripts/fetch_samples.py
- python run_nmb3_block_005.py

Optional Commands:
(none)

Configs to Test:
- onset_delta = 0.10  (run 1 and run 2; all other fields DEFAULT_CONFIG)
- onset_delta = 0.15  (run 1 and run 2; all other fields DEFAULT_CONFIG)
- onset_delta = 0.20  (run 1 and run 2; all other fields DEFAULT_CONFIG)

Maximum Number of Runs:
6

Retry Rules:
- Retry a single run only if it fails due to infrastructure error
  (network failure during sample fetch, missing audio file, runner
  crash before producing a score)
- Maximum 2 retries per failed run
- Log all retry attempts and reasons to current_block_output.txt

Stop Conditions:
- All 3 onset_delta values evaluated twice and per-case results
  logged
- Pipeline failure that prevents further runs
- More than 2 retries fail for any single run
- Any case shows non-bit-identical (within, total) across its
  two runs at any delta (determinism regression -- halt and
  report)
- Any aggregate score at the 3 deltas differs from the published
  Block 002 / Block 004 value at the same delta (pipeline drift --
  halt and report)
- Any observed score lies outside the closed interval [0.0, 1.0]

Report Path:
nmb3/nmb3_reports/block_005_report.md

Approval Required Before Next Block:
(yes -- block_006 / any successor block is NOT pre-approved.  After
block_005 the only autonomous action permitted is the Interpreter
Agent output written to
nmb3/nmb3_reports/block_005_interpreter_output.md, which closes
NMB3 objective O002.  Any further block requires a separate Steve
authorisation string.)
