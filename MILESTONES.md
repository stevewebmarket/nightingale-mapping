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

## Open issues (tracked, not hidden)

* **rock time_stretch = 4/8** since M5.3. Diagnosed as upstream cqt onset
  placement on percussive material, not the pitch window.
* **polyphonic = 5/24** is now believed to be pitch-tracker limited
  (pyin gets 10/24 there but breaks other clips; CREPE not yet tested).
