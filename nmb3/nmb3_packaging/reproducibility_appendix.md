# Reproducibility appendix (partial-scope)

Generated:    2026-04-25T19:26:00Z
Author:       NMB3 autonomous loop, executing objective O037 under
              Steve's rewrite + execute string at 2026-04-25T19:24:00Z
              (see `nmb3/nmb3_decisions.log` for the verbatim text).
Audience:     Steve, plus any external reviewer Steve chooses to
              hand this appendix to.
Scope:        **Partial.**  This appendix covers the three milestone
              results currently backed by SHA-pinned CI evidence on
              canonical (M5.6, M6.4, M6.5) and explicitly lists 13
              other milestones that are **gaps, not failures**.  It
              does **not** claim full-chain reproducibility, does
              **not** make any funding, commercial, perceptual-
              validity, or second-corpus generalisation claim, and
              does **not** authorise a broader CI-pinning campaign.
              The full-scope variant of this appendix (covering
              every M3.1–M6.5 milestone with SHA-pinned CI evidence)
              remains available as a future expansion if Steve later
              authorises a broader CI-pinning campaign and a
              follow-up rewrite of O037; nothing here forecloses
              that path.
Provenance:   O037 was rewritten from its original full-scope spec
              ("for every locked milestone result M3.1 through M6.5")
              to this partial-scope spec at 2026-04-25T19:24:00Z by
              Steve, who holds Rewrite permission on O037.  The
              rewrite is recorded in the O037 entry of
              `nmb3/nmb3_objective_map.md` (Rewrite history field)
              and in `nmb3/nmb3_decisions.log` (verbatim Steve
              string + loop interpretation).

---

## How to use this appendix

For each entry in **Section A**, an external reviewer can re-dispatch
the canonical no-cache reproducibility workflow against the listed
head SHA with the listed `target` and `script` inputs, and expect
to obtain the listed headline number with no caches, no auto-commit
of any artefact, and the workflow yml in its target-agnostic shape.
The verifier command is given inline.

For each entry in **Section B**, the milestone's locked baseline
lives in `MILESTONES.md` at the canonical commit at the time of this
appendix; no SHA-pinned CI run currently backs that baseline on
canonical, and that absence is a **gap** (no fresh CI evidence yet),
not a **failure** (which would be a re-validation that produced a
negative result).  Negative / failed milestones, where they exist,
are documented separately in `nmb3/nmb3_reports/boundary.md` (M6.5
FAIL is part of the M6 partial-scope closure approved at
2026-04-25T19:18:00Z; M5.7, M5.8, M5.9 are NEGATIVE / ABANDONED
front-end ablations recorded as factual pointers in the boundary
doc and in `MILESTONES.md`).

---

## Section A — SHA-pinned reproductions (3 milestones)

### A.1 — M5.6: locked benchmark, fresh-clone reproduction

| field | value |
|---|---|
| Milestone | M5.6 (adaptive-routing locked benchmark) |
| Headline number | **107 / 144 = 0.7431** correct on the locked benchmark |
| Locked baseline lives at | `m4_1_results.json` at canonical commit `d332f54` |
| Reproduction CI run id | `24936558636` (Run A) |
| Reproduction head SHA | `1368524699287cc28ae416c7edda7f6c04b4c0e0` |
| Workflow file | `.github/workflows/nmb3_no_cache_repro.yml` |
| Workflow inputs | `target=m5_6`, `script="python run_m4_1_benchmark.py"` |
| CI artefact (90-day retention) | `nmb3-no-cache-repro-m5_6-24936558636` |
| Inner stdout file | `no_cache_repro_m5_6.txt` |
| Loop's interpreter output | `nmb3/nmb3_reports/o023_m5_6_fresh_clone_reproduction.md` |
| Closure recommendation | `nmb3/nmb3_reports/m5_phase_p4_closure_recommendation.md` (P4 partial-scope closure, APPROVED by Steve at 2026-04-25T17:59:01Z via chat string `"Approve P4 partial-scope closure"`) |

There is also an observational replay of the same M5.6 result
(Run B, run id `24936650442` at the same head SHA `1368524`,
target `m5_6_routing`, script wrapping `run_m4_1_benchmark.main()`
with a runtime monkey-patch of `run_milestones.pitch_at` to count
routing decisions).  Run B produces the same `107 / 144 = 0.7431`
and additionally reports the locked routing split `234 / 54`.  Run
B is observational, not the load-bearing reproduction; the
load-bearing reproduction is Run A above.

