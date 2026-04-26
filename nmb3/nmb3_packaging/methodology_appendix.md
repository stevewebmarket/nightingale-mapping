# Methodology appendix

Generated:    2026-04-25T19:32:00Z
Author:       NMB3 autonomous loop, executing objective O038 under
              Steve's conditional permission at 2026-04-25T19:24:00Z
              (activated when O037 SUCCEEDED clean at canonical
              SHA be48a65 with architect review PASS).
Audience:     Steve, plus any external reviewer Steve chooses to
              hand this appendix to.
Scope:        Documents *how* the NMB3 autonomous loop produces
              evidence -- the loop discipline phases, the policy
              files that bind them, and the explicit honesty
              floors.  Does **not** rewrite, paraphrase-with-drift,
              or otherwise modify any policy file: where canonical
              text is needed, this appendix quotes it verbatim or
              points to the policy file by filename and section
              header.  Does **not** make funding, commercial,
              perceptual-validity, second-corpus generalisation,
              or real-time-deployment claims.  Does **not**
              re-litigate the P4 partial-scope closure or the M6
              partial-scope closure (both APPROVED by Steve and
              binding).
Companion:    `nmb3/nmb3_packaging/reproducibility_appendix.md`
              (O037, partial-scope) documents *what* evidence the
              loop has produced and pins it to head SHAs + CI run
              ids; this appendix documents *how* the loop produces
              evidence under what binding rules.

---

## 1. The loop discipline (phases)

The NMB3 loop's canonical 6-step cycle is defined verbatim in
`nmb3/nmb3_cycle.md` § "Cycle structure":

> 1. Steve approves a block plan
> 2. Execution Agent runs the block
> 3. Execution Agent writes report
> 4. System pauses
> 5. Interpreter Agent evaluates report
> 6. Steve reviews

The same file binds the supporting rules (verbatim from
`nmb3/nmb3_cycle.md` § "Rules"):

> - Only one block may be active at a time
> - Every block must answer one question
> - Every block must produce a report
> - No block may start without Steve approval
> - Execution Agent must stop after report

The current operational discipline implements this 6-step cycle
through six concrete phases.  The operational phases below are the
loop's current *practice*; they are not a back-edit of the
canonical cycle and they do not supersede it.  Each phase below
points at the policy file that binds it.

### Phase 1 — Block plan

A block plan is written under
`nmb3/nmb3_blocks/block_<NNN>_plan.md` against the template at
`nmb3/nmb3_block_template.md`.  Each block plan must answer
exactly one question (per `nmb3/nmb3_cycle.md` § "Rules") and
must enumerate Allowed Actions and Forbidden Actions for the
block.

### Phase 2 — Smoke test

Before any CI dispatch consumes paid runner minutes, the
manager runs a local smoke test (`replit_manager_smoke_test.py`
in repo root) to verify the runner script imports cleanly and
the runner contract is satisfied.  This is operational
discipline, not policy text; it derives from the
`nmb3/nmb3_autonomous_loop_policy.md` § "Allowed Autonomous
Actions" item "create runners for approved validation blocks"
and the implicit cost discipline of the session-budget cap on
workflow edits ("maximum workflow edits per session: 2", same
file § "Session Budget").

### Phase 3 — CI dispatch

CI runs are dispatched through the shared no-cache
reproducibility workflow at
`.github/workflows/nmb3_no_cache_repro.yml`.  The workflow takes
two parameterised inputs (`target` and `script`) and runs the
named script in a fresh checkout with no cached state, no
auto-commit of any artefact, and a 90-day artefact retention
window.  This pattern is what makes the SHA-pinned reproductions
in `nmb3/nmb3_packaging/reproducibility_appendix.md` § A
reviewer-verifiable: any external reviewer with GitHub Actions
access to the canonical repo (or a fork) can re-dispatch the
same workflow against the same head SHA with the same `target`
and `script` inputs and obtain the same headline number.

### Phase 4 — Bot commit

Commits produced by the loop are authored as
`nightingalemap <info@webmarket.ie>` (the bot identity).
Commits authored by Steve directly carry his own identity.
Commit messages produced by the loop are factual prose
describing what changed and why; they do not pre-judge any
Steve approval.

