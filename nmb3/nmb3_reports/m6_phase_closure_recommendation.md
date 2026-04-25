# M6 Phase Closure Recommendation — partial-scope, anchored on O033 / O034 / O035

Generated:    2026-04-25T19:14:00Z
Author:       NMB3 autonomous loop, executing objective O036 under
              Steve's authorisation string "Execute O036" (see
              `nmb3/nmb3_decisions.log`, 2026-04-25T19:10:00Z entry).
Audience:     Steve.
Status:       **Awaiting Steve.**  This recommendation is in
              draft until Steve replies with an explicit
              approval string in chat (matching the O024 P4
              partial-scope closure approval pattern, where the
              binding approval string was "Approve P4 partial-
              scope closure" at 2026-04-25T17:59:01Z).  Until
              that string is recorded in `nmb3/nmb3_decisions.log`
              and reflected in § 9 below, nothing in this
              recommendation is binding on the funding package.

---

## 1. Headline (required by O036 success criterion)

**M6.5 FAIL is part of the result, not a blocker for closure.**

The locked NMB3 retrieval pipeline demonstrates one good case
and one boundary, and **both must be cited together**: M6.4
family-retrieval PASS holds for the Twinkle family on a small
single-family library, AND M6.5 multi-family retrieval FAILs on
the same locked pipeline once a second family (Lamb) is added
to the library.  The M6.4 PASS and the M6.5 FAIL are two faces
of the same locked-pipeline result; closing M6 means closing
both, not closing M6.4 and leaving M6.5 open.

Both faces are SHA-pinned on canonical:

  - M6.4 PASS — re-validated under O033 SUCCEEDED at canonical
    SHA `9eaabac`, with CI run id `24937477484` at head SHA
    `3929fbc`, AND
  - M6.5 FAIL — re-validated under O034 SUCCEEDED at canonical
    SHA `cf165f4`, with CI run id `24937928571` at head SHA
    `9eaabac`, with bit-identical reproduction of all 18 cells
    of the M6.5 headline table and all 7 pre-set conditions
    versus MILESTONES.md.

The boundary that separates the M6.4 PASS from the M6.5 FAIL
is also documented under O035 SUCCEEDED at canonical SHA
`dd1b689` in `nmb3/nmb3_reports/boundary.md`, with a verbatim
byte-equal MILESTONES.md "Current boundary" quote.

## 2. Scope of this recommendation

O036's literal purpose is to "aggregate O030–O035 into a
Steve-facing recommendation that explicitly includes the M6.5
boundary as part of the closed result, not as an open issue
to be solved".  Of those six objectives:

  - **O030** (M6.1 re-validate pairwise structural similarity):
    NOT executed.  Status remains **PROPOSED** on canonical.
    M6.1's locked baseline (three pair scores: orchestra vs
    orchestra_pshift = 0.700, orchestra vs orchestra_tstretch =
    0.700, orchestra vs rock = 0.164 with "insufficient melodic
    content" verdict) carries the original MILESTONES.md record
    plus incidental score reproduction inside the O033 / O034
    leaderboards (every score in the M6.4 PASS leaderboard
    reproduces the M6.2 baseline, which itself rests on M6.1).
    No fresh CI re-validation under O030.
  - **O031** (M6.2 re-validate query-vs-library search): NOT
    executed.  Status remains **PROPOSED** on canonical.  M6.2's
    locked baseline (twinkle_box headline ranking
    twinkle_box_tstretch 0.479 → twinkle_harmonica 0.284 →
    unrelated tied at 0.164) carries the original MILESTONES.md
    record plus incidental score reproduction inside the O033 /
    O034 leaderboards.  No fresh CI re-validation under O031.
  - **O032** (M6.3 re-validate small-library retrieval): NOT
    executed.  Status remains **PROPOSED** on canonical.  M6.3's
    locked baseline (3/3-queries-PASS retrieval on the 9-clip
    library, with `twinkle_people` borderline label intact)
    carries the original MILESTONES.md record plus incidental
    leaderboard reproduction inside O033's M6.4 PASS run (the
    M6.4 family-retrieval result uses the same 9-clip library
    as M6.3, and the M6.4 leaderboard reproduces the M6.3
    leaderboard cell-for-cell where they overlap).  No fresh
    CI re-validation under O032.
  - **O033** (M6.4 re-validate Twinkle family-retrieval PASS):
    SUCCEEDED at canonical commit `59e21a9` (errata patch
    `9eaabac`).  M6.4 PASS reproduces verbatim with all four
    pre-set conditions PASS and all 18 cells of the headline
    table matching the locked baseline.  AND the same locked
    pipeline produces the M6.5 FAIL on the multi-family library
    (see O034 below).
  - **O034** (M6.5 re-validate the Lamb FAIL **as an honest
    FAIL**): SUCCEEDED at canonical commit `5190b05` (errata
    patch `cf165f4`).  M6.5 FAIL reproduces verbatim with all
    18 cells of the headline table and all 7 pre-set conditions
    matching the locked baseline; the explicit honesty floor
    (any reproduction *passing* M6.5 must trigger the Decision
    Policy "suspected metric gaming" early-stop) was checked
    and explicitly **NOT** triggered.
  - **O035** (Boundary documentation file): SUCCEEDED at
    canonical commit `dd1b689`.  `nmb3/nmb3_reports/boundary.md`
    quotes MILESTONES.md "Current boundary" verbatim with
    SHA256 byte-equality (`a6fc0d62...d2b28`) and cross-
    references both the M6.4 PASS and the M6.5 FAIL by canonical
    SHA + CI run id + interpreter output filename.

