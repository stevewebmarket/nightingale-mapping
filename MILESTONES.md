# Milestones

Single source of truth for milestone numbers. Each milestone is one commit,
sets its pass condition *before* the run, and reports headline numbers
that reproduce byte-identically from a fresh clone.

Format per entry: **What changed / Headline / Beat baseline? / Regressions /
Reproducible / Recommendation.**

---

## M3.1 — Audio Transform Invariance Metric

Formalised the implicit milestone score as one number:

```
score = notes_within_tolerance / total_notes  (1% tolerance, octave-folded)
```

Aggregated across orchestra + rock × pitch_shift / time_stretch / composition.

**Baseline:** 44/48 = 0.9167.

## M3.2 — Hyperparameter sweep

Small grid over `onset_delta`, `fmin`, `fmax`, `tolerance_pct`. Best
config carried forward; defaults frozen.

## M3.3 — Sensitivity check

Re-ran the chosen config across noise / clip-length perturbations to
confirm the score wasn't a knife-edge.

## M3.4 — Focused search

Narrower search around the M3.2 winner. Confirmed M3.2 default; no
further improvement justified at this scale.

## M4.1 — Six-clip benchmark

Expanded from 2 clips to 6: orchestra, rock, flute, polyphonic, highenergy,
synthetic_just (deterministic generator). Three transforms per clip.

**Baseline established:** total = 93/135 = 0.6889 with the M3 default
extractor.  (135 because polyphonic onset detection collapsed to 5/8.)

## M5.1 — Per-onset diagnostics (commit `9595ba1`)

Classified each detection into matches / octave_errors / other_errors /
missing. Key finding: polyphonic loses 3/8 onsets entirely and highenergy
sits in an "other_errors" bottleneck. Frame-selection problems isolated
from pitch-tracker problems.

## M5.2 — Onset detector ablation (commit `0a2790b`)

Tested 7 onset detectors. **`cqt_flux` (CQT-based onset envelope) won:**
polyphonic detected onsets 5/8 → 8/8 across all transforms; flute 16/24 →
22/24; total 93/135 → 100/144.

## M5.3 — Lock cqt_flux as default onset (commit `100a6dc`)

Pure integration step. Numbers reproduce byte-identically.
**Tracked regression:** rock time_stretch 7/8 → 4/8 (cqt onset placement
on percussive material).

## M5.4 — Pitch-window ablation (commit `5eba1f6`) — NEGATIVE

6 pitch-window variants tested with M5.3 fixed. **No variant passed all
pre-set conditions.** Key finding: frame selection alone cannot improve
polyphonic + highenergy without breaking flute.

## M5.5 — Adaptive routing ablation (commit `5042891`)

A single global rule per onset selects between baseline window
`[t-0.15, t+0.25]` and short-medium window `[t+0.02, t+0.18]`.
Four routing signals tested.

**`adaptive_rms_attack` (early-half RMS / late-half RMS in `[t-0.05, t+0.20]`,
threshold 1.5) passes all 7 conditions:**

| | poly | high | orch | flute | synth | rock_t | total |
|--|--|--|--|--|--|--|--|
| M5.3 baseline | 4 | 9 | 24 | 22 | 23 | 4 | 100/144 (0.6944) |
| **M5.5 adaptive_rms_attack** | **5** | **15** | **24** | **22** | **23** | **4** | **107/144 (0.7431)** |

Routes 234 baseline / 54 short_med (~19% routed). Genuinely adaptive,
not collapsed to one side.

## M5.6 — Lock adaptive routing (commit `d332f54`)

Pure integration step. `pitch_at()` now dispatches on `pitch_mode`;
`baseline` and `short_med` remain selectable for comparisons. Numbers
reproduce byte-identically to M5.5; fresh-clone validated.

**Locked headline: 107/144 = 0.7431.**

## M5.7 — Pitch tracker swap ablation (commit `7fd167e`) — NEGATIVE

Tested YIN (control) vs pyin vs CREPE (skipped — not importable in this
environment, not adding heavy deps mid-arc).

| variant | poly | high | orch | flute | synth | rock_t | total |
|---|---|---|---|---|---|---|---|
| yin (control) | 5 | 15 | 24 | 22 | 23 | 4 | 107/144 |
| pyin | 10 | 8 | 24 | 13 | 24 | 4 | 87/144 |

pYIN gives a real isolated win on polyphonic (+5) — confirming the M5.4
hypothesis that polyphonic was pitch-tracker limited, not segmentation
limited. But pyin's voicing classifier rejects valid frames in noisy
material, costing 7-10 matches each on rock, flute, highenergy.
**Pre-set conditions fail (3 of 7).** Not locked.

