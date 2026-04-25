# NMB3 Boundary Document — Locked Pipeline Good Case and Boundary

Generated:    2026-04-25T18:58:00Z
Objective:    O035 — Boundary documentation file
              (`nmb3/nmb3_objective_map.md`, P7 entry section).
Canonical SHA at write time:
              `cf165f4fb5b4067002d140a4ea739b4a8bb1b087`.
Pinned to:    M5.6 extractor lock SHA `d332f54`; M6.4 family-
              retrieval re-validation evidence at run id
              24937477484 / SHA `3929fbc`; M6.5 multi-family
              FAIL re-validation evidence at run id 24937928571
              / SHA `9eaabac`.

Purpose:      A single point of reference for the locked NMB3
              pipeline's *good case* and its *current boundary*.
              The good case is M6.4 (Twinkle family retrieval).
              The boundary is M6.5 (Lamb multi-family FAIL).
              Both are NEGATIVE-honest results: the boundary is
              recorded, not glossed.  This document does not
              propose, endorse, or hint at any fix; out-of-scope
              fix discussion lives under O043 only.

---

## 1. Verbatim quote of MILESTONES.md "Current boundary"

The following is a byte-identical quote of the
`## Current boundary` section of `MILESTONES.md` at canonical
SHA `cf165f4fb5b4067002d140a4ea739b4a8bb1b087`, lines 40-53
inclusive:

```markdown
## Current boundary

* **What works:** small-library retrieval by structural similarity on
  **clean instrumental melodic families** (M6.4 Twinkle result).
* **What does not yet work:** **voice-heavy / weak-melodic extraction**
  -- when the M5.6 pitch tracker recovers fewer than ~4 non-trivial
  intervals from a clip, similarity scores collapse into the same band
  as unrelated clips and family-level separation disappears (M6.5 Lamb
  result, and the `twinkle_people` borderline case).

The bottleneck is the front-end pitch tracker on weak-melodic material,
not the retrieval layer. Improving past this boundary would mean
swapping the front-end tracker (e.g. CREPE, never benchmarked here) --
explicitly out of scope for the current locked repo.
```

### Verifier reproduction

