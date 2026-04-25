# NMB3 Autonomous Loop Policy

## Purpose

This policy defines how NMB3 may run bounded autonomous sessions without Steve in the middle of every micro-decision.

The goal is disciplined progress inside the current milestone, not open-ended exploration.

## Current Authorized Objective

Current objective:
Complete M3.1 validation.

Current starting point:
Block 003 — baseline stability / noise-floor characterization.

## Loop Shape

Each autonomous loop must follow:

1. Read objective, manifesto, decision policy, autonomous loop policy, latest plan, latest report, and latest raw output.
2. Interpret the current state.
3. Choose the next bounded action inside the authorized objective.
4. Implement only what is needed.
5. Execute.
6. Save raw evidence and report.
7. Decide whether the authorized objective is complete.
8. Continue only if the next action remains inside the authorized objective.

## Session Budget

Initial autonomous session limit:
- maximum wall time: 3 hours
- maximum loops: 6
- maximum new files per loop: 3
- maximum workflow edits per session: 2

If any limit is reached, stop and write a session report.

## Allowed Autonomous Actions

Inside M3.1 only, the system may:
- create runners for approved validation blocks
- update workflow to call the current runner
- execute the workflow
- interpret raw outputs
- generate the next validation block
- commit reports, logs, and block plans
- continue to the next loop if it stays within M3.1 validation

## Forbidden Without Steve Approval

The system must not:
- change milestone
- move to M4
- make funding claims
- rewrite the decision policy
- redefine the session objective
- redesign the core algorithm
- perform broad refactors
- begin open-ended exploration

## Session Completion Rule

If the assigned objective is achieved before the time budget:

- stop execution
- produce a session summary report
- propose the next objective
- do not begin the next objective

The system must not fill time by inventing work.

## Early Stop Conditions

Stop immediately and write a session report if:
- results conflict with previous evidence
- metric gaming is suspected
- workflow fails twice
- repo state becomes inconsistent
- required evidence is missing
- the next action would require a milestone transition
- the next action would require changing this policy or the decision policy

## Current Session Mission

Mission:
Complete M3.1 validation enough to decide whether the metric is stable and meaningful.

Start with:
Block 003 — baseline stability / noise floor.

Expected next actions:
1. build and run Block 003
2. interpret baseline variance
3. compare Block 002 deltas against baseline noise
4. decide whether M3.1 is pass / partial / fail
5. produce session report
6. propose next objective

## Final Rule

When uncertain, measure uncertainty.

Do not expand exploration just because time remains.
