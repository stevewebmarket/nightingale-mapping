# O034 Interpreter Output — M6.5 Multi-Family FAIL Re-validation

Generated:    2026-04-25T18:45:00Z
Objective:    O034 — M6.5 re-validate the Lamb FAIL **as an honest FAIL**
              (`nmb3/nmb3_objective_map.md`, P7 entry section)
Verdict:      **PASS — all 18 cells of the M6.5 headline table
              reproduce verbatim; all 7 pre-set conditions
              reproduce with the same PASS/FAIL pattern (cond1
              PASS, cond2 FAIL, cond3 FAIL, cond4 FAIL, cond5
              FAIL, cond6 PASS, cond7 EXTERNAL); FAIL label
              preserved on the final `M6.5 FAIL` line; no
              condition silently re-weighted.**

Honesty Floor: SATISFIED.  The script's verdict on a fresh
clone is FAIL with the same per-condition arithmetic
(4 of 7 FAIL) as the locked baseline.  The Decision Policy
"suspected metric gaming" early-stop did NOT trigger because
the FAIL was preserved exactly.  Had the verdict flipped to
PASS, this report would not exist; the loop would have stopped
before any commit and surfaced the anomaly to Steve.

Pinning:      Reproduction CI run id 24937928571 at head SHA
              **`9eaabacf5ae5640d329fa97ebe316486eaccd08f`**
              (the canonical SHA at the moment of dispatch).
              First-attempt success — no infrastructure failure
              this time (ffmpeg already installed in the shared
              workflow yml at canonical commit 3929fbc, which
              was the O033 fix; M6.5's lamb_*.mp3 samples decode
              cleanly through that backend).

---

## 1. Steve gating

  - **"Execute O034"** issued at approximately 2026-04-25T18:30Z.
    Recorded verbatim in `nmb3/nmb3_decisions.log`.

This was a clean authorisation: O034's declared dependency was
O033, which was already SUCCEEDED at canonical SHA 9eaabac at
2026-04-25T18:21:00Z.  No waiver was required.

The objective's "Auto-execute permission" clause includes a
non-bypassable honesty floor: "any reproduction that *passes*
M6.5 must trigger the Decision Policy 'suspected metric gaming'
early-stop and be reported to Steve before any further action."
That floor is binding throughout this report; § 4 records that
it was not triggered (because FAIL reproduced exactly).

## 2. What was reproduced and how

The locked M6.5 multi-family retrieval FAIL — recorded in
MILESTONES.md M6.5 section — was reproduced on a clean
ubuntu-latest CI runner with no caches, using the shared
parameterised reproducibility workflow at
`.github/workflows/nmb3_no_cache_repro.yml` (created under O023,
extended with target-agnostic ffmpeg under O033 at canonical
commit 3929fbc).

Dispatch:

  - **target:**  `m6_5`
  - **script:**  `python run_m6_5_multi_family.py`
  - **head SHA:**  `9eaabacf5ae5640d329fa97ebe316486eaccd08f`
  - **CI run id:**  24937928571
  - **artefact:**  `nmb3-no-cache-repro-m6_5-24937928571` (90-day
    retention); inner stdout file:  `no_cache_repro_m6_5.txt`
  - **dispatched against:**  `.github/workflows/nmb3_no_cache_repro.yml`

The script ran unmodified on canonical (no edits to
`run_m6_5_multi_family.py`, `run_m6_4_family_retrieval.py`,
`run_m6_3_retrieval.py`, `run_m6_1_similarity.py`,
`run_milestones.py`, or any other pipeline file).  No edit was
made to the shared workflow yml in this objective's scope (the
ffmpeg install was already in place from O033 and benefits any
target using compressed audio without introducing target-
specific logic).

## 3. Success criteria — point-by-point (per O034 spec)

### 3.1 6-query headline table reproduces verbatim

| Query | Family | top3 (canon) | top3 (repro) | top5 (canon) | top5 (repro) | outranks (canon) | outranks (repro) | weak (canon) | weak (repro) |
|---|---|---|---|---|---|---|---|---|---|
| `twinkle_box`        | F1 | 2 | 2 ✅ | 3 | 3 ✅ | YES | YES ✅ | — | — ✅ |
| `twinkle_harmonica`  | F1 | 1 | 1 ✅ | 2 | 2 ✅ | NO  | NO  ✅ | — | — ✅ |
| `twinkle_people`     | F1 | 1 | 1 ✅ | 1 | 1 ✅ | NO  | NO  ✅ | weak | weak ✅ |
| `lamb_solo`          | F2 | 0 | 0 ✅ | 1 | 1 ✅ | NO  | NO  ✅ | weak | weak ✅ |
| `lamb_group`         | F2 | 1 | 1 ✅ | 2 | 2 ✅ | NO  | NO  ✅ | — | — ✅ |
| `lamb_male`          | F2 | 0 | 0 ✅ | 1 | 1 ✅ | NO  | NO  ✅ | weak | weak ✅ |

