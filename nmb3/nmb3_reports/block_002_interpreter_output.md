# NMB3 Block 002 — Interpreter Output

Block:        block_002
Milestone:    M3.1 — invariance metric
Plan:         nmb3/nmb3_blocks/block_002_plan.md
Report:       nmb3/nmb3_reports/current_block_report.md
Raw output:   nmb3/nmb3_logs/current_block_output.txt
Runner:       run_nmb3_block_002.py @ canonical bfcfc50

---

## Verdict

**PARTIAL.**

A real single-parameter sweep was executed and produced honest, varying
evidence — but only for 4 of the 7 onset_delta values listed in the
canonical plan, and within that 4-value window the metric response is
non-monotonic and small relative to the likely noise floor (which has
not yet been characterised). The block cannot yet be called a Pass
because its stated question — *"How does systematic variation of
onset_delta alone affect the invariance metric score?"* — is not
answered with sufficient coverage or signal-to-noise context.

## Evidence

Raw sweep table (from current_block_output.txt):

    onset_delta      score   within / total   delta vs baseline
    -----------------------------------------------------------
           0.05     0.8750      42 / 48               baseline
           0.10     0.7917      38 / 48                -0.0833
           0.15     0.8125      39 / 48                -0.0625
           0.20     0.7917      38 / 48                -0.0833

Honest observations:

1. The metric does respond to onset_delta — scores span 0.7917 to 0.8750
   (range 0.0833, ~8.3 percentage points).
2. The response is **non-monotonic** within the tested window: the
   score drops at 0.10, partially recovers at 0.15, drops again at 0.20.
3. All deltas are on the order of 1–2 note flips out of 48 total notes
   (one note flip = 0.0208 score change). The smallest reported delta
   (-0.0625) is exactly 3 note flips. Without a noise-floor measurement
   we cannot distinguish real parameter sensitivity from per-note
   classification jitter.
4. Only one run per config — no repetition, no error bars.
5. Coverage gap: the canonical plan listed
   `[0.01, 0.03, 0.05, 0.10, 0.15, 0.20, 0.25]` (7 values). The runner
   executed `[0.05, 0.10, 0.15, 0.20]` (4 values). The very-tight end
   (0.01, 0.03) and the very-loose end (0.25) are unmeasured. These are
   precisely the regions where saturation / breakdown behaviour would
   most likely appear.

## Risk

- **Process risk (high):** the canonical block_002_plan.md (7 values)
  and the executed sweep (4 values) disagree. The 4-value sweep is the
  one Steve originally approved (commit cca5d55), and the 7-value
  version was introduced later by the auto-generator overwriting the
  approved plan. Either the plan should be reverted to match what was
  run, or the run should be extended to match the plan. Leaving the
  mismatch in place is exactly the "small lie" the project is trying
  to avoid.
- **Scientific risk (medium):** without a noise-floor measurement, the
  observed 0.0625–0.0833 deltas may be indistinguishable from
  per-run / per-note jitter. Any Block 004 conclusion drawn on top of
  Block 002 alone would rest on uncalibrated evidence.
- **Scope risk (low):** no scope drift detected. The runner touched
  only `onset_delta`. Other DEFAULT_CONFIG fields were unchanged.
- **Fake-progress risk (low):** the sweep is real (locally smoke-tested
  on canonical samples; canonical CI run id 24929399657 produced
  matching numbers; bot commit 5fb41bb landed the corrected
  self-consistent report). No metric gaming detected.

## Funding Relevance

Low at this checkpoint. The block confirms the metric is not a flat
constant function of onset_delta, which is mildly reassuring, but does
not yet support any external claim ("the metric responds predictably
to a musically-relevant timing parameter"). Such a claim requires:

- a calibrated noise floor (Block 003), and then
- full sweep coverage including the boundary regions (post-Block 003).

## Recommended Next Block

**block_003 — baseline stability / noise-floor characterisation.**

Rationale: this matches the next expected work item already named in
nmb3_manifesto.md ("Block 003: test baseline stability") and it is
the single highest-leverage thing we can do — it is the precondition
for interpreting the Block 002 deltas as signal vs noise, and it is
the precondition for trusting any future sweep (including the
extension to 0.01 / 0.03 / 0.25).

A draft plan has been written to:

    nmb3/nmb3_blocks/block_003_plan.md

It is **not** approved. It is **not** executed. Per the Interpreter
Agent rules, I cannot approve my own recommendation. Steve must
approve (or amend, or reject) before the Manager / Execution layer
acts on it.

## One Decision Required From Steve

Approve, amend, or reject the proposed block_003 plan
(baseline stability over 5 repeated runs of the M3.1 default config,
no parameter changes). Specifically: is N=5 sufficient, or should
we run more repetitions to get a tighter variance estimate before
extending the onset_delta sweep?

Secondary decision (can be answered separately): should the canonical
block_002_plan.md be reverted to the 4-value sweep that was actually
executed, or should the sweep be extended to cover the 3 missing
values (0.01, 0.03, 0.25) before declaring Block 002 closed?
