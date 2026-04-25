Block ID:  
block_002

Current Milestone:  
M3.1 — invariance metric

One Question to Answer:  
How does systematic variation of onset_delta alone affect the invariance metric score?

Why This Matters:  
Demonstrating that the metric is sensitive in a predictable way to changes in onset_delta (a musically-relevant timing parameter) is necessary to establish the realness and interpretation of the metric. This isolates parameter effect, rules out confounds, and provides direct evidence of metric validity.

Allowed Actions:  
- Systematically sweep onset_delta in controlled increments
- Run the invariance metric pipeline for each onset_delta value
- Log all raw and summary outputs
- Create a table and plot: onset_delta vs invariance score
- Document any irregularities or non-monotonicities

Forbidden Actions:  
- Changing any parameter except onset_delta
- Modifying core pipeline code
- Adding unrelated mutants or configs
- Claiming metric generality beyond onset_delta

Required Commands:  
- python scripts/fetch_samples.py  
- python run_m3_1_metric.py --config configs/onset_delta_sweep.yaml

Optional Commands:  
- python scripts/plot_onset_delta_vs_score.py (to generate interpretable graphics)

Configs to Test:  
- onset_delta = [0.01, 0.03, 0.05, 0.10, 0.15, 0.20, 0.25]

Maximum Number of Runs:  
7 (one per onset_delta value)

Retry Rules:  
- Retry failed runs only if failure is due to runtime error, crash, or output corruption
- Maximum 2 retries per failed config
- Log all retry attempts and reasons

Stop Conditions:  
- All onset_delta values tested and outputs logged
- Pipeline failure that blocks further runs
- More than 2 retries fail for the same config

Report Path:  
nmb3/nmb3_reports/block_002_report.md

Approval Required Before Next Block:  
(yes)