### Phase 5 — Interpreter output

After every CI run the Interpreter Agent
(`nmb3/nmb3_interpreter_agent.md` is its role file) writes a
report under `nmb3/nmb3_reports/o<NNN>_<short_name>.md`
following the report template at
`nmb3/nmb3_report_template.md`.  Interpreter outputs cite
specific run ids + head SHAs and label findings as PASS / FAIL
/ NEGATIVE / GAP / etc, never as "approved" (approval is
Steve's prerogative, see Phase 6).

### Phase 6 — Closure recommendation (when applicable)

When an interpreter output completes the evidence inventory for
a milestone or a phase, the loop writes a closure recommendation
under `nmb3/nmb3_reports/<scope>_closure_recommendation.md`
using the established § 1–§ 9 closure layout (issue / scope /
evidence / verdict / binding items / forbidden actions / out
of scope / reproducibility / Steve approval line).  The
closure recommendation is a *recommendation*; it becomes
binding only after Steve issues the verbatim chat string named
in the § 9 fill-in.  Until then the closure recommendation
exists as a draft and must not be cited as approved.

Two such closures are currently APPROVED on canonical:
  - **P4 partial-scope closure** -- recommendation at
    `nmb3/nmb3_reports/m5_phase_p4_closure_recommendation.md`,
    APPROVED by Steve at 2026-04-25T17:59:01Z via the verbatim
    string `"Approve P4 partial-scope closure"`.
  - **M6 partial-scope closure** -- recommendation at
    `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`,
    APPROVED by Steve at 2026-04-25T19:18:00Z via the verbatim
    string `"Approve M6 partial-scope closure"`.

---

## 2. Policy files that bind the loop

The following files in `nmb3/` are the canonical policy /
process surface.  This appendix references them by filename;
their canonical text is authoritative.  The loop is forbidden
from editing any of them (per O038's Forbidden actions field
and per the bound objectives' own Rewrite permission fields).

| File | Role |
|---|---|
| `nmb3/nmb3_manifesto.md` | The session-level mission and bounds. |
| `nmb3/nmb3_decision_policy.md` | Decision-making rules: measurement integrity, score resolution, block ordering, autonomous approval, current milestone authority. |
| `nmb3/nmb3_autonomous_loop_policy.md` | Autonomous loop rules: allowed/forbidden autonomous actions, session budget, early stop conditions, session completion rule. |
| `nmb3/nmb3_cycle.md` | The 6-step cycle, supporting rules, naming conventions. |
| `nmb3/nmb3_roles.md` | Role definitions: Steve, Manager, Execution, Interpreter, etc. |
| `nmb3/nmb3_manager_agent.md` | Manager Agent role and contract. |
| `nmb3/nmb3_execution_agent.md` | Execution Agent role and contract. |
| `nmb3/nmb3_interpreter_agent.md` | Interpreter Agent role and contract. |
| `nmb3/nmb3_replit_openai_manager.md` | Manager-on-Replit-with-OpenAI integration spec. |
| `nmb3/nmb3_toolchain.md` | Tool inventory and usage rules. |
| `nmb3/nmb3_block_template.md` | Canonical block plan template. |
| `nmb3/nmb3_report_template.md` | Canonical interpreter report template. |
| `nmb3/nmb3_objective_map.md` | The persistent objective queue (P0-P8 phases, O001-O043 entries) -- not a "policy file" per se but the canonical per-objective spec surface; objectives carry their own Rewrite permission field, which restricts edits to Steve. |

Decision-log file (canonical, append-only):
  - `nmb3/nmb3_decisions.log` -- timestamped decision entries
    recording every Steve string verbatim plus the loop's
    interpretation.  This file is append-only; prior entries
    are not edited or removed.

---

## 3. Explicit honesty floors

The loop's honesty floors are concentrated in
`nmb3/nmb3_autonomous_loop_policy.md` and
`nmb3/nmb3_decision_policy.md`.  The lists below are quoted
verbatim from those files; the loop is bound by the canonical
text, not by the quotes here.

### 3.1 Early Stop Conditions

Quoted verbatim from `nmb3/nmb3_autonomous_loop_policy.md`
§ "Early Stop Conditions":

> - results conflict with previous evidence
> - metric gaming is suspected
> - workflow fails twice
> - repo state becomes inconsistent
> - required evidence is missing
> - the next action would require a milestone transition
> - the next action would require changing this policy or the
>   decision policy

The binding effect of these conditions is whatever the
canonical policy file says it is; this appendix adds no
operational gloss.  See `nmb3/nmb3_autonomous_loop_policy.md`
for the canonical text.

### 3.2 Session Budget

Quoted verbatim from `nmb3/nmb3_autonomous_loop_policy.md`
§ "Session Budget":

> - maximum wall time: 3 hours
> - maximum loops: 6
> - maximum new files per loop: 3
> - maximum workflow edits per session: 2

The interpretation of these caps (e.g. how an in-loop erratum
counts against `maximum loops`, or how a multi-file commit
counts against `maximum new files per loop`) is governed by the
canonical policy file and any precedents recorded in
`nmb3/nmb3_decisions.log`; this appendix adds no rule about
those interpretations.

### 3.3 Forbidden Without Steve Approval

Quoted verbatim from `nmb3/nmb3_autonomous_loop_policy.md`
§ "Forbidden Without Steve Approval":

> - change milestone
> - move to M4
> - make funding claims
> - rewrite the decision policy
> - redefine the session objective
> - redesign the core algorithm
> - perform broad refactors
> - begin open-ended exploration

The `make funding claims` item directly bounds this appendix's
own framing and the framing of the companion reproducibility
appendix.  Both appendices accordingly use partial-scope
language (e.g. "3 SHA-pinned reproductions; 13 explicit
gaps") and quote the binding closures' own scope language
verbatim where citing closure outcomes; neither appendix
states, implies, or invites a funding-grade / perceptual /
generalisation / commercial-deployment claim.

### 3.4 Measurement integrity (decision policy anchor)

The canonical text governing measurement integrity lives in
`nmb3/nmb3_decision_policy.md` § "Measurement Integrity
Rules" and § "Score Resolution Rule"; the canonical "metric
gaming" floor is named in those sections and referenced from
the Early Stop Conditions list above.  This appendix does not
restate those rules; it points at them.

Operational anchor (factual, not a rule restatement): the
M6.5 FAIL re-validation in O034 was the most recent loop event
where the metric-gaming floor was a live consideration.  A
fresh CI reproduction returning PASS where the locked baseline
returned FAIL would have raised that floor; the fresh
reproduction returned FAIL with bit-identical headline table
and condition outputs (run id 24937928571 at SHA 9eaabac), so
no floor fired.  Documented in
`nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md` and
in the reproducibility appendix entry A.3.

---

## 4. Schema for `nmb3/nmb3_objective_map.md` entries

Every persistent objective in the queue is specified by an
entry in `nmb3/nmb3_objective_map.md`.  The canonical schema
is documented in that file under § "Schema (legend for every
entry below)" and is quoted verbatim here.  In any case of
discrepancy between this appendix and that file, the file is
authoritative.

> Each objective uses these eleven fields:
>
> - **Objective ID** — `O###` stable identifier.  Never reused.
> - **Name** — short human-readable title.
> - **Purpose** — one paragraph stating the question the objective
>   answers and why that answer matters for the funding package.
> - **Dependencies** — list of `O###` IDs that must be in `Status:
>   CLOSED (Steve-approved)` before this objective may begin.
> - **Success criteria** — pre-set, measurable, declared *before*
>   execution per Decision Policy "pass condition declared before run".
> - **Evidence required** — the concrete artefact(s) that must be
>   produced and committed to canonical before the objective may close.
> - **Allowed autonomous actions** — the bounded set of actions the
>   Autonomous Loop may take inside this objective.
> - **Forbidden actions** — explicit no-go list, in addition to the
>   global Decision Policy "Forbidden Without Steve Approval" set.
> - **Status** — one of: `PROPOSED`, `STEVE-APPROVED (NOT STARTED)`,
>   `IN PROGRESS`, `BLOCKED`, `CLOSED (Steve-approved)`, `CLOSED
>   (autonomously, validation block)`, `DEFERRED`, `OBSOLETE`.
> - **Auto-execute permission** — `NO`, `YES (validation/stability
>   only)`, or `YES (full)`.  Default `NO`.  Anything other than `NO`
>   must cite which Decision Policy autonomous-approval criterion
>   applies.
> - **Rewrite permission** — who may edit the objective definition
>   after Steve approves the roadmap.  Default: `Steve only`.  The
>   autonomous loop may always update the `Status` field to reflect
>   observed reality and may append evidence pointers; it may not edit
>   any other field without Steve approval.

Observed extension fields (not part of the canonical 11; used
where an objective's history warrants them and consistent with
the Rewrite-permission clause that the autonomous loop may
"append evidence pointers"):

  - **Rewrite history** — timestamped record of any rewrites
    Steve has authorised (with the verbatim Steve string and
    the loop's interpretation).  Example: the O037 entry in
    `nmb3/nmb3_objective_map.md` records the
    2026-04-25T19:24:00Z partial-scope rewrite under this
    field.
  - **Evidence to date** — progress notes recording partial
    evidence en route to the full `Evidence required` set.

Worked example: see the **O037** entry in
`nmb3/nmb3_objective_map.md` (around the `### O037` heading
in the P8 — Packaging artefacts section).  All 11 canonical
fields plus the Rewrite history extension are present and
populated.

Note on field-value drift: individual objective entries in
`nmb3/nmb3_objective_map.md` have, in practice, sometimes used
`Status` and `Auto-execute permission` values that vary from
the canonical enums (e.g. `Status: SUCCEEDED at <timestamp>`
or `Auto-execute permission: YES (documentation only)`).
Where this appendix is read alongside such entries, the
canonical schema text quoted above remains the binding
specification; any practical drift in individual entries is
visible in the file itself and can be reconciled by a future
schema-alignment objective.  This appendix does not amend the
canonical schema and does not endorse any drift; it documents
the schema as canonical text says it.

---

## 5. Non-claim register

This appendix does NOT make any of the following claims; each
would require its own Steve authorisation and its own objective:

  - It does NOT claim funding-grade rigour, perceptual
    validity, second-corpus generalisation, real-time
    deployability, or commercial readiness for the locked
    pipeline.
  - It does NOT claim full-chain reproducibility (only 3 of
    the 16 milestones referenced in the reproducibility
    appendix have SHA-pinned CI evidence on canonical; the
    appendix's own Section A/B framing is the operative
    statement).
  - It does NOT propose, endorse, or hint at any fix for the
    M6.5 FAIL or any other negative result.  Fix discussion
    belongs in O043 (continuation-scope out-of-scope
    register), which itself depends on O042 (Steve-only
    continuation-scope authorisation).
  - It does NOT edit any policy file.  The policy files
    (`nmb3/nmb3_decision_policy.md`,
    `nmb3/nmb3_autonomous_loop_policy.md`,
    `nmb3/nmb3_manifesto.md`, `nmb3/nmb3_roles.md`,
    `nmb3/nmb3_cycle.md`, the agent files, the toolchain
    file, the template files) are unchanged by this objective.
  - It does NOT restate any policy rule in a way that
    conflicts with its canonical text.  Where rules are
    presented above, they are direct quotes from the
    canonical files; any interpretive framing is clearly
    operational ("the loop's current practice") rather than
    policy authority.
  - It does NOT introduce any new policy, new role, new
    objective, new milestone, or new gate.
  - It does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 / M5.x or
    M6.x closure.
  - It does NOT invalidate the P4 partial-scope closure
    (APPROVED 2026-04-25T17:59:01Z) or the M6 partial-scope
    closure (APPROVED 2026-04-25T19:18:00Z).  Both closures
    remain binding; this appendix documents the loop
    discipline that produced them, not the closures
    themselves.
  - It does NOT soften M6.5's FAIL label or M6's partial-
    scope language.  The closure-binding scope language is
    the operative framing for any external citation.
  - It does NOT initiate any further loop after O038.
    Steve's session-scope stop rule from the
    2026-04-25T19:24:00Z chat string ("Stop after O038 or
    earlier if a gate triggers") binds the loop to halt at
    this objective's commit; subsequent objectives require a
    fresh Steve authorisation.