This recommendation is therefore the **partial-scope variant**
of M6 closure that this session can honestly produce: it
aggregates **O033, O034, and O035 only**, on the strength of
the same canonical activation rule that the P4 partial-scope
closure used (preferred-path objectives that succeed with zero
drift permit deferral of the off-path objectives).  The full M6
closure recommendation, aggregating all six objectives, remains
available as a future expansion — it would require Steve to
authorise O030 / O031 / O032 first.

## 3. Evidence base — O033, O034, O035 in detail

### 3.1 O033 (M6.4 family-retrieval PASS) AND its M6.5 boundary
        (O034)

The shared parameterised reproducibility workflow at
`.github/workflows/nmb3_no_cache_repro.yml` was dispatched
once against head SHA `3929fbc` with `target=m6_4` and
`script="python run_m6_4_family_retrieval.py"`:

  - **Run** — id `24937477484`, target `m6_4`.  Conclusion:
    success.  Artefact `nmb3-no-cache-repro-m6_4-24937477484`
    (90-day retention) with inner stdout
    `no_cache_repro_m6_4.txt`.
  - **Result:** all four pre-set M6.4 conditions PASS; all 12
    cells of the headline table reproduce verbatim
    (`twinkle_box` family hits 3/3 in top-3, outranks YES;
    `twinkle_harmonica` family hits 2/3 in top-3, outranks YES;
    `twinkle_people` family hits 1/3 in top-3, outranks NO and
    flagged weak-evidence); cond4 fires its outside-family
    "partial melodic match" WARNING on `polyphonic` (correctly
    flagged but does not outrank the family).  No per-family
    tuning, no scoring change, no extractor edit was applied.
    Interpreter output:
    `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md`.

The M6.4 PASS holds **on the M6.3 9-clip library** (Twinkle is
the only family in the library).  The same locked pipeline, when
the library is extended to 12 clips by adding three Lamb-family
clips, produces the M6.5 FAIL documented in § 3.2 — so the M6.4
PASS evidence above is bound to the M6.5 FAIL evidence below
and must be cited alongside it whenever either is cited.

### 3.2 O034 (M6.5 multi-family FAIL) AND its M6.4 baseline
        (O033)