**Verifier command an external reviewer can run** (requires GitHub
Actions write access to the canonical repo or a fork; no local
build required):

```
gh workflow run nmb3_no_cache_repro.yml \
    --ref 1368524699287cc28ae416c7edda7f6c04b4c0e0 \
    -f target=m5_6 \
    -f script="python run_m4_1_benchmark.py"
```

The reviewer should expect the run to produce stdout
containing `Correct: 107/144 (74.31%)` and the artefact
`nmb3-no-cache-repro-m5_6-<new-run-id>` containing
`no_cache_repro_m5_6.txt`.

### A.2 — M6.4: family-retrieval PASS

| field | value |
|---|---|
| Milestone | M6.4 (Twinkle family-retrieval demo, single-family library) |
| Headline result | **PASS** — all 4 pre-set conditions PASS; all 12 cells of the headline table reproduce verbatim (`twinkle_box` family hits 3/3 in top-3 outranking YES; `twinkle_harmonica` hits 2/3 in top-3 outranking YES; `twinkle_people` hits 1/3 in top-3 outranking NO and flagged weak-evidence) |
| Locked baseline lives at | `MILESTONES.md` § M6.4 (canonical) |
| Reproduction CI run id | `24937477484` |
| Reproduction head SHA | `3929fbcda21e79045075dcc9ca3802f7bb9d7bc0` |
| Workflow file | `.github/workflows/nmb3_no_cache_repro.yml` |
| Workflow inputs | `target=m6_4`, `script="python run_m6_4_family_retrieval.py"` |
| CI artefact (90-day retention) | `nmb3-no-cache-repro-m6_4-24937477484` |
| Inner stdout file | `no_cache_repro_m6_4.txt` |
| Loop's interpreter output | `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md` |
| Closure recommendation | `nmb3/nmb3_reports/m6_phase_closure_recommendation.md` (M6 partial-scope closure, APPROVED by Steve at 2026-04-25T19:18:00Z via chat string `"Approve M6 partial-scope closure"`) |
| Boundary co-location | The M6.4 PASS holds on the M6.3 9-clip library (Twinkle is the only family in the library); the same locked pipeline produces the M6.5 FAIL on the multi-family library (entry A.3 below).  External citations of the M6.4 PASS must co-locate the M6.5 FAIL boundary in the same paragraph (binding requirement of the M6 partial-scope closure, recommendation item 1). |

**Verifier command an external reviewer can run:**

```
gh workflow run nmb3_no_cache_repro.yml \
    --ref 3929fbcda21e79045075dcc9ca3802f7bb9d7bc0 \
    -f target=m6_4 \
    -f script="python run_m6_4_family_retrieval.py"
```

### A.3 — M6.5: multi-family FAIL (the boundary)

| field | value |
|---|---|
| Milestone | M6.5 (multi-family retrieval validation, 12-candidate library with three Lamb clips added) |
| Headline result | **FAIL** — all 18 cells of the 6-query × 3-metric headline grid reproduce verbatim (`twinkle_box` 2/3/YES; `twinkle_harmonica` 1/2/NO; `twinkle_people` 1/1/NO weak; `lamb_solo` 0/1/NO weak; `lamb_group` 1/2/NO; `lamb_male` 0/1/NO weak); all 7 pre-set conditions reproduce (cond1 PASS; cond2 FAIL 1/3; cond3 FAIL 0/3; cond4 FAIL on `polyphonic` "partial melodic match" WARNING firing 3 times; cond5 FAIL with bit-identical Twinkle regression arithmetic; cond6 PASS; cond7 EXTERNAL satisfied by this CI evidence); both family-level booleans report FAIL; final script line `M6.5 FAIL` |
| Locked baseline lives at | `MILESTONES.md` § M6.5 (canonical, "NEGATIVE" tag) |
| Reproduction CI run id | `24937928571` |
| Reproduction head SHA | `9eaabacf5ae5640d329fa97ebe316486eaccd08f` |
| Workflow file | `.github/workflows/nmb3_no_cache_repro.yml` |
| Workflow inputs | `target=m6_5`, `script="python run_m6_5_multi_family.py"` |
| CI artefact (90-day retention) | `nmb3-no-cache-repro-m6_5-24937928571` |
| Inner stdout file | `no_cache_repro_m6_5.txt` |
| Loop's interpreter output | `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md` |
| Closure recommendation | `nmb3/nmb3_reports/m6_phase_closure_recommendation.md` (M6 partial-scope closure; same approval as A.2) |
| Honesty floor | Explicitly checked at reproduction time and **NOT** triggered.  The Decision Policy "suspected metric gaming" early-stop fires only if a fresh M6.5 reproduction returns PASS where the locked baseline returned FAIL; this reproduction returned FAIL with the bit-identical headline and condition table, so the floor was satisfied without triggering. |
| Boundary co-location | The M6.5 FAIL is the locked pipeline's boundary on multi-family material with fewer than ~4 non-trivial intervals per clip.  It is part of the result, not a blocker for closure (verbatim phrasing from the M6 partial-scope closure recommendation § 1).  External citations of the M6.5 FAIL must continue to co-locate the M6.4 PASS (entry A.2 above) in the same paragraph. |

