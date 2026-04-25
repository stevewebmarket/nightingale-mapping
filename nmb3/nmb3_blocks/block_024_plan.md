Block ID:
block_024

Current Milestone:
Boundary documentation -- not a measurement milestone.  This
block produces a single boundary-of-scope reference document
that consolidates the locked-pipeline "good case" / "what does
not yet work" boundary as recorded in MILESTONES.md "Current
boundary" section, with a SHA-pinned cross-reference to the
M6.4 PASS evidence (O033 SUCCEEDED) and the M6.5 FAIL evidence
(O034 SUCCEEDED).  This block does NOT advance any pipeline,
re-run any milestone, or modify any locked metric.

Approval Status:
STEVE-APPROVED via the chat string "Execute O035" issued at
approximately 2026-04-25T18:55Z (recorded verbatim in
`nmb3/nmb3_decisions.log` for this block).  This is a clean
authorisation -- O035's declared dependency (O034) was satisfied
at 2026-04-25T18:45:00Z (canonical SHA cf165f4 / 5190b05) by
the SUCCEEDED M6.5 multi-family FAIL re-validation; no waiver
was required.

The objective is approved with explicit forbidden-action
discipline: O035 prohibits softening boundary language (e.g.
restating "what does not yet work" as "what works partially")
and prohibits suggesting out-of-scope fixes (e.g. CREPE,
voice-friendly extractor) anywhere except the explicit
"out of scope" register that lives under O043.  The CREPE
mention that already appears in the verbatim MILESTONES.md
"Current boundary" passage is permitted (because the success
criterion requires the passage to be quoted exactly, byte-for-
byte); the forbidden action is *adding* new fix-recommendation
language outside the verbatim quote.

One Question to Answer:
Does `nmb3/nmb3_reports/boundary.md` exist and quote
MILESTONES.md "Current boundary" section in a form that is
mechanically checksum-equal to the canonical source bytes
(SHA256 of `sed -n '40,53p' MILESTONES.md` at canonical SHA
cf165f4 = `a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc`),
points at the SUCCEEDED O033 (M6.4 PASS) and O034 (M6.5 FAIL)
evidence by canonical SHA + CI run id, lists what is and is
not within the locked pipeline's good case **without softening
the boundary language**, and adds **no new fix-recommendation
language** outside the verbatim quote?

Why This Matters:
The boundary document is the funder-facing single point of
reference for what the locked NMB3 pipeline does and does not
demonstrate.  Three properties matter:

  - **Quote integrity.**  An external reviewer must be able to
    run `sed -n '40,53p' MILESTONES.md | sha256sum` at canonical
    SHA cf165f4 and get the exact SHA256 the boundary document
    cites.  Any whitespace or wording drift in the quote would
    break the audit trail and let language drift in over time.
  - **Evidence reachability.**  The boundary document must
    point at the specific CI run ids and canonical SHAs that
    produced the M6.4 PASS and M6.5 FAIL evidence (O033 run
    24937477484 at SHA 3929fbc; O034 run 24937928571 at SHA
    9eaabac).  An external reviewer must be able to fetch
    those artefacts (each under 90-day retention) and verify
    the per-cell + per-condition reproduction.
  - **Honesty discipline.**  The boundary is a NEGATIVE
    boundary (M6.5 FAIL is part of the locked result).  The
    funder-facing document must record this without softening
    -- e.g. without restating M6.5 as "an open issue" or
    "scheduled improvement", and without proposing any specific
    fix outside the dedicated O043 register.

