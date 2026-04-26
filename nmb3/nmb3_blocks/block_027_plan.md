Block ID:
block_027

Current Milestone:
O038 methodology appendix -- not a measurement milestone.  This
block produces the methodology appendix that describes the
autonomous loop discipline (block plan -> smoke test -> CI
dispatch -> bot commit -> interpreter output -> closure
recommendation), the policy files that bind it, and the explicit
honesty floors.

This block does NOT advance any pipeline, run any new CI workflow,
modify any locked metric, or edit any policy file.  It does NOT
restate policy rules in a way that conflicts with their canonical
text -- it cites and quotes the canonical text where it appears.

Approval Status:
STEVE-AUTHORISED via the chat string at 2026-04-25T19:24:00Z that
ended with "After re-scoping, execute O037 under this partial-scope
definition.  If O037 succeeds, execute O038 only if its dependency
is then satisfied and no new gate is triggered.  Stop after O038
or earlier if a gate triggers."

The conditional permission is now satisfied:
  - O037 SUCCEEDED at canonical SHA be48a65 at 2026-04-25T19:26:00Z
    under the partial-scope rewrite.
  - Architect review of the O037 commit returned PASS with no
    BLOCKING / HIGH findings (no gate triggered).
  - O038's declared dependency (O037) is therefore satisfied on
    canonical.

This is the second and final objective of the session per Steve's
stop rule.

The Steve string is recorded verbatim in
`nmb3/nmb3_decisions.log` at the 2026-04-25T19:24:00Z entry; this
block also records (in `nmb3/nmb3_decisions.log` after the O037
APPROVED-clean architect note) the loop's interpretation that
O038 is now unblocked.

One Question to Answer:
Does `nmb3/nmb3_packaging/methodology_appendix.md` exist;
describe the autonomous loop discipline (block plan -> smoke
test -> CI dispatch -> bot commit -> interpreter output ->
closure recommendation) by reference to the canonical policy
files that bind it (`nmb3/nmb3_decision_policy.md`,
`nmb3/nmb3_autonomous_loop_policy.md`, `nmb3/nmb3_cycle.md`,
`nmb3/nmb3_manifesto.md`, `nmb3/nmb3_roles.md`,
`nmb3/nmb3_manager_agent.md`, `nmb3/nmb3_execution_agent.md`,
`nmb3/nmb3_interpreter_agent.md`, `nmb3/nmb3_replit_openai_manager.md`,
`nmb3/nmb3_toolchain.md`, `nmb3/nmb3_block_template.md`,
`nmb3/nmb3_report_template.md`); document the explicit honesty
floors (the Early Stop Conditions in the autonomous loop policy,
the Forbidden Without Steve Approval list in that same policy,
and the Session Budget); and reference the schema for objective
entries in `nmb3/nmb3_objective_map.md` (the canonical 11
fields plus the optional Rewrite history / Evidence to date
extensions)?

Why This Matters:
The methodology appendix is the funder-facing artefact that
documents *how* the loop produces its evidence, not *what* the
evidence is (that's the reproducibility appendix from O037).
Three properties matter:

  - **Faithful citation of policy.**  O038's Forbidden actions
    field forbids "restating policy rules in a way that
    conflicts with their canonical text".  The appendix
    therefore quotes canonical phrasing verbatim where helpful
    and references policy files by filename + section header
    rather than paraphrasing rules.  Any paraphrase that risks
    conflict gets replaced with a direct quote or a "see
    `<file>.md`" pointer.
  - **Honest scope boundary.**  The appendix is a methodology
    document, not a methodology rewrite.  It does not edit any
    policy file, does not invent new rules, and does not soften
    or harden any existing rule.  Where the operational
    discipline (smoke test, CI dispatch, bot commit, closure
    recommendation) extends beyond the original 6-step cycle in
    `nmb3/nmb3_cycle.md`, the appendix says so explicitly --
    the operational extension is documented as the loop's
    current concrete practice, not as a back-edit of the
    canonical cycle.
  - **No scope creep.**  The appendix does not make funding /
    commercial / perceptual / generalisation claims; does not
    re-litigate any closed milestone; does not propose any new
    objective; does not advance any other objective; does not
    request a Steve approval.  It is documentation of the loop
    that has already produced the SHA-pinned reproductions in
    O037's appendix and the closures Steve has already
    approved.

Allowed Actions:
- Write `nmb3/nmb3_blocks/block_027_plan.md` (this file).
- Write `nmb3/nmb3_packaging/methodology_appendix.md` with:
    (1) header noting authorship, scope, provenance;
    (2) a description of the loop discipline phases, each
        phase referencing the policy file(s) that bind it
        and citing canonical text where useful;
    (3) a section on the explicit honesty floors quoting the
        canonical "Early Stop Conditions", "Forbidden Without
        Steve Approval", and "Session Budget" lists from
        `nmb3/nmb3_autonomous_loop_policy.md` and the
        canonical "Measurement Integrity Rules" anchor from
        `nmb3/nmb3_decision_policy.md`;
    (4) a section on the schema for `nmb3/nmb3_objective_map.md`
        entries listing the 11 canonical fields and the
        optional extensions, with a worked example pointing at
        an existing objective entry;
    (5) a non-claim register paralleling the reproducibility
        appendix's Section C (no funding / commercial /
        perceptual / generalisation claims; no policy edit; no
        closure re-litigation; no scope creep).