## M5.8 — HPSS / harmonic pre-filter ablation (commit `b5669ed`) — NEGATIVE

Tested harmonic-percussive source separation (HPSS) as a pre-filter
before YIN pitch estimation, expecting cleaner harmonic content on
polyphonic and percussive clips.

| variant | poly | high | orch | flute | synth | rock_t | total |
|---|---|---|---|---|---|---|---|
| yin (control) | 5 | 15 | 24 | 22 | 23 | 4 | 107/144 |
| hpss + yin | 5 | 15 | 24 | 22 | 23 | 4 | 107/144 |

No measurable change on any clip. **Pre-set conditions fail** (no win,
added cost). Not locked.

## M5.9 — CREPE pitch tracker — ABANDONED

Attempted to install CREPE for the pitch-tracker swap originally skipped
in M5.7. Heavy dependency footprint (`tensorflow-cpu` required), unclear
upside given M5.7's pyin result, abandoned mid-install. `tensorflow-cpu`
remains installed as a harmless leftover.

## M6.1 — Pairwise structural similarity (`run_m6_1_similarity.py`)

First milestone using the locked M5.6 extractor as a fixed front-end.
Score two clips by matching their interval-ratio sequences:
octave-folded match + raw match + non-trivial-only match (sub-scores
combined with weights 0.45 / 0.25 / 0.30).

Honest verdict labels gated on **>= 4 non-trivial intervals on both
sides** so a near-flat clip cannot be promoted to "structural match".

| pair                                | score | verdict                    |
|-------------------------------------|------:|----------------------------|
| orchestra vs orchestra_pshift       | 0.700 | structural match           |
| orchestra vs orchestra_tstretch     | 0.700 | structural match           |
| orchestra vs rock                   | 0.164 | insufficient melodic content |

All four pre-set pass conditions met. Two architect rounds applied
(gap-aware None-preserving ratios; honest non-trivial component).

## M6.2 — Query-vs-library search (`run_m6_2_search.py`)

Reuses M6.1 to rank every other library member against a query clip.
Three operator-supplied Twinkle clips (`twinkle_box.mp3`,
`twinkle_harmonica.wav`, `twinkle_people.m4a`) added — same melody,
three timbres.

Headline (`twinkle_box` query):

| rank | candidate              | score | verdict                |
|-----:|------------------------|------:|------------------------|
| 1    | twinkle_box_tstretch   | 0.479 | partial melodic match  |
| 2    | twinkle_harmonica      | 0.284 | partial melodic match  |
| 3-7  | (unrelated, tied)      | 0.164 | insufficient melodic content |

All four pre-set conditions met. Architect-review fixes: 4-non-trivial
verdict gate; per-query PASS/FAIL/N/A self-check; tied ranks visible.

## M6.3 — Small-library retrieval (`run_m6_3_retrieval.py`)

Pre-set bar: for each of 3 Twinkle queries, does any Twinkle-family
relative appear in the **top 3 dense ranks** (tied scores share the
same rank level)?

Library = 9 candidates (3 real twinkle + 1 synthetic twinkle transform
+ orchestra / rock / flute / highenergy / polyphonic).

**3/3 queries pass.** All 7 pre-set conditions met. One pass is
explicitly labelled `borderline` (`twinkle_people` — top-1 is unrelated
but `twinkle_box_tstretch` reaches rank 3). Architect-review fixes:
dense-rank semantics; spec-faithful "max(relative) >= min(unrelated)"
check; explicit `PASS (borderline)` when top-1 is unrelated.

## M6.4 — Family-retrieval demo (`run_m6_4_family_retrieval.py`)

Stronger question: given a Twinkle query, does the system retrieve the
**whole family** of Twinkle clips ahead of unrelated ones?

| Query                | Family in top 3 | Family in top 5 | Best family outranks all non-family |
|----------------------|:---------------:|:---------------:|:-----------------------------------:|
| `twinkle_box`        | 3               | 3               | YES                                 |
| `twinkle_harmonica`  | 2               | 3               | YES                                 |
| `twinkle_people`     | 1               | 1               | NO (weak-evidence, flagged)         |

All 5 pre-set conditions met. The voice query (`twinkle_people`) is
explicitly flagged as weak-evidence (only 2 non-trivial intervals
recovered by the M5.6 extractor) — the honesty guarantee is asserted in
the script's self-check, not just printed.