To verify byte-equality of the above quote against the canonical
source at the SHA cited:

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping
git checkout cf165f4fb5b4067002d140a4ea739b4a8bb1b087
sed -n '40,53p' MILESTONES.md | sha256sum
# expected: a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc  -
```

Quoted-section line range:  `MILESTONES.md` lines 40-53 (inclusive).
Quoted-section SHA256:      `a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc`.

The CREPE mention inside the quoted passage is reproduced
verbatim because the quote-byte-equality property requires it.
It is not a fix recommendation made by this document.

---

## 2. What works (locked-pipeline good case)

Within the locked NMB3 pipeline, the following result is
demonstrated and SHA-pinned:

  - **M6.4 family-retrieval PASS (Twinkle family, 9-clip
    library).**  Three Twinkle queries (`twinkle_box`,
    `twinkle_harmonica`, `twinkle_people`) over a 9-clip
    library that includes 4 Twinkle-family clips and 5
    unrelated clips.  Family-level separation holds: the
    best same-family hit outranks all non-family clips for
    every Twinkle query.  Per-condition: 4 of 4 declared
    pass conditions PASS.  cond4 fires its outside-family
    "partial melodic match" WARNING on `polyphonic` (which
    is correctly flagged but does NOT outrank the family);
    `twinkle_people` is correctly tagged as a weak-evidence
    query (only 2 non-trivial intervals).

  - **Evidence pinning:** O033 SUCCEEDED at canonical
    SHA 9eaabac (interpreter output:
    `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md`;
    re-validation CI run id `24937477484` at head SHA
    `3929fbc`; artefact
    `nmb3-no-cache-repro-m6_4-24937477484` with inner stdout
    `no_cache_repro_m6_4.txt`, 90-day retention).

What "good case" means here, precisely:

  - The library is small (9 clips, including 4 from the
    family being queried).
  - The melodic content is *clean instrumental* (Twinkle on
    music box, harmonica, and a small ensemble at the
    `twinkle_people` borderline).
  - The family is *one* family.  Adding a second family
    (Lamb) breaks separation -- see § 3.
  - The locked similarity uses the strict "outranks-all-
    other" comparator and the locked M5.6 adaptive routing
    pitch front-end.
  - No per-family tuning, no scoring change, no extractor
    edit was made for this result.

---

## 3. What does not yet work (locked-pipeline boundary)

Within the locked NMB3 pipeline, the following NEGATIVE result
is recorded and SHA-pinned:

  - **M6.5 multi-family FAIL (Twinkle + Lamb, 12-clip
    library).**  Adding a second family (Mary Had a Little
    Lamb, three timbres -- `lamb_solo`, `lamb_group`,
    `lamb_male`) to the 9-clip M6.3 library yields a 12-clip
    library and 6 queries (3 Twinkle + 3 Lamb).  Per-condition:
    4 of 7 declared pass conditions FAIL.  The headline
    leaderboard, with all 18 cells reproduced verbatim
    against MILESTONES.md M6.5:

    | query              | family | top3 | top5 | best-same-family outranks all-other |
    |--------------------|:------:|:----:|:----:|:----:|
    | `twinkle_box`        | F1 | 2 | 3 | YES |
    | `twinkle_harmonica`  | F1 | 1 | 2 | NO  |
    | `twinkle_people`     | F1 | 1 | 1 | NO (weak) |
    | `lamb_solo`          | F2 | 0 | 1 | NO (weak) |
    | `lamb_group`         | F2 | 1 | 2 | NO |
    | `lamb_male`          | F2 | 0 | 1 | NO (weak) |

    Concretely: zero of the three Lamb queries achieves
    "best same-family outranks all-other"; only one of the
    three Lamb queries has a family hit in the top 3 (and
    that hit -- `lamb_male` for the `lamb_group` query --
    sits behind `polyphonic` in rank 1); the strong-match
    label fires on `polyphonic` for outside-family clips
    three times.  The Twinkle behaviour also regresses
    once Lamb clips compete in the same library
    (`twinkle_box` top-3 family hits drop 3->2, and
    `twinkle_harmonica` top-3 family hits drop 2->1).

  - **Verbatim verdict from the script:**  `M6.5 FAIL`,
    with `Twinkle family: FAIL` and `Lamb family: FAIL` on
    the family-level summary lines.

  - **Evidence pinning:** O034 SUCCEEDED at canonical SHA
    cf165f4 (interpreter output:
    `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md`;
    re-validation CI run id `24937928571` at head SHA
    `9eaabac`; artefact
    `nmb3-no-cache-repro-m6_5-24937928571` with inner stdout
    `no_cache_repro_m6_5.txt`, 90-day retention).

What "boundary" means here, precisely (recasting the verbatim
quote in concrete terms drawn only from the locked evidence):

  - The locked M5.6 pitch tracker recovers fewer than ~4
    non-trivial intervals from each Lamb clip on these
    recordings (script self-reports 2 intervals on
    `lamb_solo`, 3 on `lamb_male`).  Below that threshold,
    similarity scores collapse into the same narrow band
    as the unrelated clips, and family-level separation
    disappears.
  - The same threshold also catches `twinkle_people` --
    which the locked pipeline already labels as a
    weak-evidence query in M6.4.
  - The bottleneck is *upstream of the retrieval layer*;
    M6.1 / M6.2 / M6.3 / M6.4 retrieval logic is unchanged
    between the M6.4 PASS case and the M6.5 FAIL case.

---

## 4. What has already been tried within the locked work
   (relevant prior NEGATIVE results, no new fix proposed here)

To make clear that the boundary documented in § 3 has been
probed at the front-end level within the locked work, this
subsection enumerates the prior NEGATIVE / ABANDONED ablations
already on canonical.  This is a factual pointer to existing
locked artefacts, not a fix recommendation.

  - **M5.7 (pyin pitch tracker swap ablation) -- NEGATIVE**
    at MILESTONES.md, commit `7fd167e`.  pyin did not improve
    the locked M3-M5 benchmark; rejected.
  - **M5.8 (HPSS / harmonic pre-filter ablation) -- NEGATIVE**
    at MILESTONES.md, commit `b5669ed`.  Harmonic pre-filter
    did not improve the locked M3-M5 benchmark; rejected.
  - **M5.9 (CREPE pitch tracker) -- ABANDONED** at MILESTONES.md.
    Install was abandoned mid-flight; CREPE was *never
    benchmarked* in the locked work, exactly as the verbatim
    quote in § 1 records.

These three prior results sit upstream in the NMB3 history;
the boundary in § 3 is what remains after them.

---

## 5. Non-claim register

This document records the boundary.  It does NOT make,
endorse, or hint at any of the following claims; each would
require its own Steve gate and its own objective:

  - It does NOT propose a fix for the M6.5 FAIL.  Fix
    discussion belongs in O043 (continuation-scope
    out-of-scope register), which itself depends on O042
    (Steve-only continuation-scope authorisation string).
    Until then, the boundary is the result.
  - It does NOT recommend CREPE, voice-friendly extractor,
    second-corpus generalisation, perceptual-validity
    studies, real-time deployment, or commercial
    productisation.  The CREPE mention in § 1 is part of
    the verbatim MILESTONES.md quote and is reproduced
    only because the success criterion requires byte-
    equality; it is not a recommendation made by this
    document.
  - It does NOT soften M6.5's FAIL label.  M6.5 is FAIL,
    not "partial pass", not "scheduled improvement", not
    "open issue".
  - It does NOT extend M6.5's claim beyond the canonical
    12-clip library + 6-query set (3 Twinkle + 3 Lamb)
    that the script operates on.
  - It does NOT advance any other objective.  O036 (M6
    phase closure recommendation), O037 (reproducibility
    appendix), O038-O041 (packaging artefacts), O042
    (continuation-scope authorisation), and O043
    (continuation out-of-scope register) all remain in
    their current states.
  - It does NOT formally re-validate M6.1, M6.2, M6.3, or
    M5.x in their own right.
  - It does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 / M5.x
    or M6.4 closure.
  - It does NOT invalidate the P4 partial-scope closure
    approved by Steve at 2026-04-25T17:59:01Z.  P4 closure
    remains binding.
  - It does NOT make any funding, commercial, or
    perceptual-validity claim.

---

## 6. Pointer summary

| What | Where |
|---|---|
| Canonical "Current boundary" passage | `MILESTONES.md` lines 40-53 at SHA `cf165f4` (SHA256 `a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc`) |
| Locked-pipeline good case (M6.4 PASS) interpreter output | `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md` |
| Locked-pipeline good case (M6.4 PASS) CI evidence | run `24937477484` at SHA `3929fbc`, artefact `nmb3-no-cache-repro-m6_4-24937477484` |
| Locked-pipeline boundary (M6.5 FAIL) interpreter output | `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md` |
| Locked-pipeline boundary (M6.5 FAIL) CI evidence | run `24937928571` at SHA `9eaabac`, artefact `nmb3-no-cache-repro-m6_5-24937928571` |
| Prior front-end ablations (NEGATIVE / ABANDONED) | `MILESTONES.md` M5.7 (`7fd167e`), M5.8 (`b5669ed`), M5.9 |
| Out-of-scope / continuation-scope discussion | O043 (`nmb3/nmb3_packaging/scope_and_out_of_scope.md`) once O042 has been issued by Steve |
