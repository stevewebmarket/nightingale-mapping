# NMB3 Block 001 Report

Block ID:
block_001

Current Milestone:
M3.1 — invariance metric

Block Question:
Does the invariance score change under controlled config mutations?

Commands Run:
- python scripts/fetch_samples.py
- python run_m3_1_metric.py

Files Changed:
- nmb3/nmb3_logs/block_001_raw_output.txt
- nmb3/nmb3_reports/block_001_report.md

Configs Tested:
- baseline
- mutant_a: onset_delta 0.05 -> 0.20
- mutant_b: fmax 16000 -> 4000
- mutant_c: tolerance 1% -> 0.1%

Raw Results:
See nmb3/nmb3_logs/block_001_raw_output.txt

Score Spread:
- Best: baseline and mutant_b = 0.8750
- Worst: mutant_c = 0.4167

Errors Encountered:
- Initial GitHub Actions run did not capture output.
- Logging was fixed to capture stderr/stdout.
- Initial dependency failure: numpy missing.
- Dependencies were added and the workflow then ran successfully.

Retries:
- Workflow rerun after logging fix.
- Workflow rerun after dependency fix.

Stop Condition Triggered:
no

Conclusion:
PASS. The metric is sensitive to controlled configuration changes. At least two mutants moved from baseline:
- mutant_a: 0.8750 -> 0.7917
- mutant_c: 0.8750 -> 0.4167

Risk:
mutant_b did not move from baseline, suggesting fmax may not affect these samples or this part of the pipeline under the current regime.

Funding Relevance:
Positive but early. This supports the claim that M3.1 is measurable and not fully saturated, but does not yet prove deeper structural meaning.

Recommended Next Block:
Block 002 — isolate one parameter family, starting with onset_delta, to determine how strongly it affects the invariance score.
