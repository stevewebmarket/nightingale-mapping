NMB3 Block 001

Block ID:
block_001

Current Milestone:
M3.1 — invariance metric

One Question to Answer:
Does the invariance score change under controlled config mutations?

Why This Matters:
If the score does not change, the metric is not usable for optimization or evaluation.

Allowed Actions:
- run baseline config
- run up to 3 mutated configs
- repeat baseline once if needed
- log results

Forbidden Actions:
- no optimization
- no new features
- no dataset expansion
- no large refactoring
- no changing evaluation logic

Required Commands:
- python scripts/fetch_samples.py
- python run_m3_1_metric.py

Optional Commands:
- repeat baseline run if results look unstable

Configs to Test:
- baseline
- mutant A (slightly lower onset_delta)
- mutant B (higher fmax)
- mutant C (lower limit_denominator)

Maximum Number of Runs:
6–8

Retry Rules:
- retry failed run once
- if fails twice → log error and skip

Stop Conditions:
- all configs return identical score
- script fails twice
- outputs invalid

Report Path:
nmb3_reports/block_001_report.md

Approval Required Before Next Block:
yes