- Update O038 PROPOSED -> SUCCEEDED in
  `nmb3/nmb3_objective_map.md` after the appendix is written.
- Append a `nmb3/nmb3_decisions.log` entry recording (a) the
  O037 APPROVED-clean architect outcome, (b) the loop's
  interpretation that O038's declared dep is now satisfied and
  Steve's conditional permission therefore active, (c) the
  session stop rule binding execution to halt after O038.
- Commit and push under nightingalemap/info@webmarket.ie.

Forbidden Actions (per O038's canonical Forbidden actions field,
plus this block's discipline):
- Editing any policy file
  (`nmb3/nmb3_decision_policy.md`,
  `nmb3/nmb3_autonomous_loop_policy.md`,
  `nmb3/nmb3_manifesto.md`, `nmb3/nmb3_roles.md`,
  `nmb3/nmb3_cycle.md`, the agent files, the toolchain file, the
  template files).
- Restating any policy rule in a way that conflicts with its
  canonical text.  Direct quotes and filename pointers are safe;
  paraphrases that change scope, severity, applicability, or
  authority are forbidden.
- Editing `MILESTONES.md`, the M3.1 archive, the M3.1 closure
  recommendation, the P4 closure recommendation, the M6 closure
  recommendation, the boundary document, the O023 / O033 / O034
  interpreter outputs, the O037 reproducibility appendix, the
  shared workflow yml, or any pipeline code.
- Editing `nmb3/nmb3_README.md` (no Steve authorisation).
- Re-running any CI workflow.
- Advancing any other objective beyond O038 (Steve's stop rule
  binds the session to halt after O038 or earlier on gate).
- Auto-applying any "approval"; O038 SUCCEEDED is a loop status,
  not a Steve approval.  No funder-facing approval headers
  needed in the appendix (it is documentation, not a closure
  recommendation).
- Claiming the methodology appendix demonstrates funding-grade
  rigour, perceptual validity, second-corpus generalisation,
  real-time deployability, or any commercial readiness.
- Re-litigating the P4 partial-scope closure or the M6
  partial-scope closure.

Pass Criteria for this block (per O038's canonical success
criteria):
- `nmb3/nmb3_packaging/methodology_appendix.md` exists at the
  commit closing this block.
- The appendix references the binding policy files (every file
  listed in the block plan above appears at least once as a
  filename pointer).
- The appendix references the schema in
  `nmb3/nmb3_objective_map.md` (the 11 canonical fields are
  enumerated; optional extensions noted; at least one worked
  example points at a real objective entry).
- The appendix does not edit any policy file (verifiable via
  the commit's diff stat).
- The appendix does not restate any policy rule in a way that
  conflicts with the canonical text (verifiable by quote vs
  policy file at the commit's head SHA).
- O038's status is updated PROPOSED -> SUCCEEDED in the
  objective map at the same commit.
- The decisions.log entry records the O037 APPROVED-clean
  architect outcome and the activation of Steve's conditional
  O038 permission, plus the session stop rule binding the
  loop to halt after O038.

Out of Scope (explicit non-claims):
- This block does NOT formally re-validate any milestone.
- This block does NOT claim full-chain reproducibility (that
  framing is forbidden by the O037 partial-scope rewrite and
  is not magically reinstated by the methodology appendix).
- This block does NOT make funding, commercial, perceptual-
  validity, second-corpus generalisation, or real-time-
  deployment claims.
- This block does NOT propose, endorse, or hint at any fix for
  the M6.5 FAIL or any other negative result.
- This block does NOT advance O030 / O031 / O032 (M6.1 / M6.2 /
  M6.3 fresh CI re-validation), O039-O041 (other packaging
  artefacts), O042 (continuation-scope authorisation), or O043
  (out-of-scope register).
- This block does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 / M5.x
  / M6.x closure.
- This block does NOT invalidate the P4 partial-scope closure
  (APPROVED at 2026-04-25T17:59:01Z) or the M6 partial-scope
  closure (APPROVED at 2026-04-25T19:18:00Z).
- This block does NOT initiate any further loop after O038.
  Per Steve's stop rule "Stop after O038 or earlier if a gate
  triggers", the loop halts at this commit (architect review
  of O038 + any errata fall within the same objective and so
  do not violate the stop rule; new objectives do).
