Block ID:
block_026

Current Milestone:
O037 reproducibility appendix (partial-scope) -- not a measurement
milestone.  This block produces the reproducibility appendix that
documents the three SHA-pinned reproductions on canonical (M5.6
from O023, M6.4 from O033, M6.5 from O034) and explicitly lists
the 13 milestones that are not yet SHA-pinned (M3.1, M3.2, M3.3,
M3.4, M4.1, M5.1, M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3) as
gaps not failures.

This block does NOT advance any pipeline, run any new CI workflow,
or modify any locked metric.  It does NOT formally re-validate any
of the 13 gap milestones (Steve's rewrite explicitly forbids a
broader CI-pinning campaign).  It does NOT claim full-chain
reproducibility.

Approval Status:
STEVE-AUTHORISED via the chat string at 2026-04-25T19:24:00Z that
opens with "Re-scope O037 to partial-scope.  Rewrite permission
granted by Steve.", continues with the new partial-scope
specification (3 SHA-pinned milestones + 13 explicit gaps; no
broader CI-pinning campaign; no full-chain reproducibility claim;
no policy change; no funding claim), and ends with "After
re-scoping, execute O037 under this partial-scope definition.
If O037 succeeds, execute O038 only if its dependency is then
satisfied and no new gate is triggered.  Stop after O038 or
earlier if a gate triggers."

This is two separate Steve actions in one chat turn:
  1. Rewrite of O037 (Rewrite permission granted by Steve;
     Steve is the only person authorised to rewrite an
     objective per the canonical Rewrite permission field).
  2. Authorisation to execute O037 under the new spec, plus
     conditional authorisation to execute O038 if O037
     succeeds and no new gate triggers.

Both actions are recorded verbatim in
`nmb3/nmb3_decisions.log` for this block.

The dependency O036 is APPROVED at canonical SHA ea935f4
(2026-04-25T19:18:00Z); the rewrite did not change the dep.

One Question to Answer:
Does `nmb3/nmb3_packaging/reproducibility_appendix.md` exist,
list the three SHA-pinned reproductions (M5.6 / M6.4 / M6.5)
with full pinning (head SHA, CI run id, exact command, workflow
file, artefact name, headline number), explicitly list the 13
non-SHA-pinned milestones (M3.1, M3.2, M3.3, M3.4, M4.1, M5.1,
M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3) as gaps not failures
with each gap entry naming the script whose locked baseline
lives in MILESTONES.md, and explicitly disclaim full-chain
reproducibility / funding / commercial / perceptual claims?

Why This Matters:
The reproducibility appendix is the funder-facing artefact that
documents what *can* be reproduced from the canonical research
repo right now.  Three properties matter:

  - **SHA-pinned section honesty.**  Every number in the
    SHA-pinned section must be traceable to a CI run id + head
    SHA + exact command, so an external reviewer can dispatch
    the same workflow against the same SHA and get the same
    number.  Un-pinned numbers in this section would mislead
    the reviewer.
  - **Gap-list completeness.**  All 13 non-SHA-pinned
    milestones must be listed, each labelled "gap, not
    failure".  Omitting any gap would let a reviewer
    incorrectly assume the missing milestone is fully
    reproduced; mis-labelling a gap as a failure would
    incorrectly imply a negative result.
  - **No claim inflation.**  Steve's rewrite explicitly
    forbids claiming full-chain reproducibility, making
    funding claims, or running a broader CI-pinning campaign
    to backfill the gaps.  The appendix must be precisely
    what its scope says it is: a partial-scope reproducibility
    record + an honest gap list.

Allowed Actions:
- Apply the O037 rewrite to `nmb3/nmb3_objective_map.md`
  (Purpose, Dependencies, Success criteria, Evidence required,
  Allowed autonomous actions, Forbidden actions, Rewrite
  history fields all updated; Status remains PROPOSED until
  the appendix is written and committed).
- Write `nmb3/nmb3_blocks/block_026_plan.md` (this file).
- Create `nmb3/nmb3_packaging/` directory (if not present)
  and write `nmb3/nmb3_packaging/reproducibility_appendix.md`
  with:
    (a) header noting partial-scope and the rewrite
        provenance;
    (b) Section A: three SHA-pinned reproductions, each
        with head SHA + CI run id + exact command + workflow
        file + artefact name + headline number + interpreter
        output filename + verifier command an external
        reviewer can run to re-dispatch the same workflow;
    (c) Section B: explicit list of all 13 non-SHA-pinned
        milestones (M3.1, M3.2, M3.3, M3.4, M4.1, M5.1,
        M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3), each
        labelled "gap, not failure", each pointing at the
        MILESTONES.md baseline, each naming the script whose
        locked baseline carries the result;
    (c) Section C: explicit non-claim register disclaiming
        full-chain reproducibility / funding / commercial /
        perceptual claims, and stating that Steve's rewrite
        forbids running a broader CI-pinning campaign within
        O037's scope (any future broader campaign would
        require its own Steve authorisation).
