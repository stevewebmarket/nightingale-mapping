Block ID:
block_023

Current Milestone:
M6.5 — multi-family retrieval validation
(`run_m6_5_multi_family.py`).  Locked NEGATIVE result in
MILESTONES.md ("M6.5 result: FAIL" with 4 of 7 pre-set
conditions failing) at the M5.6 extractor SHA d332f54.  This
block does NOT introduce a new milestone or modify the locked
metric; it re-validates the existing locked FAIL on a fresh
clone with no caches, with explicit honesty discipline.

Approval Status:
STEVE-APPROVED via the chat string "Execute O034" issued at
approximately 2026-04-25T18:30Z (recorded verbatim in
`nmb3/nmb3_decisions.log` for this block).  This is a clean
authorisation — O034's declared dependency (O033) was satisfied
at 2026-04-25T18:21:00Z (canonical SHA 9eaabac) by the SUCCEEDED
M6.4 reproduction; no waiver was required this time.

The objective is approved with a non-bypassable honesty floor
written into O034's "Auto-execute permission" clause: the loop
may execute this objective only because the FAIL is the locked,
declared result.  Any reproduction that *passes* M6.5 must
trigger the Decision Policy "suspected metric gaming" early-stop
and be reported to Steve before any further action.  This block
binds itself to that floor (see "Honesty Floor" section below).

One Question to Answer:
Does the locked M6.5 multi-family retrieval FAIL reproduce on a
fresh clone with no caches, including all six query rows of the
headline table, the per-condition results (4 of 7 PASS, 3 of 7
FAIL), the explicit FAIL verdict, and — most importantly — the
specific failure modes documented in MILESTONES.md (`polyphonic`
repeatedly tagged "partial melodic match"; Twinkle top-3 hits
regress when Lamb clips occupy higher ranks; family-2 hits in
top-3 < 2 of 3; best family-2 outranks-all-other = 0 of 3)?

Why This Matters:
M6.5 is the **boundary-defining negative** for the funding
package.  It says: M6.4's family-retrieval PASS is the locked
pipeline's good case, not its general case; on a second melody
(Mary Had a Little Lamb, three timbres) recorded under similar
conditions, the same locked extractor + similarity + ranking
chain fails to separate family from non-family.  The FAIL is
recorded honestly so the package does not over-claim general
melodic retrieval capability.

Re-validation matters because:

  - The M6.4 PASS depends on the same M5.6 extractor + M6.1
    similarity + M6.3 ranking chain that M6.5 fails on.  If
    M6.5 silently flipped to PASS on a fresh clone, the most
    likely cause would be a regression in one of those layers
    (or a metric-gaming change).  Either possibility must
    trigger the honesty-floor early-stop.
  - The 4 specific FAIL conditions (cond2 family-2 top-3 hits;
    cond3 family-2 outranks; cond4 outside-family clip
    "partial melodic match"; cond5 Twinkle behaviour regresses
    when Lamb clips compete) document the precise failure
    modes.  Each must reproduce as a FAIL with the same
    arithmetic the MILESTONES.md table records.
  - The 3 specific PASS conditions (cond1 ≥ 2 queries from new
    family; cond6 weak-evidence honestly flagged; cond7 fresh-
    clone reproducible) are the honesty-discipline conditions
    rather than the substantive retrieval-quality conditions.
    They must remain PASS.

Allowed Actions:
- Dispatch `run_m6_5_multi_family.py` exactly as written on
  canonical (no edits to the script; no per-family tuning; no
  scoring changes; no extractor changes).
- Use the shared no-cache reproducibility workflow at
  `.github/workflows/nmb3_no_cache_repro.yml` (already includes
  ffmpeg from O033's commit 3929fbc; no further workflow edits
  required for M6.5) with target=`m6_5`.
- Capture the run id and head SHA for pinning in the interpreter
  output.
- Compare the captured stdout line-by-line against the M6.5
  baseline in MILESTONES.md for: every cell of the 6-query x
  3-metric headline table; every condition of the 7-row
  pre-set conditions table (with the exact PASS/FAIL labels);
  the final `M6.5 FAIL` (or equivalent) verdict line.
