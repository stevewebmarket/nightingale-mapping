Block ID:
block_003

Current Milestone:
M3.1 — invariance metric

Approval Status:
AUTONOMOUSLY APPROVED under nmb3/nmb3_decision_policy.md
(Autonomous Approval Rules — all 7 criteria satisfied; no pause
condition triggered. See nmb3/nmb3_reports/block_002_interpreter_output.md
for the policy-check audit table.)

One Question to Answer:
Are baseline M3.1 scores stable enough that Block 002 score deltas
can be interpreted as real parameter sensitivity?

Why This Matters:
Block 002 observed score deltas of approximately 0.0625–0.0833,
equal to roughly 3–4 note flips out of 48. Per the Decision Policy
(Score Resolution Rule and Measurement Integrity Rules), deltas in
this band must be compared against repeated baseline variance
before being treated as meaningful. Without this calibration, no
further sweep, optimization, M4 demo, or funding claim is permitted.
This block produces the noise-floor evidence required to interpret
all subsequent M3.1 work.

Allowed Actions:
- Run the M3.1 evaluation pipeline 8 times with no parameter changes
  (run_milestones.DEFAULT_CONFIG verbatim, onset_delta = 0.05)
- Log per-run score, within / total, and full case_results
- Compute mean, stdev, min, max of score across the 8 runs
- Compare per-case results across runs to confirm (or refute)
  bit-identity at the case level
- Document any source of nondeterminism observed
- Compare baseline variance against Block 002 deltas (0.0625, 0.0833)
  and state whether those deltas exceed baseline jitter

Forbidden Actions:
- Changing any pipeline parameter (onset_delta or otherwise)
- Modifying any core pipeline code in run_milestones.py or
  run_m3_1_metric.py
- Running with any non-default config
- Drawing conclusions about onset_delta sensitivity beyond the
  signal-vs-noise comparison defined above
- Extending the onset_delta sweep to 0.01 / 0.03 / 0.25 in this block
- Beginning any optimization work
- Making any funding claim
- Proposing any milestone transition

Required Commands:
- python scripts/fetch_samples.py
- python run_nmb3_block_003.py

Optional Commands:
(none)

Configs to Test:
- run_milestones.DEFAULT_CONFIG (onset_delta = 0.05), repeated 8 times

Maximum Number of Runs:
8

Retry Rules:
- Retry a single run only if it fails due to infrastructure error
  (network failure during sample fetch, missing audio file, runner
  crash before producing a score)
- Maximum 2 retries per failed run
- Log all retry attempts and reasons to current_block_output.txt

Stop Conditions:
- All 8 runs completed and per-run scores logged
- Pipeline failure that prevents further runs
- More than 2 retries fail for any single run
- Any observed score lies outside the closed interval [0.0, 1.0]
  (would indicate a runner bug; halt and report)

Report Path:
nmb3/nmb3_reports/block_003_report.md

Approval Required Before Next Block:
(yes — block_004 is NOT autonomously approved by this plan; the
Interpreter must re-evaluate under nmb3_decision_policy.md once
block_003 evidence exists.)