**PASS.**  All 18 cells of the 6-query × 3-metric headline grid
reproduce, plus the 6 weak-evidence flags (3 weak / 3 not weak)
match exactly.

### 3.2 Per-condition results reproduce

| # | Condition | Canonical | Reproduction |
|---|---|---|---|
| 1 | `>= 2 queries from the new family` | PASS | PASS ✅ |
| 2 | `family-2 hit in top 3 for >= 2 queries` | FAIL (1/3) | FAIL (1/3) ✅ |
| 3 | `best family-2 outranks all-other for >= 2 queries` | FAIL (0/3) | FAIL (0/3) ✅ |
| 4 | `no outside-family clip labelled a strong / partial match` | FAIL (`polyphonic` repeatedly tagged "partial melodic match") | FAIL (`polyphonic` flagged with WARNING in 3 queries: twinkle_box score 0.160, twinkle_harmonica score 0.160, lamb_group score 0.429) ✅ |
| 5 | `Twinkle behaviour does not regress` | FAIL (twinkle_box top-3 3→2, twinkle_harmonica top-3 2→1, twinkle_harmonica `outranks` flips YES→NO) | FAIL (script self-reports `expected (3, 3, True, False), got (2, 3, True, False)` for twinkle_box; `expected (2, 3, True, False), got (1, 2, False, False)` for twinkle_harmonica) ✅ |
| 6 | `weak-evidence cases honestly flagged` | PASS | PASS ✅ (twinkle_people / lamb_solo / lamb_male all carry the weak-evidence tag with their non-trivial interval counts) |
| 7 | `fresh-clone reproducible` | PASS (verified externally) | EXTERNAL by script design — satisfied by THIS CI evidence ✅ |

**PASS.**  Every condition's PASS/FAIL label and arithmetic
matches the locked baseline.

### 3.3 FAIL label preserved

The script's final summary lines:

```
Twinkle family: FAIL
Lamb family:    FAIL

M6.5 FAIL
```

**PASS.**  The locked NEGATIVE / FAIL label is preserved
unchanged.  4 of 7 conditions FAIL; the script declares `M6.5
FAIL` without ambiguity, exactly as recorded in MILESTONES.md
("M6.5 result: FAIL (4 of 7 pre-set conditions fail)").

### 3.4 No condition silently re-weighted

**PASS.**  The script's own pre-declared 7-condition list
(declared once in MILESTONES.md *before* the canonical run, and
re-emitted by the script's `Pass-condition self-check` block on
this CI run) is the binding list.  The reproduction did not
add, drop, re-order, or re-weight any condition.  Each
condition's PASS/FAIL label is computed by the same logic that
was committed at the M5.6-lock SHA d332f54 and unchanged
since.

### 3.5 Forbidden-actions compliance (per O034 spec)

