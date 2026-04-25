Block ID:
block_025

Current Milestone:
M6 phase closure recommendation -- not a measurement milestone.
This block produces the Steve-facing closure recommendation
that aggregates the M6 work demonstrably present on canonical
into a single recommendation document, with the M6.5 FAIL
boundary co-located with the M6.4 PASS in every place either
is mentioned, and the canonical "M6.5 FAIL is part of the
result, not a blocker for closure" phrasing recorded verbatim.

This block does NOT advance any pipeline, re-run any milestone,
or modify any locked metric.  It does NOT formally re-validate
M6.1, M6.2, or M6.3 (those are O030 / O031 / O032, all of
which remain PROPOSED on canonical).

Approval Status:
STEVE-APPROVED via the chat string "Execute O036" issued at
approximately 2026-04-25T19:10Z (recorded verbatim in
`nmb3/nmb3_decisions.log` for this block).  This is a clean
authorisation against O036's literal Dependencies clause:
O035 is SATISFIED at canonical SHA dd1b689 (SUCCEEDED at
2026-04-25T18:58:00Z).  No waiver is required against the
literal dependency.

The objective is approved with explicit forbidden-action
discipline: O036 prohibits presenting M6.4 PASS without the
M6.5 boundary in the same paragraph, and (per the success
criterion) requires the recommendation to explicitly state
"M6.5 FAIL is part of the result, not a blocker for closure".

One Question to Answer:
Does `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`
exist, aggregate the M6 work demonstrably present on canonical
(O033 SUCCEEDED, O034 SUCCEEDED, O035 SUCCEEDED -- and the
asymmetric note that O030 / O031 / O032 remain PROPOSED, with
the M6.1 / M6.2 / M6.3 baseline carrying only its MILESTONES.md
record plus incidental score reproduction inside the O033 and
O034 leaderboards), explicitly state "M6.5 FAIL is part of the
result, not a blocker for closure", and never present M6.4 PASS
without the M6.5 boundary in the same paragraph?

Why This Matters:
The M6 phase closure recommendation is the Steve-facing
artefact that fixes the locked-pipeline retrieval claim for
the funding package.  Three properties matter:

  - **Boundary co-location.**  A funder reading any single
    paragraph that mentions M6.4 PASS must also see the M6.5
    FAIL boundary in that same paragraph -- otherwise the
    PASS could be cited out of context as a stronger result
    than the locked work demonstrates.
  - **Required phrasing.**  The success criterion requires
    the verbatim phrase "M6.5 FAIL is part of the result,
    not a blocker for closure".  This phrasing is the
    operative governance statement that the recommendation
    asks Steve to bind: M6.5 FAIL is not an open issue
    awaiting fix, it is part of what the locked pipeline
    demonstrates and what closure approves.
  - **Aggregation honesty.**  O036's purpose names "O030-
    O035" as the aggregation set, but O030 / O031 / O032
    are PROPOSED on canonical (M6.1 / M6.2 / M6.3 have not
    received fresh CI re-validation; only their MILESTONES.md
    baseline + incidental observational reproduction inside
    O033 / O034 leaderboards exist).  The closure
    recommendation must record this asymmetry honestly,
    matching the pattern set by the O024 P4 partial-scope
    closure recommendation (which aggregated only O023 and
    explicitly recorded O020 / O021 / O022 as PROPOSED).

Allowed Actions:
- Write `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`
  containing:
    (a) headline restating M6.4 family-retrieval PASS and
        M6.5 multi-family FAIL together;
    (b) explicit scope record of which O030-O035 objectives
        are SUCCEEDED (O033, O034, O035) and which remain
        PROPOSED (O030, O031, O032), with the same partial-
        scope governance note the P4 closure used;
    (c) per-objective evidence pinning for the SUCCEEDED
        items (canonical SHA, CI run id where applicable,
        interpreter output filename, CI artefact name);
    (d) honest record of the M6.1 / M6.2 / M6.3 evidence
        position (MILESTONES.md baseline + incidental score
        reproduction inside O033 / O034 leaderboards, NOT
        fresh CI re-validation);
    (e) the verbatim required phrase "M6.5 FAIL is part of
        the result, not a blocker for closure";
    (f) the boundary co-location discipline applied
        consistently throughout (every mention of M6.4 PASS
        co-located with M6.5 FAIL in the same paragraph);
    (g) explicit non-claim register (no fix proposed for
        M6.5; no funding / commercial / perceptual claim;
        out-of-scope fix discussion routed to O043; future-
        expansion path to a full-scope M6 closure preserved
        if Steve later authorises and succeeds O030 / O031
        / O032);
    (h) governance note that O029 (P6 entry approval) is
        PROPOSED on canonical and that the M6 work this
        session proceeded on a per-objective Steve-string
        basis without an explicit P6 phase entry -- this
        is a more conservative governance posture (each
        objective individually authorised) than a single
        phase entry would have been;
    (i) approval-status placeholder header (initially
        "Awaiting Steve") matching the P4 closure pattern,
        so a post-approval errata commit can replace it
        with the binding approval string + timestamp.