- Update O037 PROPOSED -> SUCCEEDED in objective_map.md
  after the appendix is written.
- Append the standard Steve-string + interpretation entry
  to `nmb3/nmb3_decisions.log` recording both the rewrite
  string and the execute string.
- Commit and push under nightingalemap/info@webmarket.ie.

Forbidden Actions (per O037 rewrite, plus this block's discipline):
- Omitting any of the 13 non-SHA-pinned milestones from the
  Section B gap list.  (M3.1, M3.2, M3.3, M3.4, M4.1, M5.1,
  M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3 -- all 13 must
  appear.)
- Mis-labelling a gap as a failure (or vice-versa).  Gap
  means "no SHA-pinned CI evidence yet on canonical"; failure
  would mean "the milestone has been re-validated and the
  result is negative".  M5.7 / M5.8 / M5.9 / M6.5 are
  examples of milestones with locked NEGATIVE / FAIL results
  (not gaps); the 13 listed are gaps (not failures).
- Introducing into Section A any number that is not pinned
  to a CI run id + head SHA.
- Running a broader CI-pinning campaign (specifically
  forbidden by Steve's rewrite string).  Any future campaign
  would require its own Steve authorisation.
- Claiming full-chain reproducibility (the appendix is
  partial-scope; it must say so).
- Editing any policy file (`nmb3_decision_policy.md`,
  `nmb3_autonomous_loop_policy.md`, `nmb3_manifesto.md`,
  `nmb3_roles.md`, etc).
- Editing MILESTONES.md, the M3.1 archive, the M3.1 closure
  recommendation, the P4 closure recommendation, the M6
  closure recommendation, the boundary document, the O023 /
  O033 / O034 interpreter outputs, the shared workflow yml,
  or any pipeline code.
- Editing `nmb3/nmb3_README.md` (Steve's rewrite did not
  carry the original "cross-link from README" requirement
  forward; adding a cross-link would require separate Steve
  authorisation).
- Re-running any CI workflow.
- Advancing any other objective (this block produces O037
  only; O038 will be considered in a separate block after
  O037 closes cleanly and architect review APPROVED).
- Auto-applying any "approval"; O037 SUCCEEDED is a loop
  status, not a Steve approval.  No § 9-style "Awaiting
  Steve" headers needed in the appendix (it is documentation,
  not a closure recommendation).
- Making any funding, commercial, perceptual-validity,
  second-corpus generalisation, or real-time-deployment
  claim.

Pass Criteria for this block (per O037 rewritten success criteria):
- `nmb3/nmb3_packaging/reproducibility_appendix.md` exists at
  the commit closing this block.
- Section A lists the three SHA-pinned reproductions with the
  six pinning fields each (head SHA, CI run id, exact
  command, workflow file, artefact name, headline number).
- Section B lists all 13 non-SHA-pinned milestones with
  "gap, not failure" labelling and a MILESTONES.md baseline
  pointer for each.
- Section C disclaims full-chain reproducibility, funding,
  commercial, and perceptual claims; states the broader
  CI-pinning campaign restriction.
- No un-pinned number appears in Section A.
- No gap is mis-labelled as a failure.
- No policy file, no MILESTONES.md, no nmb3_README.md
  edited.

Out of Scope (explicit non-claims):
- This block does NOT formally re-validate any milestone.
- This block does NOT claim full-chain reproducibility.
- This block does NOT propose, endorse, or hint at any fix
  for the M6.5 FAIL or any other negative result.
- This block does NOT advance O038 in this commit; O038
  will be executed in a separate block only if (a) O037
  closes cleanly here, (b) architect review APPROVED, (c)
  no new gate is triggered.
- This block does NOT advance O030 / O031 / O032 (M6.1 /
  M6.2 / M6.3 fresh CI re-validation), O039-O041 (other
  packaging artefacts), O042 (continuation-scope
  authorisation), or O043 (out-of-scope register).
- This block does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 /
  M5.x / M6.x closure.
- This block does NOT invalidate the P4 partial-scope
  closure or the M6 partial-scope closure.
- This block does NOT make any funding, commercial,
  perceptual-validity, second-corpus generalisation, or
  real-time-deployment claim.
