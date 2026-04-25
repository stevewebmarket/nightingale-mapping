# NMB3 Block 002 — Interpreter Output (Policy-Bound Rerun)

Block:        block_002
Milestone:    M3.1 — invariance metric
Policy:       nmb3/nmb3_decision_policy.md (binding)
Plan:         nmb3/nmb3_blocks/block_002_plan.md
Report:       nmb3/nmb3_reports/current_block_report.md
Raw output:   nmb3/nmb3_logs/current_block_output.txt
Runner:       run_nmb3_block_002.py @ canonical bfcfc50

Note: this file supersedes the prior interpreter judgement at git
commit 439e312 (which was made before nmb3_decision_policy.md
existed). The verdict is unchanged; the difference is that the
recommendation is now backed by an explicit, file-resident policy
rather than ad-hoc reasoning, and Block 003 is autonomously
approved rather than waiting for Steve's per-block sign-off.

---

## Verdict

**PARTIAL.**

A real single-parameter sweep was executed and produced honest,
varying evidence — but per the *Measurement Integrity Rules* of the
Decision Policy, the system "must not interpret score movement as
meaningful until baseline noise is measured". The Block 002 deltas
fall squarely in the policy's "require baseline stability testing"
band (0.06–0.08) and therefore cannot be promoted to a Pass on their
own evidence. The block is closed as PARTIAL with all coverage and
calibration gaps explicitly carried forward to Block 003.

## Evidence

Raw sweep table (from current_block_output.txt):

    onset_delta      score   within / total   delta vs baseline
    -----------------------------------------------------------
           0.05     0.8750      42 / 48               baseline
           0.10     0.7917      38 / 48                -0.0833
           0.15     0.8125      39 / 48                -0.0625
           0.20     0.7917      38 / 48                -0.0833

Policy-bound interpretation (Score Resolution Rule):

    Note resolution:  1 / 48  =  0.0208
    Observed deltas:  0.0625  =  3 note flips
                      0.0833  =  4 note flips

Per the policy, deltas of 0.06–0.08 are explicitly in the band that
"require baseline stability testing". They are not in the
"may be noise" band (< 0.02) and they are not yet in a "clearly
above noise" band — that determination requires Block 003.

Other observations:

1. The metric does respond to onset_delta — scores span 0.7917 to
   0.8750. The response is non-monotonic within the tested window.
2. Only one run per config — no repetition, no error bars.
3. Coverage gap: canonical plan listed 7 onset_delta values; runner
   executed 4. The boundary regions (0.01, 0.03, 0.25) are
   unmeasured. Per the *Block Ordering Rule*, these MUST NOT be
   added now — wider sweeps are forbidden until baseline stability
   is known.

## Risk

- **Process risk (carried forward, unresolved):** the canonical
  block_002_plan.md (7 values, autogen) still disagrees with what
  the runner executed (4 values, originally operator-approved).
  Per the policy this is not autonomously resolvable — the choice
  between reverting the plan vs extending the sweep is "subjective
  judgement not covered by this policy" (pause condition #6) and
  is therefore a Steve decision. It is *not* a blocker for Block
  003 because Block 003 does not depend on the onset_delta sweep.
- **Scientific risk (mitigated by Block 003):** without a
  noise-floor measurement, the observed 0.0625–0.0833 deltas may
  be indistinguishable from per-run jitter. Block 003 directly
  addresses this.
- **Scope risk (low):** no scope drift. Runner touched only
  onset_delta. All other DEFAULT_CONFIG fields unchanged.
- **Fake-progress risk (low):** sweep verified real (smoke-tested
  locally; canonical CI run 24929399657 produced matching numbers;
  bot commit 5fb41bb landed self-consistent report).

## Funding Relevance

Low. Per the policy: "The system must not begin optimization
before: (1) metric sensitivity is shown, (2) baseline
stability/noise floor is measured, (3) score changes are larger
than baseline jitter." Block 002 satisfies (1). Blocks 003+ are
required for (2) and (3). No funding claim is made.

## Recommended Next Block — Autonomously Approved Within M3.1

**block_003 — baseline stability / noise-floor characterisation.**

Policy check (autonomous approval requires all 7 to be true):

| # | Criterion                                      | block_003 |
|---|------------------------------------------------|-----------|
| 1 | Remains inside M3.1                            | yes       |
| 2 | Answers one question only                      | yes       |
| 3 | Reduces uncertainty                            | yes (directly measures noise floor) |
| 4 | Does not change project direction              | yes       |
| 5 | Does not make funding claims                   | yes       |
| 6 | Does not modify core architecture              | yes       |
| 7 | Validation / stability / measurement-integrity | yes (literally a stability block) |

Pause-condition check (any one true → Steve required):

| # | Condition                                      | Triggered? |
|---|------------------------------------------------|------------|
| 1 | Milestone transition proposed                  | no         |
| 2 | Funding claim proposed                         | no         |
| 3 | Core algorithm change proposed                 | no         |
| 4 | Results conflict with previous evidence        | no         |
| 5 | Drift or metric gaming detected                | no         |
| 6 | Subjective judgement not covered by policy     | no         |

Result: **block_003 is autonomously approved under
nmb3/nmb3_decision_policy.md.** No Steve decision is required to
proceed to block_003 itself.

The plan at nmb3/nmb3_blocks/block_003_plan.md has been updated to
use **8 baseline repetitions** (per the *Block 003 Policy* section
of the Decision Policy file), with an autonomous-approval marker.

## Items That Still Require Steve

The policy correctly forbids autonomous resolution of the
following — these are surfaced for Steve's attention but they do
NOT block block_003:

1. Block 002 closure: revert canonical plan to the 4-value sweep,
   or extend the sweep to cover [0.01, 0.03, 0.25]? (process /
   scope question — pause condition #6).
2. After block_003 completes and noise floor is known: whether the
   onset_delta sweep should be re-run / extended depends on what
   the noise floor turns out to be, and may itself require a Steve
   decision if the result is ambiguous.
3. Any future M3.1 → M4 milestone transition (always Steve).
