Block ID:
block_003

Current Milestone:
M3.1 — invariance metric

One Question to Answer:
Is the M3.1 invariance score deterministic under repeated runs of the
baseline default configuration, and if not, what is its run-to-run
variance?

Why This Matters:
Block 002 produced score deltas of 0.0625 to 0.0833 across an
onset_delta sweep. Each delta corresponds to only 3–4 note-level
classification flips out of 48 total notes. Before any further
parameter sweeps, before any monotonicity claim, and before any
extension to the missing onset_delta values (0.01 / 0.03 / 0.25),
we must establish the noise floor of the metric pipeline itself.
If the baseline is bit-identical across repeated runs, the Block 002
deltas can be interpreted as real signal. If the baseline drifts by
amounts comparable to those deltas, the Block 002 conclusions are
uncalibrated and any further sweep work would build on sand. This
block produces the calibration evidence required to interpret all
future M3.1 work.

Allowed Actions:
- Run the M3.1 evaluation pipeline 5 times with no parameter changes
  (run_milestones.DEFAULT_CONFIG verbatim, onset_delta = 0.05)
- Log per-run score, within / total, and full case_results
- Compute mean, stdev, min, max of score across the 5 runs
- Compare per-case results across runs to confirm (or refute)
  bit-identity at the case level
- Document any source of nondeterminism observed

Forbidden Actions:
- Changing any pipeline parameter (onset_delta or otherwise)
- Modifying any core pipeline code in run_milestones.py or
  run_m3_1_metric.py
- Running with any non-default config
- Drawing conclusions about onset_delta sensitivity (that question
  belongs to block_002 and any successor sweep block)
- Extending the onset_delta sweep to 0.01 / 0.03 / 0.25 in this block

Required Commands:
- python scripts/fetch_samples.py
- python run_nmb3_block_003.py

Optional Commands:
(none)

Configs to Test:
- run_milestones.DEFAULT_CONFIG (onset_delta = 0.05), repeated 5 times

Maximum Number of Runs:
5

Retry Rules:
- Retry a single run only if it fails due to infrastructure error
  (network failure during sample fetch, missing audio file, runner
  crash before producing a score)
- Maximum 2 retries per failed run
- Log all retry attempts and reasons to current_block_output.txt

Stop Conditions:
- All 5 runs completed and per-run scores logged
- Pipeline failure that prevents further runs
- More than 2 retries fail for any single run
- Any observed score lies outside the closed interval [0.0, 1.0]
  (would indicate a runner bug; halt and report)

Report Path:
nmb3/nmb3_reports/block_003_report.md

Approval Required Before Next Block:
(yes)