- Write this Block 025 plan.
- Update `nmb3/nmb3_objective_map.md` to flip O036
  PROPOSED -> SUCCEEDED with the standard expanded Status
  entry referencing the new closure recommendation file.
- Append the standard Steve-string + interpretation entry to
  `nmb3/nmb3_decisions.log`.
- Commit and push under nightingalemap/info@webmarket.ie.

Forbidden Actions (per O036 spec, plus this block's discipline):
- Presenting M6.4 PASS without the M6.5 boundary in the same
  paragraph.  Every paragraph that mentions M6.4 PASS must
  also reference M6.5 FAIL (or the boundary).  This applies
  to the headline, the scope section, the evidence base, and
  every section that mentions M6.4.
- Restating M6.5 FAIL as "an open issue", "scheduled
  improvement", "next steps", "work in progress", "partial
  pass", or any other softening.  M6.5 FAIL is part of the
  closed result.
- Proposing, endorsing, or hinting at any fix for M6.5
  (CREPE, voice-friendly extractor, pyin re-revisit, HPSS
  re-revisit, second-corpus generalisation).  Such discussion
  belongs in O043, which itself depends on O042 (Steve-only
  continuation-scope authorisation).
- Implying that the M6.1 / M6.2 / M6.3 baseline has been
  freshly re-validated by CI in this session.  It has not.
  The recommendation must accurately distinguish baseline-
  evidence-only from fresh-CI-evidence milestones.
- Editing MILESTONES.md, the M3.1 archive, the M3.1 closure
  recommendation, the P4 partial-scope closure recommendation,
  the boundary document just written under O035, the O033 /
  O034 interpreter outputs, the shared workflow yml, or any
  pipeline code.
- Re-running any CI workflow (this objective is documentation
  only).
- Advancing any other objective.  Specifically: this block
  does NOT advance O030 / O031 / O032 (M6.1 / M6.2 / M6.3
  fresh re-validation), O037 (reproducibility appendix),
  O042 (continuation-scope authorisation), or O043 (out-of-
  scope register).
- Auto-applying the binding approval; this recommendation,
  once written, is "Awaiting Steve" until Steve issues an
  explicit approval string in chat (matching the O024 P4
  partial-scope closure approval pattern).

Pass Criteria for this block (per O036 success criteria):
- `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`
  exists at the commit closing this block.
- The document contains the verbatim phrase "M6.5 FAIL is
  part of the result, not a blocker for closure" at least
  once, in a section heading or load-bearing sentence (not
  in a footnote).
- Boundary co-location discipline holds throughout: every
  paragraph mentioning M6.4 PASS also references M6.5 FAIL
  or the boundary.
- The asymmetric scope (O033 / O034 / O035 SUCCEEDED, O030 /
  O031 / O032 PROPOSED) is explicitly recorded.
- Per-objective evidence pinning is present for each
  SUCCEEDED objective (canonical SHA, CI run id where
  applicable, interpreter output filename, artefact name).
- The non-claim register routes all out-of-scope fix
  discussion to O043 and explicitly disclaims funding /
  commercial / perceptual / second-corpus claims.

Out of Scope (explicit non-claims):
- This block does NOT diagnose or propose a fix for the M6.5
  FAIL.
- This block does NOT formally re-validate any milestone.
  M6.1 / M6.2 / M6.3 baseline carries only its MILESTONES.md
  record plus incidental score reproduction inside O033 /
  O034 leaderboards.
- This block does NOT advance O030 / O031 / O032 / O037 /
  O038-O041 / O042 / O043 in any way.
- This block does NOT extend M6.5's claim, soften M6.5's FAIL
  label, or restate any pre-set condition.
- This block does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 /
  M5.x / M6.4 closure.
- This block does NOT invalidate the P4 partial-scope closure
  approved at 2026-04-25T17:59:01Z.
- This block does NOT auto-apply the M6 closure approval.
  The recommendation is "Awaiting Steve" until Steve issues
  an explicit approval string in chat.
- This block does NOT make any funding, commercial,
  perceptual-validity, second-corpus generalisation, or
  real-time-deployment claim.
