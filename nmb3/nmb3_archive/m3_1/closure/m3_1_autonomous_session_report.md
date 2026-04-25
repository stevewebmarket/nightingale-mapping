# NMB3 — M3.1 Autonomous Validation Session Report

Session governance: nmb3/nmb3_autonomous_loop_policy.md (binding)
Per-block governance: nmb3/nmb3_decision_policy.md (binding)
Mission: complete M3.1 validation enough to decide whether the
metric is stable and meaningful.

---

## Mission Outcome

**M3.1 validation evidence is complete. Metric is BOTH stable AND
meaningful (responsive to a known timing parameter).**

The session does NOT autonomously declare the M3.1 milestone closed
— that is a Steve decision, per Decision Policy "Forbidden Without
Steve Approval: change milestone".

## Budget Usage

| Limit                       | Used | Cap | Remaining |
|-----------------------------|-----:|----:|----------:|
| Wall time                   | ~3 min | 3 hours | well under |
| Loops                       | 3    | 6   | 3         |
| Workflow edits              | 1    | 2   | 1         |
| New files (this session)    | 3    | 3 / loop | within   |

Loops executed:

1. **Build + smoke-test runner.** Wrote run_nmb3_block_003.py;
   smoke-tested locally on canonical samples; caught + fixed a
   cosmetic display bug (within-counter was case-level instead of
   note-level) before any commit.
2. **Workflow swap + dispatch + bot commit.** Single yml edit
   (block_002 → block_003 in 5 places); pushed runner + yml; manual
   workflow_dispatch; CI run id 24934283280 succeeded; bot commit
   488a889 landed identical numbers to the local smoke test.
3. **Interpret + write artifacts + stop.** Wrote
   nmb3/nmb3_reports/block_003_interpreter_output.md and this file;
   no new objective started.

No early-stop condition triggered: no conflicting evidence, no
suspected metric gaming, no workflow failures, no inconsistent repo
state, no missing evidence, no proposed milestone transition, no
proposed policy change.

## Evidence Summary

### Block 002 — onset_delta sensitivity (carried in from prior turns)

Sweep: onset_delta in [0.05, 0.10, 0.15, 0.20]; all other fields
DEFAULT_CONFIG.

    onset_delta   score    delta vs baseline
    ----------------------------------------
       0.05      0.8750    baseline
       0.10      0.7917    -0.0833
       0.15      0.8125    -0.0625
       0.20      0.7917    -0.0833

Score does respond to onset_delta. Response is non-monotonic in the
tested window. Coverage gap: 3 of the 7 originally-planned values
(0.01, 0.03, 0.25) were not run — flagged for Steve, not blocking
the M3.1 stable-and-meaningful judgement.

### Block 003 — baseline stability / noise-floor (this session)

Eight repeated runs of DEFAULT_CONFIG, no parameter changes.
All eight produced **bit-identical case-level results and identical
scores of 0.8750**. Population stdev across 8 runs = 0.0000. Span
(max − min) = 0.0000. The M3.1 pipeline is deterministic.

CI run id 24934283280, head ce6eca9, conclusion=success.
Bot commit 488a889 landed the evidence on canonical.

### Combined: signal-vs-noise

Block 002 deltas of 0.0625 and 0.0833 are 3 and 4 note flips out of
48 respectively. Baseline stdev = 0. delta / stdev = ∞. The Block
002 deltas are real responses to onset_delta, not pipeline jitter.

## Decision Policy Audit (M3.1 unblocking sequence)

Per the Decision Policy: "The system must not begin optimization
before: (1) metric sensitivity is shown, (2) baseline stability /
noise floor is measured, (3) score changes are larger than baseline
jitter."

| Prerequisite                              | Status (this session) |
|-------------------------------------------|-----------------------|
| (1) metric sensitivity shown              | YES (Block 002)       |
| (2) baseline stability / noise floor measured | YES (Block 003)   |
| (3) score changes > baseline jitter       | YES (∞-many stdevs)   |

All three prerequisites for *technical* M3.1 readiness are met.
The remaining gates (M3.1 closure, M3.1 → M4 transition, any funding
claim) are policy-level / Steve-level decisions and are explicitly
out of autonomous scope.

## Honest Limits of This Conclusion

- "Meaningful" here means "responsive in a measurable, deterministic
  way to a known timing parameter on the canonical sample set". It
  does **not** yet mean "the score corresponds to human-perceived
  structural preservation" — that is a stronger claim that would
  need its own block (and probably its own Steve judgement on how
  to frame the question).
- Coverage of the onset_delta parameter space is partial (4 of 7
  planned values).
- Generalisation across audio types beyond the canonical 6-case set
  is untested.
- Sensitivity to parameters other than onset_delta is untested.

None of these limits invalidate the stable-and-meaningful judgement
on the canonical M3.1 question; they are the next layer of work,
not corrections to this layer.

## Proposed Next Objective (NOT begun, per autonomous loop policy)

**Objective: M3.1 closure decision.**

This is a Steve decision, framed as one binary plus one optional
follow-up:

1. (binary) Close M3.1 now on the strength of Blocks 001–003, or
   require the Block 002 coverage gap to be filled first (extend
   onset_delta sweep to {0.01, 0.03, 0.25} as a small block_004a
   under M3.1)?
2. (optional, only if M3.1 is being closed) Authorise the M3.1 → M4
   milestone transition.

The autonomous loop will not begin work on either of these without
Steve's explicit instruction. Per policy: *"The system must not fill
time by inventing work."*

## Stop

Session terminated cleanly. No new loop initiated. No milestone
change. No funding claim. No decision-policy or autonomous-loop-
policy edits.

Canonical state at session end:

- ce6eca9  NMB3 Block 003: real baseline-stability runner + workflow wiring
- 488a889  Add current block results  (bot)
- (this commit)  NMB3: Block 003 interpreter output + M3.1 session report