**Verifier command an external reviewer can run:**

```
gh workflow run nmb3_no_cache_repro.yml \
    --ref 9eaabacf5ae5640d329fa97ebe316486eaccd08f \
    -f target=m6_5 \
    -f script="python run_m6_5_multi_family.py"
```

---

## Section B — Gap list (13 milestones, "gap, not failure")

The following 13 milestone results are not yet backed by a
SHA-pinned CI run on canonical.  Each entry is a **gap**, not a
**failure**: the milestone's locked baseline lives in
`MILESTONES.md` and is the operative result for any current
citation, but no fresh CI re-validation has been dispatched on
canonical for that milestone in the form documented in Section A.
Steve's rewrite of O037 explicitly forbids running a broader
CI-pinning campaign within O037's scope to backfill these gaps;
any such campaign would require its own Steve authorisation as a
separate objective.

| # | Milestone | Script in repo | Locked baseline | Gap status |
|---|---|---|---|---|
| 1 | M3.1 | `run_m3_1_metric.py` | `MILESTONES.md` § M3.1 | **gap, not failure** -- locked baseline operative; no SHA-pinned CI run on canonical |
| 2 | M3.2 | `run_m3_2_optimize.py` | `MILESTONES.md` § M3.2 | **gap, not failure** |
| 3 | M3.3 | `run_m3_3_sensitivity.py` | `MILESTONES.md` § M3.3 | **gap, not failure** |
| 4 | M3.4 | `run_m3_4_focused_search.py` | `MILESTONES.md` § M3.4 | **gap, not failure** |
| 5 | M4.1 | `run_m4_1_benchmark.py` (the M4.1 milestone preceded the M5.6 lock; M5.6 reuses the same script -- the M4.1 entry is the M4.1 locked baseline before the M5.6 routing update, not the same as the M5.6 reproduction in A.1) | `MILESTONES.md` § M4.1 | **gap, not failure** |
| 6 | M5.1 | `run_m5_1_diagnostics.py` | `MILESTONES.md` § M5.1 | **gap, not failure** |
| 7 | M5.2 | `run_m5_2_onset_ablation.py` | `MILESTONES.md` § M5.2 | **gap, not failure** |
| 8 | M5.3 | (no separate script in repo at this commit; M5.3 is documented in `MILESTONES.md` § M5.3 with diagnostics produced via the M5.1 / M5.2 scripts.  Citing the milestone still requires a SHA-pinned CI run, which does not exist; therefore this entry is correctly listed as a gap.) | `MILESTONES.md` § M5.3 | **gap, not failure** |
| 9 | M5.4 | `run_m5_4_pitch_ablation.py` | `MILESTONES.md` § M5.4 | **gap, not failure** |
| 10 | M5.5 | `run_m5_5_adaptive_ablation.py` | `MILESTONES.md` § M5.5 | **gap, not failure** |
| 11 | M6.1 | `run_m6_1_similarity.py` | `MILESTONES.md` § M6.1 | **gap, not failure** -- incidental score reproduction inside the M6.4 PASS leaderboard (entry A.2) and M6.5 FAIL leaderboard (entry A.3) provides observational evidence the M6.1 pair scores reproduce on the M6.4/M6.5 head SHAs, but the M6.1 script itself has not been dispatched as a SHA-pinned CI run; the entry is therefore a gap |
| 12 | M6.2 | `run_m6_2_search.py` | `MILESTONES.md` § M6.2 | **gap, not failure** -- same incidental observational reproduction caveat as M6.1 |
| 13 | M6.3 | `run_m6_3_retrieval.py` | `MILESTONES.md` § M6.3 | **gap, not failure** -- same incidental observational reproduction caveat as M6.1 / M6.2 |