- Make the explicit assertion in the interpreter output that no
  per-family tuning, scoring change, or extractor edit was
  applied (per O034's evidence-required clause).

Forbidden Actions (per O034 spec, plus this block's discipline):
- Editing `run_m6_5_multi_family.py`, `run_m6_4_family_retrieval.py`,
  `run_m6_3_retrieval.py`, `run_m6_1_similarity.py`,
  `run_milestones.py`, or any other pipeline file -- the dispatch
  must run the canonical scripts unmodified.
- Per-family tuning (changing thresholds, weights, MIN_NT,
  ranking semantics, or any other parameter in a way that
  improves M6.5's pass count).
- Scoring changes (modifying the M6.1 similarity formula or
  weights).
- Extractor edits (modifying the locked M5.6 extractor or any
  of its components).
- Downgrading the comparator from "outranks-all-other" to a
  weaker comparator (e.g. "outranks-all-non-family") to make
  cond3 look better.  M6.5 deliberately uses the stricter
  "outranks-all-other" comparator; that strictness is part of
  what the FAIL records.
- Restating cond5 to look better (e.g. quietly excluding
  twinkle_box / twinkle_harmonica regression because "the
  Twinkle PASS was already documented in M6.4").  Cond5 is
  exactly the regression check; restating it would erase the
  result it records.
- Removing the weak-evidence flag (a weak-evidence flag fired on
  twinkle_people in M6.4 reproduction; it should fire on the
  same query and on lamb_solo / lamb_male in M6.5 per the
  baseline).
- Caching any sample, library output, or pip dependency.
- Cherry-picking the run -- the first dispatch's result is the
  reproduction unless dispatch failed for infrastructure reasons
  (in which case the failure must be logged honestly and the
  retry's reasoning made explicit in decisions.log, exactly as
  was done for the O033 ffmpeg incident at 2026-04-25T18:18:54Z).
- Introducing M6.5-specific logic into the shared workflow yml
  (target-specific logic lives in the `script` input).
- Auto-committing the reproduction artefact (the workflow does
  not commit; artefacts are pinned by run id + SHA only).

Honesty Floor (non-bypassable, from O034's spec):
The script's verdict on a fresh clone must reproduce as FAIL.
Possible outcomes and required loop response:

  - **(a) FAIL with the same per-cell numbers as MILESTONES.md
        baseline:**  Expected outcome.  Block 023 succeeds.
        Write interpreter output, mark O034 SUCCEEDED, commit,
        surface to Steve.

  - **(b) FAIL but with different per-cell numbers (drift):**
        The FAIL verdict is preserved but the underlying
        numbers have moved.  Possible causes: backend-version
        drift (e.g. ffmpeg version differences on compressed
        audio), random-seed exposure (none expected; the
        pipeline is fully deterministic by design).  Write the
        drift findings into the interpreter output honestly,
        flag a follow-up investigation, and surface to Steve
        with the FAIL/drift mixed verdict.  Block 023 succeeds
        on the FAIL-preservation criterion but raises a quality
        flag on the drift.

  - **(c) PASS on a fresh clone (4-of-7 conditions flip to
        ≥4-of-7 PASS):**  Trigger the Decision Policy
        "suspected metric gaming" early-stop **immediately**.
        Stop before any commit.  Capture the full stdout, the
        run id, and the SHA.  Surface to Steve before any
        SUCCEEDED entry, any objective-map update, or any
        recommendation.  Do NOT mark O034 SUCCEEDED in this
        case — it would not be SUCCEEDED, it would be a
        critical investigation trigger.

Pass Criteria for this block (per O034 success criteria):
- 6-query headline table reproduces verbatim (all 18 cells
  match MILESTONES.md M6.5 table).
- Per-condition results reproduce: cond1 PASS, cond2 FAIL
  (1/3), cond3 FAIL (0/3), cond4 FAIL (`polyphonic` "partial
  melodic match" tag), cond5 FAIL (Twinkle regression in cell
  count; outranks flip), cond6 PASS (weak-evidence flagged),
  cond7 PASS (external).
- FAIL label preserved on the final verdict line.
- No condition silently re-weighted (the script's own
  pre-declared condition list is the binding list).
- Explicit assertion in the interpreter output that no per-
  family tuning, scoring change, or extractor edit was
  applied.

Out of Scope (explicit non-claims):
- This block does NOT diagnose the upstream pitch-tracker
  bottleneck (M5.7 / M5.8 / M5.9 territory; out-of-scope per
  the M6.5 honest interpretation in MILESTONES.md and per
  O043 "out of scope" register).
- This block does NOT propose a fix to M6.5 (that would be
  a different objective and would risk metric gaming).
- This block does NOT advance any other objective.
- This block does NOT touch policy files, MILESTONES.md, the
  M3.1 archive, the M3.1 closure recommendation, the P4
  closure recommendation, or any pipeline code.
- This block does NOT formally re-validate M6.1 / M6.2 / M6.3
  (incidental score reproduction inside the M6.5 leaderboard
  is observational only, just like inside O033's M6.4
  reproduction).
- This block does NOT advance O035 (boundary documentation),
  O036 (M6 phase closure recommendation), or O037
  (reproducibility appendix); each requires its own Steve
  string.
- This block does NOT declare M6.5 as PASS, partial PASS, or
  improved.  The FAIL label is the locked result; preserving
  it is the success criterion.
- This block does NOT make any funding, commercial, or
  perceptual-validity claim.
