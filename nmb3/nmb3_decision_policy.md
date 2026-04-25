# NMB3 Decision Policy

## Purpose

This file defines how the NMB3 Manager/Interpreter should make decisions without Steve in the middle.

The Manager may recommend and execute low-risk next blocks if they stay inside the current milestone and obey this policy.

## Current Milestone Authority

Current milestone:
M3.1 — invariance metric validation.

The system may autonomously continue within M3.1.

The system may not move from M3.1 to M4 without explicit Steve approval.

## Measurement Integrity Rules

The system must not interpret score movement as meaningful until baseline noise is measured.

The system must not extend parameter sweeps before baseline stability is known.

The system must not begin optimization before:
1. metric sensitivity is shown,
2. baseline stability/noise floor is measured,
3. score changes are larger than baseline jitter.

The system must distinguish:
- real signal,
- measurement noise,
- metric gaming,
- incomplete evidence.

## Score Resolution Rule

Current M3.1 score is measured over 48 note-level units.

One note flip corresponds to approximately:

1 / 48 = 0.0208

Therefore:
- deltas below ~0.02 may be noise,
- deltas around 0.06–0.08 require baseline stability testing,
- deltas must be compared against repeated baseline variance before being treated as meaningful.

## Block Ordering Rule

After Block 002 sensitivity sweep, the next correct block is baseline stability / noise-floor characterization.

Block 003 must therefore test repeated baseline runs before any:
- wider sweep,
- optimization,
- M4 demo,
- funding claim.

## Autonomous Approval Rules

The Manager/Interpreter may autonomously approve and execute the next block if all are true:

1. The next block remains inside M3.1.
2. The next block answers one question only.
3. The next block reduces uncertainty.
4. The next block does not change project direction.
5. The next block does not make funding claims.
6. The next block does not modify core architecture.
7. The next block is a validation, stability, or measurement-integrity block.

The Manager/Interpreter must pause for Steve if:

1. A milestone transition is proposed.
2. A funding claim is proposed.
3. Core algorithm changes are proposed.
4. Results conflict with previous evidence.
5. The system detects drift or metric gaming.
6. The next action requires subjective judgement not covered by this policy.

## Block 003 Policy

For Block 003, use:

Baseline repetitions:
8

Reason:
Block 002 observed score deltas of approximately 0.0625–0.0833, equal to roughly 3–4 note flips out of 48. Eight repeated baseline runs are required to estimate whether that difference is larger than normal baseline jitter.

Block 003 question:
Are baseline M3.1 scores stable enough that Block 002 score deltas can be interpreted as real parameter sensitivity?

## Final Rule

When uncertain, choose the next block that measures uncertainty rather than expanding exploration.
