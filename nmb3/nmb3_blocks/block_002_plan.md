NMB3 Block 002

Block ID:
block_002

Current Milestone:
M3.1 — invariance metric

One Question to Answer:
How does variation in onset_delta affect the invariance score?

Why This Matters:
Block 001 showed the invariance score moves under controlled mutations and is sensitive to onset_delta. This block isolates that single parameter family and sweeps it across a small, well-defined range to characterise the score's response. Establishing how strongly onset_delta drives the score is required before any optimisation or further milestone work.

Allowed Actions:
- vary onset_delta only, across the configs listed below
- run baseline (onset_delta = 0.05) and three mutants (0.10, 0.15, 0.20)
- optionally repeat the baseline run once for stability check
- log all runs and write a single block report

Forbidden Actions:
- no changes to any other parameter family (fmax, tolerance, limit_denominator, pitch / onset modes, etc.)
- no changes to the metric, dataset, sample set, or evaluation logic
- no refactoring of the core pipeline or repo structure
- no scope expansion beyond onset_delta
- no advancing the milestone — stay strictly in M3.1

Required Commands:
- python scripts/fetch_samples.py
- python run_m3_1_metric.py    (once per onset_delta value)

Optional Commands:
- repeat the baseline run once if the first baseline result looks unstable

Configs to Test:
- baseline: onset_delta = 0.05
- onset_delta = 0.10
- onset_delta = 0.15
- onset_delta = 0.20

Maximum Number of Runs:
5 (4 sweep values + at most 1 optional baseline repeat)

Retry Rules:
- retry a failed run once
- if a single config fails twice → log the error and skip that config; do not substitute another value
- do not expand the tested range to compensate for failed runs

Stop Conditions:
- all four onset_delta values successfully tested and logged
- script fails twice on the same config
- outputs invalid or unparseable
- evidence of metric breakdown / unexplainable behavior emerges

Report Path:
nmb3/nmb3_reports/block_002_report.md

Approval Required Before Next Block:
yes