Architect-review fixes: replaced a tautological cond4 with a real check
(every nt<4 query must be marked weak AND `twinkle_people` must still
be weak); dense-rank semantics called out in docs.

## M6.5 — Multi-family retrieval validation (`run_m6_5_multi_family.py`) — NEGATIVE

The deliberate generalization test: does the M6.4 result hold for a
second, independently-recorded melody under the *same* locked pipeline,
with no per-family tuning?

Family 2: **Mary Had a Little Lamb**, three timbres
(`lamb_solo.mp3`, `lamb_group.mp3`, `lamb_male.mp3`) — operator-supplied,
attached to release `samples-v3`.

Library = M6.3 library (9) + the three Lamb clips = 12 candidates.

Discipline (declared before the run):

* No per-family tuning.
* No scoring changes.
* No extractor edits.
* Honest weak-evidence labelling preserved.

### Headline (all six queries)

| query              | family | top3 hits | top5 hits | best-same-family outranks all-other |
|--------------------|:------:|:---------:|:---------:|:-----------------------------------:|
| `twinkle_box`        | F1 | 2 | 3 | YES |
| `twinkle_harmonica`  | F1 | 1 | 2 | NO  |
| `twinkle_people`     | F1 | 1 | 1 | NO (weak) |
| `lamb_solo`          | F2 | 0 | 1 | NO (weak) |
| `lamb_group`         | F2 | 1 | 2 | NO |
| `lamb_male`          | F2 | 0 | 1 | NO (weak) |

### Pre-set pass conditions (declared before the run)

| # | condition                                                | result |
|--:|----------------------------------------------------------|--------|
| 1 | >= 2 queries from the new family                         | PASS   |
| 2 | family-2 hit in top 3 for >= 2 queries                   | **FAIL** (1/3) |
| 3 | best family-2 outranks all-other for >= 2 queries        | **FAIL** (0/3) |
| 4 | no outside-family clip labelled a strong / partial match | **FAIL** (`polyphonic` repeatedly tagged "partial melodic match") |
| 5 | Twinkle behaviour does not regress                       | **FAIL** (`twinkle_box` top-3 family hits drop 3->2 and `twinkle_harmonica` top-3 drops 2->1 because Lamb clips now occupy ranks 1-3 for those queries -- a real behavioural change. The `outranks` field for `twinkle_harmonica` also flips YES->NO, but that is partly apples-to-oranges: M6.5 uses the stricter 'outranks-all-other' comparator (Lamb counts as 'other'), where M6.4 only had to beat non-family clips. We deliberately do NOT downgrade the comparator to look better; both effects are honest consequences of adding Family 2.) |
| 6 | weak-evidence cases honestly flagged                     | PASS   |
| 7 | fresh-clone reproducible                                 | PASS (verified externally) |

**M6.5 result: FAIL** (4 of 7 pre-set conditions fail).

### Honest interpretation

The Twinkle family is the locked-extractor + locked-similarity
pipeline's good case, not its general case. The Lamb clips show that
when the pitch tracker recovers fewer non-trivial intervals (2-3 per
clip on these recordings), the similarity scores collapse into the same
narrow band as the unrelated clips, and family-level separation
disappears. Twinkle's family separation in M6.4 was real, but it
relied on (a) the unusually clean interval structure of the Twinkle
recordings the operator chose, and (b) the absence of any other
melodic family in the library to compete with it.

The bottleneck is upstream — the M5.6 pitch tracker on weak-melodic
material — not the retrieval layer. M5.7 (pyin) and M5.8 (HPSS) were
already tested and rejected for the M3-M5 benchmark; M5.9 (CREPE) was
abandoned mid-install. A real fix here is a better front-end pitch
tracker, not more retrieval engineering.

This is the result the operator explicitly asked us to be willing to
report. **No tuning was applied to make M6.5 pass.**

## Open issues (tracked, not hidden)

* **rock time_stretch = 4/8** since M5.3. Diagnosed as upstream cqt onset
  placement on percussive material, not the pitch window.
* **polyphonic = 5/24** is now believed to be pitch-tracker limited
  (pyin gets 10/24 there but breaks other clips; CREPE not yet tested).
* **voice-query family retrieval (`twinkle_people`)** remains a real
  pipeline limit — needs a better front-end pitch tracker for voice,
  not more retrieval engineering.
* **multi-family generalization (M6.5 NEGATIVE)** — the locked
  extractor + similarity pipeline does not generalise to a second
  independently-recorded melodic family without per-family tuning.
  The honest read is that the Twinkle result is closer to a special
  case than to a general retrieval claim at the current pipeline
  maturity.