The same shared parameterised workflow was dispatched once
against head SHA `9eaabac` with `target=m6_5` and
`script="python run_m6_5_multi_family.py"`:

  - **Run** — id `24937928571`, target `m6_5`.  Conclusion:
    success (the workflow conclusion; the script verdict is
    `M6.5 FAIL` as locked).  Artefact
    `nmb3-no-cache-repro-m6_5-24937928571` (90-day retention)
    with inner stdout `no_cache_repro_m6_5.txt`.
  - **Result:** all 18 cells of the headline table reproduce
    verbatim (`twinkle_box` 2/3/YES; `twinkle_harmonica` 1/2/NO;
    `twinkle_people` 1/1/NO weak; `lamb_solo` 0/1/NO weak;
    `lamb_group` 1/2/NO; `lamb_male` 0/1/NO weak); all 7 pre-
    set conditions reproduce (cond1 PASS; cond2 FAIL 1/3; cond3
    FAIL 0/3; cond4 FAIL on `polyphonic` "partial melodic match"
    WARNING firing 3 times; cond5 FAIL with bit-identical
    Twinkle regression arithmetic
    `(3,3,True,False)→(2,3,True,False)` and
    `(2,3,True,False)→(1,2,False,False)`; cond6 PASS; cond7
    EXTERNAL satisfied by this CI evidence); both family-level
    booleans report FAIL; final script line `M6.5 FAIL`.  The
    explicit honesty floor was checked and **NOT** triggered
    (M6.5 line is FAIL not PASS; only 3 of 7 conditions PASS;
    both family booleans FAIL).  No per-family tuning, no
    scoring change, no extractor edit was applied.  Interpreter
    output: `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md`.

The M6.5 FAIL holds **on the locked pipeline that produced the
M6.4 PASS** — same M5.6 extractor, same M6.1 similarity, same
M6.3 ranking.  The only change between the M6.4 PASS and the
M6.5 FAIL is the library composition (one family vs two).  This
is exactly why the M6.4 PASS and the M6.5 FAIL must be cited
together.

### 3.3 O035 (Boundary documentation) — bridges M6.4 PASS and
        M6.5 FAIL

`nmb3/nmb3_reports/boundary.md` at canonical commit `dd1b689`
contains the verbatim MILESTONES.md "Current boundary" passage
(lines 40-53 at SHA `cf165f4`, SHA256
`a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc`)
along with the verifier reproduction command
(`sed -n '40,53p' MILESTONES.md | sha256sum`) so an external
reviewer can mechanically verify byte-equality.  Boundary doc
section 2 cites the M6.4 PASS evidence; section 3 cites the
M6.5 FAIL evidence; section 5 routes all out-of-scope fix
discussion to O043; section 6 is a pointer-summary table cross-
referencing all five evidence locations.

### 3.4 Honest record of the M6.1 / M6.2 / M6.3 evidence
        position (O030 / O031 / O032 PROPOSED)

The closure recommendation rests on M6.4 PASS and M6.5 FAIL
**together** — that pair is the load-bearing evidence.  The
M6.1 / M6.2 / M6.3 baseline carries only its MILESTONES.md
record plus incidental score reproduction inside the O033
(M6.4) and O034 (M6.5) leaderboards.  In particular:

  - The M6.4 PASS leaderboard (and, on its M6.5 boundary
    side, the Twinkle rows of the M6.5 FAIL leaderboard --
    M6.5 extends M6.4's library with Lamb-family clips, so
    Twinkle scores carry through cell-for-cell) reproduces
    every M6.2 score (`twinkle_box_tstretch` 0.479,
    `twinkle_harmonica` 0.284, unrelated clips tied at
    0.164) cell-for-cell.  This is incidental observational
    evidence that M6.1 (which produces the underlying pair
    scores) and M6.2 (which produces the headline rankings)
    reproduce on this fresh canonical SHA.
  - The M6.4 PASS leaderboard also reproduces the M6.3 9-clip
    library leaderboard cell-for-cell where they overlap.
    Same incidental observational reproduction, not formal
    re-validation.

This is not equivalent to the formal CI re-validation that
O030 / O031 / O032 would provide, and the closure
recommendation does not claim that it is.  The funder-facing
truth is: **the M6 retrieval-pipeline claim is anchored by
M6.4 PASS + M6.5 FAIL together, with M6.1 / M6.2 / M6.3 as
the documented input layers whose locked baselines are
incidentally reproduced inside the M6.4 / M6.5 leaderboards**.
A future-expansion full-scope M6 closure that adds formal
fresh CI evidence for M6.1 / M6.2 / M6.3 (via O030 / O031 /
O032) is available if Steve later authorises it.

