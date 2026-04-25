# O023 Interpreter Output — M5.6 Fresh-Clone Reproducibility Check

Generated:    2026-04-25T17:38:00Z
Objective:    O023 — M5.6 fresh-clone reproducibility check
              (`nmb3/nmb3_objective_map.md`, P4 entry-adjacent)
Verdict:      **PASS — all three success criteria met, with zero
              drift on every measured cell and zero drift on the
              routing distribution.**

---

## 1. What was reproduced and how

The locked M5.6 baseline — **107 / 144 = 0.7431** — was reproduced
on a clean ubuntu-latest CI runner with no caches, using the
shared parameterised reproducibility workflow created in this same
objective execution.  The M5.6 lock baseline command on canonical
is `python run_m4_1_benchmark.py`, which loads the six canonical
clips (orchestra, rock, flute, polyphonic, highenergy,
synthetic_just), runs the unchanged M3.1 invariance pipeline with
the M5.6 `pitch_mode='adaptive_rms_attack'` default, and prints the
6-clip × 3-transform table.

Two CI runs were dispatched on the same head SHA (`1368524`):

  - **Run A** — pure M5.6 reproduction.  Run id 24936558636.
    Script: `python run_m4_1_benchmark.py`.  Used as the headline
    bit-identical evidence.

  - **Run B** — routing-instrumented reproduction.  Run id
    24936650442.  Script: an inline Python wrapper that monkey-
    patches `run_milestones.pitch_at` to count routing decisions
    (baseline vs short_med) while invoking
    `run_m4_1_benchmark.main()` unchanged.  Used to satisfy the
    routing-distribution criterion directly rather than by
    inference.  No pipeline file was modified; the wrapper lives
    only in the dispatch's `script` input, not in the repository.

Both runs were dispatched against `.github/workflows/nmb3_no_cache_repro.yml`
with the no-caches design rules from O012's workflow spec
(checkout with no caching options; pip install with
`--no-cache-dir`; no `actions/cache` step; no auto-commit of any
artefact).  Workflow file head SHA when each run executed:
**`1368524699287cc28ae416c7edda7f6c04b4c0e0`**.

## 2. Success criteria — point-by-point

### Criterion 1: 107/144 reproduces bit-identically

| Source | Total | Score |
|---|---|---|
| Canonical `m4_1_results.json` (M5.6 lock at d332f54) | 107/144 | 0.7430555555555556 |
| Run A (run id 24936558636, SHA 1368524) | 107/144 | 0.7431 (printed) |
| Run B (run id 24936650442, SHA 1368524) | 107/144 | 0.7431 (printed) |

**PASS.**  Both fresh-clone runs reproduce the headline.

### Criterion 2: per-clip / per-transform breakdown reproduces to the note-flip

The canonical `m4_1_results.json` (frozen at the M5.6 lock commit
d332f54) and the fresh-clone reproduction Run A were compared at
every individual cell of the 6-clip × 3-transform grid.

| clip | pitch_shift | time_stretch | composition | clip total |
|---|---|---|---|---|
| orchestra | 8/8 ✅ | 8/8 ✅ | 8/8 ✅ | 24/24 ✅ |
| rock | 8/8 ✅ | 4/8 ✅ | 6/8 ✅ | 18/24 ✅ |
| flute | 7/8 ✅ | 8/8 ✅ | 7/8 ✅ | 22/24 ✅ |
| polyphonic | 1/8 ✅ | 3/8 ✅ | 1/8 ✅ | 5/24 ✅ |
| highenergy | 6/8 ✅ | 5/8 ✅ | 4/8 ✅ | 15/24 ✅ |
| synthetic_just | 8/8 ✅ | 7/8 ✅ | 8/8 ✅ | 23/24 ✅ |
| **TOTAL** | | | | **107/144** ✅ |

**PASS.**  All 18 of 18 (clip, test) cells reproduce bit-identically.
Zero note-flips.  This is a stronger result than the
"reproduces to the note-flip" wording requires (which would have
admitted small drift); the fresh clone reproduces with zero drift.

The cell-level comparison was performed by the loop using the
canonical `m4_1_results.json` (which the M5.6 lock commit d332f54
shipped as the frozen expected output) on one side, and the parsed
6-row table from Run A's stdout on the other.

### Criterion 3: routing distribution reproduces to ±2 routing decisions

| Source | baseline | short_med | total onsets | route fraction |
|---|---|---|---|---|
| Canonical M5.5 / M5.6 claim (MILESTONES.md) | 234 | 54 | 288 | 18.75% short_med |
| Run B (instrumented, run id 24936650442, SHA 1368524) | 234 | 54 | 288 | 18.75% short_med |
| Delta | 0 | 0 | 0 | 0 |

**PASS.**  Routing distribution reproduces with zero drift,
comfortably within the ±2 tolerance.  Run B also confirmed
`other_mode = 0` (no onset bypassed the adaptive routing and fell
back to a non-adaptive pitch_mode).

The instrumentation works by wrapping `run_milestones.pitch_at` to
re-compute the same `_rms_attack_ratio` the production code uses,
applying the same threshold (1.5), and counting which side of the
threshold each onset lands on.  No pipeline behaviour was changed;
only an observation hook was added.  The 18/18 bit-identical cell
match in Criterion 2 already implied that routing decisions had to
be identical (a single flipped routing decision could change the
within-tolerance count for that test); Run B turns that implication
into a direct measurement.

## 3. Pinning evidence (per O023 success criterion: "CI run id pinned by SHA")