| Forbidden action | Compliance |
|---|---|
| Per-family tuning (changing thresholds, weights, MIN_NT, ranking, or any other parameter to improve M6.5's pass count) | None applied — `run_m6_5_multi_family.py`, `run_m6_4_family_retrieval.py`, `run_m6_3_retrieval.py`, `run_m6_1_similarity.py`, `run_milestones.py` all unmodified.  The git log between the M5.6-lock SHA d332f54 and this run's SHA 9eaabac contains zero pipeline-code edits (only nmb3/ documentation, the shared workflow yml's ffmpeg infrastructure step, and the M3.1 archive). |
| Scoring changes (modifying M6.1 similarity formula or weights) | None applied — `run_m6_1_similarity.py` unmodified.  The M6.4 reproduction under O033 already independently confirmed the M6.1 underlying scores match the M6.2 baseline to 3 decimal places. |
| Extractor edits (modifying the locked M5.6 extractor or any of its components) | None applied — `run_milestones.py` unmodified.  The M5.6 extractor reproduction under O023 already confirmed bit-identical 107/144 = 0.7431 with all 18 cells matching. |
| Downgrading the comparator from "outranks-all-other" to a weaker comparator | None applied — the script uses the strict "outranks-all-other" comparator throughout (see the headline column "best-same-family outranks all-other"), the same as MILESTONES.md.  No softer comparator was substituted to make cond3 look better. |
| Restating cond5 to look better | None applied — cond5 is exactly the regression check ("Twinkle behaviour does not regress").  The script self-reports the exact regression in cell counts: `twinkle_box: expected (3, 3, True, False), got (2, 3, True, False)` and `twinkle_harmonica: expected (2, 3, True, False), got (1, 2, False, False)`.  These are the same regressions MILESTONES.md describes verbatim. |

**Explicit assertion (per O034's evidence-required clause):**
**No per-family tuning, scoring change, or extractor edit was
applied in this reproduction.**  The reproduction was performed
by dispatching the unmodified canonical script on a fresh
ubuntu-latest CI runner with no caches.  The diff between the
M5.6-lock SHA d332f54 and this run's SHA 9eaabac contains no
pipeline-code modifications.

## 4. Honesty floor — explicit non-trigger record

O034's "Auto-execute permission" clause requires that any
reproduction passing M6.5 must trigger the Decision Policy
"suspected metric gaming" early-stop.  This subsection
explicitly records that the trigger did NOT fire and why.

  - **Verdict produced by the script:** `M6.5 FAIL`.
  - **Number of pre-set conditions FAILing:** 4 (cond2, cond3,
    cond4, cond5) — same as locked baseline.
  - **Number of pre-set conditions PASSing:** 3 (cond1, cond6,
    cond7) — same as locked baseline.
  - **Trigger condition:** Would fire if the script printed
    `M6.5 PASS`, or if ≥4 of the 7 conditions reported PASS, or
    if the script's family-level booleans (`Twinkle family` /
    `Lamb family`) reported PASS for either family.
  - **Trigger status:** NOT FIRED.  All three trigger
    conditions checked: `M6.5` line is `FAIL`; only 3 of 7
    conditions are PASS (less than 4); both family-level
    booleans report `FAIL`.
  - **Required loop response on non-trigger:** Continue with
    standard SUCCEEDED workflow (write interpreter output,
    update objective map, append decisions.log, commit, surface
    to Steve).  Done.

The honesty floor was the most important guard on this
objective; it held without surprise because the canonical FAIL
on this fresh clone reproduces the canonical FAIL on the
locked SHA exactly.

## 5. Scoring sanity — incidental reproduction of M6.1 / M6.2 / M6.3 / M6.4 base

This section is an OBSERVATION, not a formal re-validation
claim (those would each require their own objectives —
O030 / O031 / O032 plus the already-SUCCEEDED O033).

The M6.5 leaderboards include the same family-1 internal scores
that M6.4 produced under O033's reproduction one objective ago.
Spot checks against the M6.4 reproduction (interpreter output
for O033) and against the M6.2 / M6.3 baselines documented in
MILESTONES.md:

| Score in M6.5 reproduction | Same as M6.4 / M6.2 / M6.3 baseline | Source |
|---|---|---|
| `twinkle_box` query → `twinkle_box_tstretch`: 0.479 | yes (= M6.4 repro § 6 = M6.2 baseline) | M6.2 |
| `twinkle_box` query → `twinkle_harmonica`: 0.284 | yes (= M6.4 repro § 6 = M6.2 baseline) | M6.2 |
| `twinkle_box` query → `twinkle_people`: 0.164 | yes (= M6.4 repro = M6.2 baseline) | M6.2 |
| `twinkle_harmonica` query → `twinkle_box`: 0.284 | yes (= M6.4 repro) | M6.4 |
| `twinkle_people` query → leaderboard intercepts | identical leaderboard ordering and scores to M6.4 reproduction (the addition of Lamb clips inserts new rows but does not perturb the F1-internal scores) | M6.4 |

Therefore the M6.5 reproduction provides further incidental
evidence that the underlying M6.1 / M6.2 / M6.3 / M6.4 scores
also reproduce on this fresh clone — but this is incidental,
not the formal re-validation that O030 / O031 / O032 would
require.  The observation is logged here so Steve has a full
picture; it does not extend the scope of this objective.

## 6. Risk assessment

| Risk | Status | Notes |
|---|---|---|
| FAIL flipped to PASS (metric gaming or regression) | Did NOT occur | Honesty floor not triggered.  Verdict reproduced as FAIL with bit-identical per-condition arithmetic. |
| Underlying-score drift (would suggest backend / library version drift) | None observed | All sampled scores in § 5 reproduce to the 3-decimal precision MILESTONES.md records. |
| Sample drift (Lamb / Twinkle clips were re-fetched from samples-v3 / -v1) | None observed | Per-cell match is exact; per-condition arithmetic is exact; weak-flag firing pattern matches. |
| Caching contamination | None | No `actions/cache` step; pip used `--no-cache-dir`; checkout was fresh; samples fetched fresh by `scripts/fetch_samples.py` (the same fetch the M6.4 reproduction under O033 used). |
| Cherry-picking | None.  First-attempt success | No retry was needed; the first dispatch produced the reproduction of record. |
| Forbidden-action violation | None | See § 3.5 — the table enumerates each forbidden action and the compliance evidence. |
| Comparator downgrade (would make cond3 look artificially better) | None | The strict "outranks-all-other" comparator was used throughout; the script labels the column "outranks all-other" in every leaderboard. |
| Cond5 restatement (would make the Twinkle regression invisible) | None | Cond5 fired FAIL with the exact `expected (..., ..., ..., ...), got (..., ..., ..., ...)` arithmetic from MILESTONES.md. |

## 7. What this report does NOT claim

This report is the M6.5 multi-family retrieval FAIL reproduction
evidence.  By its existence it does not authorise any of the
following — each requires a separate Steve gate:

  - It does not advance any other objective.  Only O034 moves
    to SUCCEEDED.  In particular: O035 (boundary documentation),
    O036 (M6 phase closure recommendation), O037 (reproducibility
    appendix) are NOT advanced; each requires its own Steve
    string and its own Block plan.
  - It does not formally re-validate M6.1, M6.2, M6.3, or M6.4
    in their own right.  The score reproduction in § 5 is
    incidental observational evidence, not formal re-validation.
  - It does not propose, justify, or even suggest a fix to
    M6.5.  M6.5 is the locked NEGATIVE; the funding-package
    discipline is to record it honestly, not to repair it.  Any
    fix attempt would be a different objective and would risk
    metric gaming.
  - It does not extend M6.5's claim beyond the canonical
    12-clip library + 6 query set (3 Twinkle + 3 Lamb) that
    the script operates on.
  - It does not relax the strict "outranks-all-other"
    comparator (forbidden by O034's spec; explicitly respected
    — see § 3.5 and § 6).
  - It does not restate cond5 to soften the Twinkle regression
    (forbidden by O034's spec; explicitly respected — § 3.5).
  - It does not re-open M3.1, M3.2, M3.3, M3.4, M5.x, or M6.4
    closure.  Those milestones remain in their canonical state.
  - It does not invalidate or modify the P4 partial-scope
    closure recommendation that Steve approved at
    2026-04-25T17:59:01Z.  P4 closure remains binding.
  - It does not edit any policy file, MILESTONES.md, the M3.1
    archive, the M3.1 closure recommendation, the P4 closure
    recommendation, or any pipeline code.
  - It does not declare that the M6.5 FAIL is now resolved,
    explained beyond MILESTONES.md, or sharpened.  The locked
    "honest interpretation" in MILESTONES.md remains the
    canonical interpretation.
  - It does not make any funding, commercial, or perceptual-
    validity claim.

## 8. Recommended next move

Per the autonomous loop policy "Session Completion Rule", the
loop stops on objective success and proposes the next objective
without beginning it.  Standing constraint "do not execute the
whole preferred path yet" still active.

On the preferred path, natural next options now that O034 has
produced SHA-pinned CI evidence for M6.5:

  - **O035** (Boundary documentation file) — declared dependency
    O034 is now satisfied; O035 is documentation-only ("write;
    commit; push"); no fresh CI runs needed.  Cleanest single-
    step.
  - **O036** (M6 phase closure recommendation) — declared
    dependency O035 still PROPOSED; would need O035 first or an
    explicit waiver string.
  - **O037** (Reproducibility appendix) — declared dependency
    O036 still PROPOSED, AND the broader empirical-evidence
    gap surfaced in the previous round (M3.x, M4.1, M5.1–M5.5,
    M6.1, M6.2, M6.3 still lack SHA-pinned CI runs) still
    applies.  Not yet executable in its current spec.
  - **A broader CI-pinning campaign** for the milestones that
    still lack SHA-pinned CI runs (would close the empirical
    evidence gap that blocks O037 today).
  - **Pause.**

Awaiting Steve.
