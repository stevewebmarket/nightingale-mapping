Block ID:
block_004

Current Milestone:
M3.1 — invariance metric

Approval Status:
AUTONOMOUSLY APPROVED under nmb3/nmb3_decision_policy.md as the
final M3.1 closure block, authorised by Steve in the conversation
turn that opened this session.  Per the autonomous-approval audit
in nmb3/nmb3_reports/block_003_interpreter_output.md the block
satisfies all 7 criteria (inside M3.1, single question, reduces
uncertainty, no direction change, no funding claim, no core
architecture change, validation/measurement-integrity block) and
triggers no pause condition.

One Question to Answer:
Does the M3.1 invariance score continue to track onset_delta in the
unmeasured boundary regions {0.01, 0.03, 0.25}, and is the resulting
combined sweep consistent with the partial Block 002 evidence and the
zero noise floor established by Block 003?

Why This Matters:
Block 002 executed only 4 of the 7 onset_delta values listed in its
canonical plan.  The unmeasured values are precisely the boundary
regions: very-tight (0.01, 0.03) and very-loose (0.25).  These are
where saturation or breakdown of the metric would most likely
appear, so they are exactly the values that must be present before
M3.1 can honestly be called closed.  This block fills that gap and
nothing more -- it does not extend scope, does not vary any other
parameter, and does not propose any milestone transition.

Allowed Actions:
- Run the M3.1 invariance metric for onset_delta in {0.01, 0.03, 0.25}
- Use run_milestones.DEFAULT_CONFIG for every other field
- Log per-run score, within / total, and delta vs baseline (0.05)
- Combine the new values with the existing Block 002 values
  (0.05, 0.10, 0.15, 0.20) in a single ordered table
- Compare every observed delta against the Block 003 noise floor
  (population stdev = 0.0000)
- Document any irregularity, saturation, or breakdown observed at
  the boundary values

Forbidden Actions:
- Changing any pipeline parameter except onset_delta
- Modifying any core pipeline code
- Running any onset_delta value not in {0.01, 0.03, 0.25}
  (the four already-measured values are referenced from Block 002,
  not re-run)
- Re-running the Block 003 baseline (it is already deterministic;
  re-running it would only consume budget)
- Declaring M3.1 closed (closure is a Steve decision)
- Beginning any M4 work
- Making any funding claim
- Editing nmb3_decision_policy.md or nmb3_autonomous_loop_policy.md

Required Commands:
- python scripts/fetch_samples.py
- python run_nmb3_block_004.py

Optional Commands:
(none)

Configs to Test:
- onset_delta = 0.01  (all other fields DEFAULT_CONFIG)
- onset_delta = 0.03  (all other fields DEFAULT_CONFIG)
- onset_delta = 0.25  (all other fields DEFAULT_CONFIG)

Maximum Number of Runs:
3

Retry Rules:
- Retry a single run only if it fails due to infrastructure error
  (network failure during sample fetch, missing audio file, runner
  crash before producing a score)
- Maximum 2 retries per failed run
- Log all retry attempts and reasons to current_block_output.txt

Stop Conditions:
- All 3 onset_delta values evaluated and per-run scores logged
- Pipeline failure that prevents further runs
- More than 2 retries fail for any single run
- Any observed score lies outside the closed interval [0.0, 1.0]
  (would indicate a runner bug; halt and report)

Report Path:
nmb3/nmb3_reports/block_004_report.md

Approval Required Before Next Block:
(yes — block_005 / any successor block is NOT pre-approved.  The
only authorised next step after block_004 is the M3.1 closure
recommendation written to nmb3/nmb3_reports/m3_1_closure_recommendation.md
for Steve's review.)
