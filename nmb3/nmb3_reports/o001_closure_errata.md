# O001 Closure Errata — gitignore fix

Audience:    Steve.
Author:      NMB3 autonomous loop.
Status:      Errata to canonical commit 33e533d ("NMB3 O001:
             CLOSED (Steve-approved); O002 STEVE-APPROVED (NOT
             STARTED)").  No milestone change.  No policy change.
             No funding claim.

---

## What happened

Commit 33e533d intended to land three files on canonical:

1. `nmb3/nmb3_objective_map.md` — O001/O002 status updates.
2. `nmb3/nmb3_reports/o001_closure_report.md` — closure session
   report.
3. `nmb3/nmb3_decisions.log` — Steve's verbatim closure string,
   as the load-bearing audit-trail evidence for O001 closure.

Files (1) and (2) landed.  File (3) was **silently dropped by a
system-wide `/etc/.gitignore` rule** matching `*.log`.  The repo's
own `.gitignore` was empty, so nothing in-repo opted the file
back in.  `git add` printed an "ignored paths" warning that the
loop caught on the immediate follow-up verification step.

This left canonical 33e533d in an internally-inconsistent state:
the objective map's O001 `Evidence to date` field listed
`nmb3/nmb3_decisions.log` as the carrier of Steve's verbatim
string, but the file was not on canonical.

## What this errata commit does

- Adds a repo-local `.gitignore` containing exactly one rule:
  `!nmb3/nmb3_decisions.log`.  This pins the audit-trail log as
  canonical and overrides the system `*.log` rule for this one
  file.  The repo-local `.gitignore` was previously absent (empty
  pre-existing state), so adding it does not reverse any prior
  policy.
- Force-adds `nmb3/nmb3_decisions.log` (already present locally
  with the correct 2026-04-25T16:34:20Z entry written in 33e533d's
  workspace) to canonical.  Once tracked, future appends to this
  file will not require `-f` because gitignore does not apply to
  tracked files.
- Adds this errata file as the audit record of the catch-and-fix.

## What this errata commit does NOT do

- Does not edit `nmb3/nmb3_objective_map.md`.  The references to
  `nmb3/nmb3_decisions.log` are now valid as written; no edit is
  required.
- Does not edit `nmb3/nmb3_reports/o001_closure_report.md`.  Its
  pointer to `nmb3_decisions.log` is now valid as written.
- Does not edit `nmb3/nmb3_reports/m3_1_closure_recommendation.md`
  (forbidden under O001).
- Does not edit `nmb3/nmb3_decision_policy.md` or
  `nmb3/nmb3_autonomous_loop_policy.md`.
- Does not edit `MILESTONES.md`.
- Does not begin O002 or any other objective.
- Does not change Steve's closure string or its effects.  O001
  remains CLOSED (Steve-approved) at 2026-04-25T16:34:20Z; O002
  remains STEVE-APPROVED (NOT STARTED) at the same timestamp; the
  "narrow reading" closure remains exactly as recorded in
  `nmb3/nmb3_decisions.log`.

## Was this an early-stop event?

The autonomous loop policy lists "required evidence is missing"
and "repo state becomes inconsistent" as early-stop conditions.
Both were true between commits 33e533d and the present errata
commit.  The loop triggered the early-stop discipline by
verifying the canonical state immediately after the closure push,
catching the gitignore drop, and refusing to proceed past O001
closure until the inconsistency was resolved on canonical.

The fix is mechanical and confined to repo infrastructure (one
new `.gitignore` line, one force-add).  No scientific, policy, or
strategic content was changed.  The loop now stops, exactly where
it was scheduled to stop after O001 closure.

## Lesson for future Steve-decision logs

Once the audit-trail log is tracked (after this commit), future
appends to it will not require force-adding.  But the loop will
still verify, after every commit that touches
`nmb3/nmb3_decisions.log`, that the file is present on canonical
and that its tail matches the new entry's expected wording.  This
verification step is folded into the loop's standard
post-commit checks under the autonomous loop policy "save raw
evidence and report" rule.

## Stop

Errata applied.  The loop now stops where it was originally
scheduled to stop after O001 closure.  Awaiting Steve's next
instruction (e.g., "Execute O002").

Canonical state at end of errata:

    33e533d  NMB3 O001: CLOSED (Steve-approved); O002 STEVE-APPROVED (NOT STARTED)
    (this commit)  NMB3 O001 errata: gitignore fix; decisions.log force-added to canonical
