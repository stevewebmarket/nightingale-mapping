# NMB3 Block 003 — Interpreter Output

Block:        block_003
Milestone:    M3.1 — invariance metric
Policy:       nmb3/nmb3_decision_policy.md (binding)
Plan:         nmb3/nmb3_blocks/block_003_plan.md
Report:       nmb3/nmb3_reports/current_block_report.md
Raw output:   nmb3/nmb3_logs/current_block_output.txt
Runner:       run_nmb3_block_003.py @ canonical ce6eca9
CI run:       id 24934283280, conclusion=success, head=ce6eca9
Bot commit:   488a889

---

## Verdict

**PASS.**

The block's question — *"Are baseline M3.1 scores stable enough that
Block 002 score deltas can be interpreted as real parameter
sensitivity?"* — is answered cleanly and unambiguously by the
evidence. The M3.1 metric pipeline is fully deterministic under
repeated invocation with identical inputs. The noise floor of the
pipeline itself is zero, and the Block 002 deltas (0.0625 and 0.0833)
are therefore real responses to onset_delta, not pipeline jitter.

## Evidence

Eight repeated runs of run_milestones.DEFAULT_CONFIG (onset_delta =
0.05, all other fields unchanged):

    run     score    within / total
    -----------------------------------
       1   0.8750    42 / 48
       2   0.8750    42 / 48
       3   0.8750    42 / 48
       4   0.8750    42 / 48
       5   0.8750    42 / 48
       6   0.8750    42 / 48
       7   0.8750    42 / 48
       8   0.8750    42 / 48

    mean   = 0.8750
    stdev  = 0.0000   (population stdev across 8 runs)
    min    = 0.8750
    max    = 0.8750
    span   = 0.0000

Per-case bit-identity check (covers all 6 cases × per-case
within/total/raw_score/folded_score signature): 1 distinct signature
across 8 runs. **bit-identical = True.**

Independent reproduction: identical numbers from a local smoke test
in /tmp/vchk and from a clean ubuntu-latest GitHub Actions runner.
This is not a "lucky local run" — it reproduces in a fresh
environment with freshly downloaded samples.

## Signal-vs-Noise Comparison Against Block 002

Per the Decision Policy *Score Resolution Rule* (one note flip =
1/48 = 0.0208):

| block_002 delta | note flips | baseline stdev | clearly above baseline jitter? |
|-----------------|-----------:|---------------:|--------------------------------|
| 0.0625          | 3          | 0.0000         | yes (delta / stdev = ∞)        |
| 0.0833          | 4          | 0.0000         | yes (delta / stdev = ∞)        |

The Decision Policy classified the 0.06–0.08 band as "require
baseline stability testing" before being treated as meaningful.
Baseline stability has now been tested. The deltas pass.

## Risk

- **Scientific risk (very low):** result is unambiguous; pipeline is
  deterministic; bit-identity holds at the per-case level not just
  the score level.
- **Process risk (low):** the four-vs-seven coverage gap in Block 002
  remains an open question (Steve decision, flagged in the prior
  interpreter output). It is *not* a blocker for the M3.1-stable /
  M3.1-responsive judgement, but it limits the strength of any
  generalisation claim about onset_delta.
- **Fake-progress risk (none detected):** the runner imports the
  locked `evaluate_m3_1` hook, varies nothing, and is a faithful
  N-fold repetition. No metric gaming surface exists in this design.
- **Autonomy risk (none observed):** the session stayed inside M3.1,
  used 1 of its 2 workflow-edit budget, completed in 3 of 6 loops,
  and produced exactly the artifacts mandated by the autonomous loop
  policy. No scope drift.

## Funding Relevance

Still none claimed. The Decision Policy unblocking sequence —
"(1) metric sensitivity is shown, (2) baseline stability/noise floor
is measured, (3) score changes are larger than baseline jitter" — is
now satisfied for the *technical* prerequisites. Steps from here to
fundable evidence are policy-level decisions (M3.1 closure, M3.1 →
M4 transition) that require Steve.

## Recommended Next Steps (NOT executed by this Interpreter)

The Interpreter Agent rules forbid self-approval. The following are
recommendations only, surfaced for Steve.

1. **M3.1 closure decision (Steve).** The two-prong M3.1 validation
   question — *is the metric stable AND meaningful?* — is now
   answered yes / yes. Steve should decide whether M3.1 is closed,
   or whether closure is conditional on first resolving the
   block_002 coverage gap (extend the onset_delta sweep to the
   missing values 0.01 / 0.03 / 0.25).

2. **Milestone transition (Steve only, per policy).** If M3.1 is
   closed, M3.1 → M4 is forbidden under autonomous approval and
   requires explicit Steve sign-off.

3. **Optional deepening within M3.1 (Steve).** If Steve wishes to
   strengthen the "meaningful" half of the verdict beyond
   "responsive to a known timing parameter", the next bounded block
   could probe whether score corresponds to perceived structural
   preservation — but framing that block carefully enough to satisfy
   the Decision Policy's "validation / stability / measurement-
   integrity" autonomous-approval criterion #7 is itself a Steve
   judgement call (pause condition #6: subjective judgement not
   covered by policy).
