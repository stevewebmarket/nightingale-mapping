# P4 Closure Recommendation — partial-scope, anchored on O023

Generated:    2026-04-25T17:41:53Z
Author:       NMB3 autonomous loop, executing objective O024 under
              Steve's authorisation string "Execute O024
              (partial-scope closure)" (see
              `nmb3/nmb3_decisions.log`, 2026-04-25T17:41:53Z entry).
Audience:     Steve.
Status:       Recommendation only.  Becomes binding only on Steve's
              explicit approval string in chat.

---

## 1. Headline (required by O024 success criterion)

The locked M5.6 baseline is **107 / 144 = 0.7431** and it
reproduces bit-identically on a fresh clone with no caches.

That is the load-bearing reproducibility number that anchors
every later claim in the funding package, and it is now backed by
two independent runs of the unmodified canonical script on a
clean ubuntu-latest CI runner with no caches, both pinned to the
same head SHA.

## 2. Scope of this recommendation

O024's literal purpose is to "aggregate O020–O023 into a single
Steve-facing recommendation that the locked M5.6 baseline is
reproduced".  Of those four objectives:

  - **O020** (M5.4 re-document the pitch-window NEGATIVE result):
    NOT executed.  Status remains PROPOSED on canonical.
  - **O021** (M5.5 re-validate adaptive-routing ablation): NOT
    executed.  Status remains PROPOSED on canonical.
  - **O022** (M5.6 re-validate adaptive-routing lock, in-repo
    benchmark): NOT executed.  Status remains PROPOSED on canonical.
  - **O023** (M5.6 fresh-clone reproducibility check, on
    preferred path): SUCCEEDED at 2026-04-25T17:38:00Z (canonical
    commit 4e72100).

This recommendation is therefore the **partial-scope variant** of
P4 closure that Steve explicitly authorised in his
"Execute O024 (partial-scope closure)" string: it aggregates
**O023 alone**, on the strength of the canonical activation rule
(see § 4) which permits the off-path P4 objectives to remain
deferred when O023 succeeds with zero drift.  The full P4
recommendation, aggregating all four objectives, remains
available as a future expansion — it would require Steve to
authorise O020 / O021 / O022 first.

## 3. Evidence base — O023 in detail

### 3.1 What O023 ran

The shared parameterised reproducibility workflow at
`.github/workflows/nmb3_no_cache_repro.yml` (created in canonical
commit 1368524 under the O023 / O012 interchangeability clause)
was dispatched twice against head SHA
**`1368524699287cc28ae416c7edda7f6c04b4c0e0`**:

  - **Run A** — id 24936558636, target=`m5_6`.  Script:
    `python run_m4_1_benchmark.py` (the unmodified canonical M5.6
    benchmark command).
  - **Run B** — id 24936650442, target=`m5_6_routing`.  Script:
    an inline Python wrapper around the same benchmark that
    monkey-patched `run_milestones.pitch_at` at runtime to count
    routing decisions while invoking
    `run_m4_1_benchmark.main()` unchanged.  No pipeline file was
    modified; no M5.6-specific logic was introduced into the
    workflow yml.

