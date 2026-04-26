# O039 Interpreter Output — Independent Reproduction Protocol

Generated:   2026-04-26T01:50:00Z
Objective:   O039 — Independent reproduction protocol
             (`nmb3/nmb3_objective_map.md`, P8 packaging arc,
             after O038 methodology appendix)
Verdict:     **PASS — protocol artefact written; reference CI
             dispatch reproduced all four headline lines on a
             fresh `ubuntu-latest` runner with no caches; pinning
             complete.**

---

## 1. Pinning

  - **Protocol artefact:**     `nmb3/nmb3_packaging/independent_reproduction_protocol.md`
  - **Pinning SHA:**           `766cff65c2f868e37d344065c5188d69db88cf90`
                               (the commit that introduced the
                               protocol artefact; this is the SHA
                               an external reviewer should clone
                               at to bit-identically reproduce the
                               headline numbers via Mode A or to
                               re-dispatch via Mode B).
  - **Workflow file:**         `.github/workflows/nmb3_no_cache_repro.yml`
                               (created in O023 at SHA `1368524`,
                               ffmpeg-extended in O033 at SHA
                               `3929fbc`; reused unmodified here).
  - **CI run id:**             `24945531211`
  - **CI run head SHA:**       `766cff65c2f868e37d344065c5188d69db88cf90`
                               (workflow ran at the same commit
                               that introduced the protocol — the
                               protocol's pin SHA and the dispatch
                               SHA coincide).
  - **Run started:**           2026-04-26T01:43:24Z
  - **Run finished:**          2026-04-26T01:44:45Z (1 min 21 s)
  - **Run conclusion:**        `success`
  - **Dispatch URL:**          https://github.com/stevewebmarket/nightingale-mapping/actions/runs/24945531211
  - **Artefact name:**         `nmb3-no-cache-repro-m6_4_repro_smoke-24945531211`
                               (90-day retention)
  - **Workflow inputs:**
      - `target=m6_4_repro_smoke`
      - `script=python run_m4_1_benchmark.py && python run_m6_4_family_retrieval.py`

## 2. What was reproduced and how

A single CI dispatch against the shared no-cache workflow at
`.github/workflows/nmb3_no_cache_repro.yml` ran two canonical
scripts back-to-back on a fresh `ubuntu-latest` runner with no
caches:

  1. `python run_m4_1_benchmark.py` — the locked M5.6 baseline
     (107/144 = 0.7431) on the canonical 6-clip benchmark set.
  2. `python run_m6_4_family_retrieval.py` — the locked M6.4
     family-retrieval table on the canonical 4-clip Twinkle
     family + 5-clip non-family library, including the
     weak-evidence flag and cond4 honesty self-check.

Both scripts ran unmodified.  No pipeline file was edited; no
new workflow file was created; the shared workflow yml was
reused unmodified.