**What "gap, not failure" means:**
  - **gap** = no SHA-pinned CI run on canonical for this milestone yet.  The milestone's locked baseline in `MILESTONES.md` remains the operative result for any current citation; an external reviewer who needs to verify it must currently rely on `MILESTONES.md` and the scripts named above, without the no-cache CI guarantee that Section A entries carry.
  - **failure** = a fresh re-validation has been dispatched and returned a negative result (M6.5 in entry A.3 is the canonical example of a failure / NEGATIVE result that has been re-validated).  None of the 13 milestones in this Section B table are failures by this definition.

**What is explicitly NOT in this gap list (because they are
NEGATIVE / FAIL / ABANDONED, not gaps):**
  - **M5.7** (pyin tracker ablation, NEGATIVE) -- locked at
    canonical commit `7fd167e`; documented in `MILESTONES.md` and
    in `nmb3/nmb3_reports/boundary.md` § 4 as a prior negative
    front-end ablation, not a gap.
  - **M5.8** (HPSS ablation, NEGATIVE) -- locked at canonical
    commit `b5669ed`; same.
  - **M5.9** (CREPE-abandoned) -- documented in `MILESTONES.md`
    and in the boundary doc § 4.
  - **M6.5** (multi-family FAIL) -- already in Section A.3 above
    as a SHA-pinned reproduction of the FAIL.

---

## Section C — Non-claim register

This appendix does NOT make any of the following claims; each
would require its own Steve authorisation and its own objective:

  - It does NOT claim full-chain reproducibility.  Only 3 of the
    16 referenced milestones (3 in Section A + 13 in Section B)
    have SHA-pinned CI evidence on canonical at the time of this
    appendix.  Any external statement that "every NMB3
    milestone is reproducible from this appendix" would be
    incorrect; the accurate statement is "M5.6, M6.4, and M6.5
    are reproducible from this appendix; the other 13
    milestones' locked baselines remain operative but are not
    yet backed by SHA-pinned CI runs on canonical".
  - It does NOT make any funding, commercial, perceptual-
    validity, second-corpus generalisation, or real-time-
    deployment claim.
  - It does NOT propose, endorse, or hint at any fix for the
    M6.5 FAIL or any other negative result.  Fix discussion
    belongs in O043 (continuation-scope out-of-scope register),
    which itself depends on O042 (Steve-only continuation-scope
    authorisation).  Until then, the M6.5 FAIL boundary
    documented in entry A.3 is the operative result.
  - It does NOT authorise a broader CI-pinning campaign within
    O037's scope.  Steve's rewrite at 2026-04-25T19:24:00Z
    explicitly forbids this.  Backfilling the Section B gaps
    with SHA-pinned CI runs would require a separate Steve
    authorisation as a new objective; nothing in this appendix
    pre-authorises such a campaign.
  - It does NOT change any policy file.  The policy files
    (`nmb3_decision_policy.md`, `nmb3_autonomous_loop_policy.md`,
    `nmb3_manifesto.md`, `nmb3_roles.md`, etc) are unchanged by
    this objective.
  - It does NOT extend M6.5's FAIL beyond the canonical 12-clip
    library + 6-query set documented in entry A.3 and in the
    M6 partial-scope closure recommendation § 3.2.
  - It does NOT soften M6.5's FAIL label.  The closure approved
    at 2026-04-25T19:18:00Z binds M6.5 FAIL as part of the M6
    result; this appendix preserves that framing in entry A.3.
  - It does NOT re-open M3.1 / M3.2 / M3.3 / M3.4 / M5.x or
    M6.4 closure.
  - It does NOT invalidate the P4 partial-scope closure
    approved at 2026-04-25T17:59:01Z or the M6 partial-scope
    closure approved at 2026-04-25T19:18:00Z.  Both closures
    remain binding; this appendix is an evidence-pinning
    document under those closures, not a re-litigation of
    them.

## Section D — Future-expansion path preserved

If Steve later authorises a broader CI-pinning campaign as a
separate objective and that campaign succeeds in producing
SHA-pinned CI runs for all 13 Section B milestones (or any
subset of them), this appendix can be superseded by a
`reproducibility_appendix_v2.md` that moves the affected
entries from Section B (gap) to Section A (SHA-pinned),
preserving the partial-scope discipline of this current version
for any milestones that remain gaps.  Nothing in this appendix
forecloses that path; the current version is the honest
snapshot of what the loop can SHA-pin from canonical right
now under O037's partial-scope rewrite.