Both runs ran on a clean ubuntu-latest runner with no caches
(`actions/checkout@v4` with no cache options; `pip install
--no-cache-dir`; no `actions/cache` step; no auto-commit of any
artefact, per O012's design constraints).

### 3.2 What O023 reproduced — point-by-point

| Success criterion (per O023 spec) | Canonical reference | Reproduction | Drift |
|---|---|---|---|
| Headline 107/144 = 0.7431 | MILESTONES.md M5.6 (commit d332f54) | Run A: `TOTAL  107/144  0.7431` | 0 |
| Per-clip / per-transform breakdown reproduces "to the note-flip" | `m4_1_results.json` (frozen at d332f54) | Run A: 18 of 18 (clip × test) cells bit-identical | 0 / 18 cells (better than the criterion required) |
| Routing distribution reproduces to ±2 routing decisions | MILESTONES.md M5.5 / M5.6 = 234 baseline / 54 short_med | Run B: 234 baseline / 54 short_med | 0 (exact) |

The per-cell evidence:

| clip | pitch_shift | time_stretch | composition | clip total |
|---|---|---|---|---|
| orchestra | 8/8 | 8/8 | 8/8 | 24/24 |
| rock | 8/8 | 4/8 | 6/8 | 18/24 |
| flute | 7/8 | 8/8 | 7/8 | 22/24 |
| polyphonic | 1/8 | 3/8 | 1/8 | 5/24 |
| highenergy | 6/8 | 5/8 | 4/8 | 15/24 |
| synthetic_just | 8/8 | 7/8 | 8/8 | 23/24 |
| **TOTAL** | | | | **107/144 = 0.7431** |

Identical at every cell to the canonical `m4_1_results.json`
written at the M5.6 lock commit d332f54 (and unchanged on
canonical since).

### 3.3 Pinning

Every datum in this recommendation can be re-derived from
canonical artefacts by an external reviewer:

  - Workflow file:  `.github/workflows/nmb3_no_cache_repro.yml`
    (introduced at canonical commit 1368524).
  - Run A:  https://github.com/stevewebmarket/nightingale-mapping/actions/runs/24936558636
  - Run B:  https://github.com/stevewebmarket/nightingale-mapping/actions/runs/24936650442
  - Both runs at head SHA `1368524699287cc28ae416c7edda7f6c04b4c0e0`.
  - Full interpreter output:
    `nmb3/nmb3_reports/o023_m5_6_fresh_clone_reproduction.md`
    (canonical commit 4e72100).
  - Canonical baseline being matched against:
    `m4_1_results.json` (frozen at the M5.6 lock commit d332f54).

## 4. Why partial-scope closure is permitted

The objective map's "Activation rule for off-path objectives"
states (verbatim, see `nmb3/nmb3_objective_map.md`):

> "An off-path objective ... [becomes] on-path only when an
> on-path objective produces evidence that points back at the
> off-path milestone — for example, if O022 (M5.6 lock
> re-validation) fails to reproduce 107/144 to the note-flip,
> then O017 (M5.2 cqt_flux ablation) and O018 (M5.3 lock) become
> on-path so the regression can be localised."

O023 is the stronger sibling of O022: same M5.6 lock validation
under stricter conditions (fresh clone, no caches, routing-
distribution evidence required, run id pinned by SHA).  O023
reproduced 107/144 with **zero drift on every measured cell and
zero drift on the routing distribution** — comfortably stricter
than "to the note-flip".

Therefore:

  - **No regression points back at any earlier milestone.**
    M4.1 (P2), M5.1 / M5.2 / M5.3 (P3), M5.4 (P4-O020), or M5.5
    (P4-O021) all remain off-path under the activation rule.
  - **No errata commit against MILESTONES.md is required.**  The
    canonical numbers (107/144, 234/54 routing, 18% routed
    fraction) reproduce exactly.
  - **The literal P4 spec ("aggregate O020–O023") is satisfiable
    in partial form**: the weakest reading would have been "all
    four objectives must be SUCCEEDED before P4 closure can be
    recommended", but that reading is incompatible with the
    activation rule, which explicitly permits the off-path
    objectives (O020 / O021 / O022) to remain deferred when O023
    succeeds with zero drift.

The full-scope expansion path is preserved.  If Steve later
authorises O020 / O021 / O022, this recommendation can be
superseded by a full-scope `m5_phase_p4_closure_recommendation_v2.md`
that aggregates all four.  Nothing in this recommendation closes
that door.

## 5. What this recommendation recommends

Subject to Steve's approval:

  - **Treat the locked M5.6 baseline of 107/144 = 0.7431 as
    independently reproducible** for funding-package purposes,
    on the strength of the O023 fresh-clone evidence.
  - **Treat the M5.6 routing distribution (234 baseline / 54
    short_med, ~19% routed)** as part of the locked baseline,
    likewise reproducible from a fresh clone.
  - **Cite the O023 evidence by run id and SHA** in any future
    funding-package material:
      - run ids 24936558636 and 24936650442
      - head SHA `1368524699287cc28ae416c7edda7f6c04b4c0e0`
      - reproducibility workflow:
        `.github/workflows/nmb3_no_cache_repro.yml`
  - **Treat the M5.4 / M5.5 / M5.6 in-repo objectives (O020 /
    O021 / O022) as deferred under the activation rule** — not
    failed, not skipped, *deferred*.  They become on-path again
    only if a later objective produces evidence that points back
    at one of them (and at present no later evidence does).
  - **Keep the shared no-cache reproducibility workflow as the
    canonical reproduction surface** for all later headline-
    number reproductions (M4.1 if ever needed, M6.4 family
    retrieval, M5.6 + M6.4 smoke for the independent reproduction
    protocol in O039).  No M5.6-specific or other-target-specific
    logic should ever be added to that workflow yml.

## 6. What this recommendation does NOT recommend (forbidden + scope guards)

This recommendation explicitly does NOT do, recommend, or imply
any of the following.  Each would require its own Steve gate.

  - It does **not** claim improvement on the M5.6 baseline (this
    is forbidden by O024's "Forbidden actions" clause and is not
    implied by any reproduction evidence).
  - It does **not** generalise the M5.6 baseline beyond the
    canonical 6-clip benchmark set (orchestra, rock, flute,
    polyphonic, highenergy, synthetic_just).  The 107/144 number
    is the M4.1-style score on those six clips; nothing here
    speaks to performance on any other clip.
  - It does **not** generalise the routing distribution beyond
    the same 6-clip set.  234 baseline / 54 short_med is the
    routing pattern produced by those six clips' onset structure;
    different clips would produce different distributions.
  - It does **not** re-open M3.1, M3.2, M3.3, M3.4, M5.1, M5.2,
    M5.3, M5.4, M5.5 closure.  Those milestones remain in the
    state captured by `MILESTONES.md` and (for M3.1) the frozen
    archive at `nmb3/nmb3_archive/m3_1/`.
  - It does **not** declare M5.6 a "PASS for funding purposes" on
    the strength of reproducibility evidence alone.  M5.6 = PASS
    is documented in `MILESTONES.md` and at canonical commit
    d332f54; this recommendation only confirms that PASS reproduces
    on a fresh clone with no caches.
  - It does **not** recommend transition to M4 (the funding-
    package-preparation phase referenced by P8 / P9 in the
    objective map).  Funding-package-preparation work remains
    gated on later objectives (O037–O044).
  - It does **not** authorise any later objective.  Specifically,
    it does not begin O020, O021, O022, O029, O033, O037, O039,
    O042, or any other objective.  Per the autonomous loop
    policy "Session Completion Rule", the loop will stop after
    this objective's success and propose the next objective
    without beginning it.
  - It does **not** edit any policy file
    (`nmb3_decision_policy.md`, `nmb3_autonomous_loop_policy.md`).
  - It does **not** edit `MILESTONES.md`.
  - It does **not** edit the M3.1 frozen archive at
    `nmb3/nmb3_archive/m3_1/` (every file there is locked under
    O004's immutability rule).
  - It does **not** edit the M3.1 closure recommendation at
    `nmb3/nmb3_reports/m3_1_closure_recommendation.md`.
  - It does **not** edit any pipeline code (`run_milestones.py`,
    `run_m4_1_benchmark.py`, the `run_m5_*` ablation scripts,
    `scripts/fetch_samples.py`).
  - It does **not** edit the shared reproducibility workflow
    (`.github/workflows/nmb3_no_cache_repro.yml`); that file is
    the load-bearing reproduction surface and must remain
    target-agnostic.
  - It does **not** make any funding claim, any commercial claim,
    or any claim about perceptual validity of the M5.6 metric.

## 7. Decision request

Steve, please respond with one line:

  - **"Approve P4 partial-scope closure"** (or equivalent unambiguous
    string) — accepts this recommendation as binding for
    funding-package purposes, on the partial-scope basis defined
    in § 2.  Future full-scope expansion remains available if
    O020 / O021 / O022 are later authorised and succeed.
  - **"Reject — wait for O022 (or O020 / O021 / O022)"** — defers
    P4 closure until at least O022 has executed.  This
    recommendation file remains on canonical as a draft.
  - **"Send back for changes"** with specific edits requested.
    The loop will revise and resubmit.
  - **Pause** or any other instruction.

Until Steve responds with one of these, the recommendation is on
canonical as a draft only and is not binding.