## 4. Governance note — P6 entry approval (O029) and the per-
   objective Steve-string pattern this session used

O029 (P6 entry approval) is **PROPOSED** on canonical.  The M6
work that produced O033 / O034 / O035 SUCCEEDED in this session
proceeded on a per-objective Steve-string basis without an
explicit P6 phase entry approval:

  - O033 was authorised at 2026-04-25T18:00Z by the explicit
    waiver string "Override deps for O033 (single-objective
    waiver)" -- a stronger gate than a phase entry, since it
    is per-objective and explicitly notes the waived
    dependencies.
  - O034 was authorised at 2026-04-25T18:30Z by the clean
    string "Execute O034" against an unwaived satisfied
    dependency (O033).
  - O035 was authorised at 2026-04-25T18:55Z by the clean
    string "Execute O035" against an unwaived satisfied
    dependency (O034).

This is a **more conservative** governance posture than a
single P6 phase entry would have been: each objective is
individually authorised, and each authorisation is recorded
verbatim in `nmb3/nmb3_decisions.log`.  No M6 work proceeded
without an explicit per-objective Steve string.  The closure
recommendation does not retro-actively claim P6 phase entry,
nor does it require it; the per-objective string trail is
the binding governance trail.

## 5. Recommendation (binding once approved)

The autonomous loop recommends that Steve approve M6 closure
on the partial-scope basis defined in § 2 by replying to
this recommendation with an explicit approval string (matching
the O024 P4 partial-scope closure approval pattern; suggested
string: "Approve M6 partial-scope closure").

If Steve approves, the following items become binding for
funding-package purposes:

  1. **Treat M6.4 PASS + M6.5 FAIL as the load-bearing M6
     result**, with the understanding that the M6.4 PASS
     describes the locked pipeline's good case (Twinkle
     family, single-family library) AND the M6.5 FAIL
     describes the locked pipeline's boundary (Lamb +
     Twinkle, multi-family library), and that the two must
     always be cited together.
  2. **Treat the M6.5 FAIL as part of the result, not a
     blocker for closure** -- that is, M6.5 FAIL is not an
     open issue, scheduled improvement, work in progress, or
     "next steps"; it is what the locked pipeline
     demonstrably does on multi-family material with
     fewer than ~4 non-trivial intervals per clip, and the
     closure approves that demonstrably.
  3. **Cite M6.4 by run id `24937477484` at SHA `3929fbc`,
     and M6.5 by run id `24937928571` at SHA `9eaabac`,**
     for any external reviewer who needs to verify the
     reproduction.
  4. **Treat O030 / O031 / O032 (M6.1 / M6.2 / M6.3 fresh
     CI re-validation) as deferred, not skipped or failed.**
     The M6.1 / M6.2 / M6.3 baselines are incidentally
     reproduced inside the M6.4 PASS and M6.5 FAIL
     leaderboards; a future-expansion full-scope M6 closure
     can add formal CI evidence for them via O030 / O031 /
     O032 if Steve later authorises them.
  5. **Keep `nmb3/nmb3_reports/boundary.md` as the canonical
     boundary reference**, with its verbatim MILESTONES.md
     "Current boundary" quote and SHA256 pinning, and route
     all out-of-scope fix discussion through O043 (which
     itself depends on O042 -- continuation-scope
     authorisation).
  6. **Continue using the shared no-cache reproducibility
     workflow** at `.github/workflows/nmb3_no_cache_repro.yml`
     in its current target-agnostic shape (the same workflow
     that O023, O033, and O034 used) as the canonical M6
     reproduction surface.

The M6.4 PASS and the M6.5 FAIL — taken together — are the
M6 result.  Approving M6 closure means approving both faces
of that result.

## 6. Risk assessment