The dispatch was performed via the GitHub REST API (the `gh`
CLI is not installed in the loop's environment); the protocol
nonetheless documents `gh workflow run` as the recommended
external interface, because `gh` is the documented portable way
to dispatch a workflow_dispatch event from an external
reviewer's machine.  The REST-API call used identical inputs to
the protocol's documented `gh workflow run` invocation; the
workflow yml is unaware of which client dispatched it.

## 3. Success criteria — point-by-point

### 3.1  Protocol artefact exists and fits on one page

| Property | Value |
|---|---|
| Path | `nmb3/nmb3_packaging/independent_reproduction_protocol.md` |
| Source line count | 111 lines markdown source (incl. blank lines, code-block fences, multi-line bullet continuations) |
| Effective rendered length | one page (single-page markdown render at standard width) |
| Sections | Header / Pinning / Mode B / Mode A / Expected output / Out of scope / Reference dispatch |

**PASS.**  The protocol was written and committed at SHA
`766cff6`.  Both Mode A (local fresh clone) and Mode B (CI
re-dispatch) are documented, both with explicit
`--no-cache-dir` / no-`actions/cache` discipline.

### 3.2  Reference CI dispatch reproduces the headline numbers

Four expected lines verified verbatim in the run log
(`reproduce/8_Run reproduction script.txt` of run 24945531211):

| Expected line | Found at log line | Match |
|---|---|---|
| `TOTAL ... 107/144   0.7431` (M5.6 baseline) | `TOTAL                                                      107/144   0.7431` | ✅ |
| `twinkle_box ... top3=3 top5=3 outranks-all-nonfam=YES` | `  twinkle_box               top3=3 top5=3 outranks-all-nonfam=YES` | ✅ |
| `4. weak-evidence honestly flagged AND twinkle_people still weak: PASS` | exact match | ✅ |
| `M6.4 PASS` (final line of M6.4 stdout) | exact match | ✅ |

**PASS.**  All four headline-line verifications succeeded.

### 3.3  Cell-level reproduction of the M5.6 6-clip × 3-transform table

| clip | pitch_shift | time_stretch | composition | total | matches O023 Run A / canonical |
|---|---|---|---|---|---|
| orchestra | 8/8 | 8/8 | 8/8 | 24/24 | ✅ |
| rock | 8/8 | 4/8 | 6/8 | 18/24 | ✅ |
| flute | 7/8 | 8/8 | 7/8 | 22/24 | ✅ |
| polyphonic | 1/8 | 3/8 | 1/8 | 5/24 | ✅ |
| highenergy | 6/8 | 5/8 | 4/8 | 15/24 | ✅ |
| synthetic_just | 8/8 | 7/8 | 8/8 | 23/24 | ✅ |
| **TOTAL** | | | | **107/144** | ✅ |

All 18 of 18 cells reproduce bit-identically vs the O023 Run A
table (run 24936558636 at SHA `1368524`) and vs the canonical
`m4_1_results.json` shipped at the M5.6 lock commit `d332f54`.
Zero drift on any cell.  This is the same zero-drift result
O023 reported, now reproduced a third time (after O023's Run A
and Run B) on a different head SHA, demonstrating that
intervening doc-only commits between `1368524` and `766cff6`
have no effect on the pipeline.

### 3.4  M6.4 family-retrieval table

| Query | top3 | top5 | outranks-all-nonfam | weak |
|---|---|---|---|---|
| `twinkle_box` | 3 | 3 | YES | no |
| `twinkle_harmonica` | 2 | 3 | YES | no |
| `twinkle_people` | 1 | 1 | NO | weak (2 non-trivial) |

**PASS.**  Every cell of the M6.4 family-retrieval table
reproduces vs the O033 reference (run 24937477484 at SHA
`3929fbc`) and vs the canonical M6.4 PASS recorded in
`MILESTONES.md`.  The weak-evidence flag fires on
`twinkle_people` only (2 non-trivial intervals, < `MIN_NT=4`),
and the cond4 honesty self-check PASSes.

### 3.5  Forbidden actions — explicit non-violation check

| Forbidden action (per O039 spec) | Status |
|---|---|
| Relaxing the "no caches" requirement | None — workflow uses `actions/checkout@v4` with no cache options, `pip install --no-cache-dir` everywhere, no `actions/cache` step.  Mode A in the protocol documents the same discipline. |
| Hiding any setup step in an unspoken assumption | None — both Mode A and Mode B list every step explicitly: clone → pin → venv → pip → fetch_samples → run scripts (Mode A), or workflow inputs verbatim (Mode B). |
| Introducing M6.4-specific logic into the shared workflow yml | None — the workflow yml is unchanged from canonical (last edit was O033's ffmpeg add at SHA `3929fbc`); M6.4 logic lives entirely in the `script` input. |

## 4. Risk assessment

| Risk | Status | Notes |
|---|---|---|
| Sample drift | None | Bit-identical M5.6 cell match (18/18) and bit-identical M6.4 row match (3/3 queries) imply samples are byte-identical to the canonical fixtures. |
| Library-version drift | None observed | `pip freeze` versions captured in the run log; numbers reproduce regardless. |
| Caching contamination | None | No `actions/cache` step; pip used `--no-cache-dir`; checkout fresh; samples fetched fresh by `scripts/fetch_samples.py`. |
| Cherry-picking | None | First and only dispatch with `target=m6_4_repro_smoke`; no failed runs were discarded; the dispatch is the reproduction. |
| Backend-version drift (audio decoder) | Low | ffmpeg installed via apt-get on the runner; the M6.4 script decoded `twinkle_people.m4a` without error.  Same backend posture as O033 (the dispatch that first surfaced the missing-ffmpeg infrastructure issue). |
| Protocol vs dispatch SHA drift | None | The protocol artefact's introducing commit and the dispatch's head SHA coincide at `766cff6` — pin SHA and dispatch SHA are identical. |
| Workflow yml mutation this loop | None | Workflow yml unchanged from canonical (zero of two yml-edit budget consumed this loop). |

## 5. What this report does NOT claim

This report is the O039 independent-reproduction-protocol PASS
evidence.  By its existence it does not authorise any of the
following — each requires a separate Steve gate:

  - It does not advance any other objective (O029–O035, O040+).
    Only O039 moves to SUCCEEDED.
  - It does not generalise the M5.6 baseline beyond the canonical
    6-clip benchmark, or the M6.4 family-retrieval table beyond
    the canonical 4-clip Twinkle family + 5-clip non-family
    library.
  - It does not formally re-validate M6.1, M6.2, or M6.3 (the
    underlying-score match in this dispatch is incidental
    observation, identical to the incidental observation in
    O033 § 6).
  - It does not extend the locked M5.6 / M6.4 PASS verdicts; it
    only confirms they reproduce on a fresh clone with no caches
    via the documented protocol.
  - It does not fill any of the 13 explicit gaps catalogued in
    `nmb3/nmb3_packaging/reproducibility_appendix.md` § B.  The
    gaps remain gaps.
  - It does not modify the partial-scope basis on which Steve
    approved P4 closure (2026-04-25T17:59:01Z) and M6 closure
    (2026-04-25T19:18:00Z).  Both partial-scope closures remain
    binding exactly as they were.
  - It does not invalidate or supersede the methodology
    appendix (O038) or the reproducibility appendix (O037);
    the protocol artefact is a pointer to the no-cache-workflow
    dispatch path, not a replacement for either appendix.
  - It does not edit any policy file, MILESTONES.md, the M3.1
    archive, the M3.1 closure recommendation, the P4 closure
    recommendation, the M6 closure recommendation, or any
    pipeline code.
  - It does not make any funding, commercial, or
    perceptual-validity claim.

## 6. Recommended next move

Per the autonomous loop policy "Session Completion Rule", the
loop stops on objective success and proposes the next objective
without beginning it.  Standing constraint "do not execute the
whole preferred path yet" still active.

Natural next options after O039, given the packaging arc is now
three artefacts deep (O037 reproducibility appendix + O038
methodology appendix + O039 independent reproduction protocol):

  - **O040** if it exists in the objective map as the next
    packaging step (e.g. a packaging-arc closure recommendation
    aggregating O037 / O038 / O039).
  - Authorise the upstream M6.1 / M6.2 / M6.3 formal
    re-validations (O030 / O031 / O032), which would convert the
    incidental observations in O033 § 6 and O039 § 5 into formal
    evidence.
  - **Pause.**

Awaiting Steve.