Allowed Actions:
- Write `nmb3/nmb3_reports/boundary.md` containing:
    (a) the verbatim MILESTONES.md "Current boundary" passage
        (lines 40-53 at canonical SHA cf165f4) inside a fenced
        code block, plus its SHA256 and the exact reproduction
        command;
    (b) a "what works (locked-pipeline good case)" subsection
        cross-referencing O033 (M6.4 family-retrieval PASS) by
        canonical SHA + CI run id + interpreter output path;
    (c) a "what does not yet work (locked-pipeline boundary)"
        subsection cross-referencing O034 (M6.5 multi-family
        FAIL) by canonical SHA + CI run id + interpreter
        output path;
    (d) explicit non-claim register pointing readers at O043
        for any fix discussion;
    (e) explicit pointer to the M5.7 (NEGATIVE), M5.8
        (NEGATIVE), and M5.9 (ABANDONED) ablations to make
        clear the boundary has already been probed at the
        front-end level within the locked work.
- Write this Block 024 plan.
- Update `nmb3/nmb3_objective_map.md` to flip O035
  PROPOSED -> SUCCEEDED with the standard expanded Status
  entry referencing the new boundary file.
- Append the standard Steve-string + interpretation entry to
  `nmb3/nmb3_decisions.log`.
- Commit and push under nightingalemap/info@webmarket.ie.

Forbidden Actions (per O035 spec, plus this block's discipline):
- Softening boundary language.  Specifically: do not restate
  "what does not yet work" as "what works partially" or "what
  is still in development".  Do not minimise the M6.5 FAIL
  by surrounding it with hedges.  Do not characterise the
  boundary as anything other than a NEGATIVE boundary.
- Suggesting out-of-scope fixes (CREPE, voice-friendly
  extractor, second-corpus generalisation, perceptual-validity
  studies, real-time deployment, commercial productisation)
  anywhere outside the verbatim quote.  Such discussion belongs
  in O043's `nmb3/nmb3_packaging/scope_and_out_of_scope.md` if
  and when O042 (Steve-only continuation-scope authorisation)
  triggers it.  The CREPE mention in the verbatim quote is
  permitted (because the success criterion requires the
  quote to be byte-equal).
- Editing MILESTONES.md, the M3.1 archive, the M3.1 closure
  recommendation, the P4 closure recommendation, the O033 /
  O034 interpreter outputs, the shared workflow yml, or any
  pipeline code.
- Re-running any CI workflow (this objective is documentation
  only; no new CI evidence is produced or needed).
- Advancing any other objective.  Specifically: this block does
  not advance O036 (M6 phase closure recommendation), O037
  (reproducibility appendix), or O042 / O043 (continuation-
  scope objectives).
- Quoting any other MILESTONES.md section verbatim that is
  not the "Current boundary" section (the quote-byte-equality
  property is asserted only for that section in O035's spec).
- Promising any specific continuation outcome.

Pass Criteria for this block (per O035 success criteria):
- `nmb3/nmb3_reports/boundary.md` exists at the commit closing
  this block.
- The verbatim quote inside `boundary.md` is mechanically
  byte-equal to `sed -n '40,53p' MILESTONES.md` at canonical
  SHA cf165f4.  Verifier-facing reproduction command and
  expected SHA256 are embedded in the document.
- The document points at O033 evidence (CI run id 24937477484
  at SHA 3929fbc) for the "what works" side and O034 evidence
  (CI run id 24937928571 at SHA 9eaabac) for the "what does
  not yet work" side.
- No softening language is introduced.  No fix-recommendation
  language is added outside the verbatim quote.
- The non-claim register in the document explicitly points
  out-of-scope fix discussion to O043.

Out of Scope (explicit non-claims):
- This block does NOT diagnose or propose a fix for the M6.5
  FAIL.  Any such proposal is O043 (continuation work) with
  O042 as its predecessor.
- This block does NOT formally re-validate any milestone.
- This block does NOT advance O036 (M6 phase closure
  recommendation), O037 (reproducibility appendix), or any
  P9 (continuation-scope) objective.
- This block does NOT extend M6.5's claim, soften M6.5's FAIL
  label, or restate any condition.
- This block does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 /
  M5.x / M6.4 closure.
- This block does NOT invalidate the P4 partial-scope closure
  approved at 2026-04-25T17:59:01Z.
- This block does NOT make any funding, commercial,
  perceptual-validity, second-corpus generalisation, or
  real-time-deployment claim.