Both runs are pinned to head SHA **`1368524699287cc28ae416c7edda7f6c04b4c0e0`**,
the canonical commit that introduced the shared no-cache workflow:

  - Run A:  https://github.com/stevewebmarket/nightingale-mapping/actions/runs/24936558636
  - Run B:  https://github.com/stevewebmarket/nightingale-mapping/actions/runs/24936650442
  - Workflow file:  `.github/workflows/nmb3_no_cache_repro.yml`
  - Workflow file commit:  `1368524`
  - Reproduction targets dispatched:  `m5_6` (Run A), `m5_6_routing` (Run B)
  - Reproduction commands:
      - Run A:  `python run_m4_1_benchmark.py`
      - Run B:  inline Python wrapper around `run_m4_1_benchmark.main()`

Artefacts retained for 90 days at:

  - `nmb3-no-cache-repro-m5_6-24936558636`
  - `nmb3-no-cache-repro-m5_6_routing-24936650442`

## 4. Risk assessment

| Risk | Status | Notes |
|---|---|---|
| Sample drift (samples re-fetched mid-window) | None | Bit-identical results imply samples are byte-identical to the canonical fixtures used at d332f54. |
| Library-version drift | None observed | Pip resolved versions were captured in each run log; numbers match regardless. |
| Caching contamination | None | No `actions/cache` step; pip used `--no-cache-dir`; checkout was fresh. |
| Cherry-picking | None | Both dispatches are the first dispatch of their `target` value; no failed runs were discarded. |
| M5.6-specific logic in shared workflow yml | None | The yml has zero target-specific logic.  The M5.6-specific bits live entirely in the `script` inputs (Run A: standard canonical script; Run B: inline observation wrapper). |
| Pipeline modification by the routing instrumentation | None | Run B monkey-patches `pitch_at` only at runtime in the dispatch process; the canonical `run_milestones.py` was untouched.  Run A used the unmodified canonical script and produced bit-identical numbers, providing the independent control. |
| Loop-budget pressure | Low | This loop dispatched twice; each dispatch is within the workflow's spec; loop count unchanged. |

## 5. What this report does NOT claim

This report is the M5.6 lock fresh-clone reproducibility evidence.
It does not, by its existence, authorise any of the following
(each requires a separate Steve gate):

  - It does not advance any other objective (O020, O021, O022,
    O024, O029, O037, etc.).  Only O023 moves to SUCCEEDED.
  - It does not generalise the M5.6 baseline beyond the canonical
    6-clip benchmark set.  M5.6 = 107/144 is the M4.1 6-clip
    score; nothing here speaks to performance on any other clip.
  - It does not claim improvement over the M5.6 baseline.  This
    is a reproduction of the lock, not an optimisation.
  - It does not re-open M3.1, M3.2, M3.3, M3.4, M5.1, M5.2, M5.3,
    M5.4, or M5.5 closure.  Those milestones remain in the state
    captured by `MILESTONES.md`.
  - It does not declare M5.6 a "PASS for funding purposes".  M5.6
    PASS is documented in `MILESTONES.md` and in the M5.6 commit
    d332f54; this report only confirms that PASS reproduces on a
    fresh clone with no caches.
  - It does not recommend M4 transition (note: M4 here means
    funding-package preparation, not the M4.1 milestone, which is
    superseded by M5.6 per the objective map's off-path note for
    P2).  P8 / P9 work remains gated on later objectives.
  - It does not generalise to non-M5.6 milestones (M6.1, M6.4,
    M6.5).  The shared workflow created here CAN be reused for
    those (per O039's design); this report only validates M5.6.
  - It does not edit any policy file, MILESTONES.md, the M3.1
    archive, the M3.1 closure recommendation, or the canonical
    pipeline code.
  - It does not make any funding claim.

## 6. Activation-rule check

The objective map's activation rule for off-path objectives says:

> "if O022 (M5.6 lock re-validation) fails to reproduce 107/144
>  to the note-flip, then O017 (M5.2 cqt_flux ablation) and O018
>  (M5.3 lock) become on-path so the regression can be localised"

O022's literal scope is the M5.6 lock re-validation; O023's scope
is the same lock under stronger conditions (fresh clone, no
caches).  Both runs A and B passed at 18/18 bit-identical with zero
routing drift.  Therefore:

  - **No P3 / P2 activation triggered.**  M5.1–M5.3 and M4.1
    remain off-path.  The M5.6 fresh-clone evidence stands on its
    own, and there is no regression that points back at any
    earlier milestone.
  - **No errata commit needed against MILESTONES.md.**  The
    canonical numbers in MILESTONES.md (107/144, 234/54 routing)
    reproduce exactly.

## 7. Recommended next move

Per the autonomous loop policy "Session Completion Rule", the loop
stops on objective success and proposes the next objective without
beginning it.  Standing constraint "do not execute the whole
preferred path yet" still active.

On the preferred path, the natural next objective after O023 is
**O024** (P4 closure recommendation: aggregate O020–O023 into a
single Steve-facing recommendation that the locked M5.6 baseline
is reproduced).  However, O024's success criteria require
aggregating O020–O023; only O023 has actually been executed in
this session (O020, O021, O022 are still PROPOSED).  Steve has
options:

  - Authorise O022 next (the literal M5.6 lock re-validation,
    using the in-repo benchmark rather than the no-cache
    workflow), which would close the activation-rule loop with
    two independent reproductions of 107/144.
  - Authorise O024 with a narrower scope: a P4-partial closure
    recommendation that aggregates O023 alone and notes O020 /
    O021 / O022 as deferred under the activation rule.
  - Skip ahead to a P6 / P7 objective on the preferred path
    (O029+).
  - Pause.

Awaiting Steve.