| Risk | Status | Notes |
|---|---|---|
| M6.4 PASS cited out of context (without M6.5 boundary) | Closure governance addresses this | Recommendation item 1 binds the co-citation requirement; boundary doc § 2/3 also enforces co-location; this entire recommendation co-locates M6.4 PASS and M6.5 FAIL in every paragraph that mentions either. |
| M6.5 FAIL re-framed as "open issue" or "scheduled improvement" | Closure governance addresses this | Recommendation item 2 binds the headline phrase "M6.5 FAIL is part of the result, not a blocker for closure"; § 1 puts that phrase load-bearing. |
| Aggregation drift (claiming O030/O031/O032 are SUCCEEDED when they are PROPOSED) | None — explicitly avoided | § 2 enumerates all six objectives by current canonical status; § 3.4 explicitly distinguishes incidental observational reproduction from formal re-validation. |
| Out-of-scope fix recommendation bleeding into the closure document | None — § 7 disclaims, routes to O043 | The CREPE / pyin / HPSS / voice-friendly extractor / second-corpus / perceptual / commercial / real-time topics do not appear in this document except as out-of-scope pointers. |
| Auto-applied approval (closure binding without Steve's explicit string) | None — header status is "Awaiting Steve" | Matches the P4 partial-scope closure pattern; § 9 is the post-approval errata target. |

## 7. Non-claim register

This recommendation does NOT make, endorse, or hint at any of
the following claims; each would require its own Steve gate
and its own objective:

  - It does NOT propose, endorse, or hint at any fix for the
    M6.5 FAIL.  Fix discussion belongs in O043 (continuation-
    scope out-of-scope register), which itself depends on
    O042 (Steve-only continuation-scope authorisation).
    Until then, the boundary is the result.
  - It does NOT advance O030 (M6.1 fresh CI re-validation),
    O031 (M6.2), O032 (M6.3), O037 (reproducibility appendix),
    O038-O041 (packaging artefacts), O042 (continuation-scope
    authorisation), or O043 (out-of-scope register).
  - It does NOT formally re-validate M6.1 / M6.2 / M6.3 in
    their own right.  The incidental score reproduction
    inside the O033 / O034 leaderboards is observational
    evidence, not a formal re-validation claim.
  - It does NOT extend M6.5's claim beyond the canonical
    12-clip library + 6-query set (3 Twinkle + 3 Lamb) that
    the M6.5 script operates on.
  - It does NOT soften M6.5's FAIL label.  M6.5 is FAIL,
    and the closure approves that.
  - It does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 / M5.x or
    M6.4 closure.
  - It does NOT invalidate the P4 partial-scope closure
    approved by Steve at 2026-04-25T17:59:01Z.  P4 closure
    remains binding.
  - It does NOT auto-apply any approval; it is a draft until
    Steve replies with an explicit approval string in chat.
  - It does NOT make any funding, commercial, perceptual-
    validity, second-corpus generalisation, or real-time-
    deployment claim.

## 8. Future-expansion path preserved

Nothing in this recommendation forecloses a future full-scope
M6 closure.  If Steve later authorises and succeeds O030
(M6.1) / O031 (M6.2) / O032 (M6.3), the partial-scope
recommendation in this document can be superseded by a full-
scope `m6_phase_closure_recommendation_v2.md` that aggregates
all six O030-O035 objectives with formal fresh CI evidence
for every M6 milestone.  The current recommendation is the
honest snapshot of what the loop can aggregate from canonical
right now.

## 9. Approval record (to be added post-approval)

  - **Approver:**  _Steve._
  - **Approval string (verbatim):**  _Awaiting._
  - **Approval timestamp:**  _Awaiting._
  - **Channel:**  Chat reply to the loop's O036 SUCCEEDED
    summary.
  - **Effect (post-approval):**  This recommendation will
    become binding for funding-package purposes on the
    partial-scope basis defined in § 2.  The six binding
    items in § 5 will then be in force.
  - **Future-expansion path preserved:**  See § 8.
  - **Cross-references (post-approval):**  to be filled in
    against:
      - O036 in `nmb3/nmb3_objective_map.md` (Status entry
        will be updated to reflect the binding approval).
      - `nmb3/nmb3_decisions.log`, post-approval entry
        (Steve's verbatim approval string).
      - O033 / O034 / O035 evidence in
        `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md`,
        `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md`,
        `nmb3/nmb3_reports/boundary.md`.
      - Workflow file `.github/workflows/nmb3_no_cache_repro.yml`
        (the canonical reproduction surface this approval
        keeps in its current target-agnostic shape).
