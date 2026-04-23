# The Nightingale Mapping

**A research probe into whether mathematical structure survives translation into sound.**

We test this by running real audio through systematic transforms (pitch shift, time
stretch, composition), extracting per-onset pitch ratios, and measuring how many
fall within 1% of the algebraically expected value.

**Latest capability (M6.3 / M6.4):** small-library **retrieval by relational
similarity** for the Twinkle melody family — given a Twinkle query, the
system recovers the Twinkle family from a mixed library using extracted
interval structure, not raw timbre. See [Retrieval headline](#retrieval-headline-m63--m64) below.

**M6.5 (multi-family validation): NEGATIVE.** Adding a second melody
family (Mary Had a Little Lamb, three timbres) under the *same* locked
extractor + similarity pipeline — no per-family tuning — does *not*
reproduce the Twinkle result. Lamb queries fail to retrieve their own
family ahead of unrelated clips, and the Lamb clips also disrupt some
Twinkle retrievals. The honest reading: the Twinkle result is closer to
a *special case* than to a general-purpose retrieval claim at the
current pipeline maturity. Details in [MILESTONES.md § M6.5](MILESTONES.md).

## Headline (as of M5.6, commit `d332f54`)

| Clip            | Total | Score  |
|-----------------|-------|--------|
| orchestra       | 24/24 | 1.0000 |
| flute           | 22/24 | 0.9167 |
| synthetic_just  | 23/24 | 0.9583 |
| rock            | 18/24 | 0.7500 |
| highenergy      | 15/24 | 0.6250 |
| polyphonic      |  5/24 | 0.2083 |
| **TOTAL**       | **107/144** | **0.7431** |

6 clips × 3 transforms (pitch_shift 1.5×, time_stretch 1.5×, composition) ×
8 notes each, octave-folded, deterministic across runs.

Open issues tracked, not hidden: rock time_stretch sits at 4/8 (regression
introduced when `cqt_flux` onset detection was locked in M5.3); polyphonic
remains the largest "other_errors" bucket and is now believed to be
pitch-tracker limited (see M5.7).

## Retrieval headline (M6.3 / M6.4)

In a **9-clip mixed library** (3 real Twinkle recordings on different
instruments + 1 synthetic Twinkle time-stretch + 5 unrelated clips), all
3 Twinkle queries retrieve a Twinkle-family relative in the top 3 dense
ranks (tied scores share the same rank level). M6.4 family-retrieval
summary:

| Query                | Family in top 3 | Family in top 5 | Best family outranks all non-family |
|----------------------|:---------------:|:---------------:|:-----------------------------------:|
| `twinkle_box`        | 3               | 3               | YES                                 |
| `twinkle_harmonica`  | 2               | 3               | YES                                 |
| `twinkle_people`     | 1 (borderline)  | 1 (borderline)  | NO (weak-evidence, flagged)         |

The borderline / weak-evidence case is honest: the pitch tracker recovers
only 2 non-trivial intervals from the voice clip, so its rows are
explicitly labelled `insufficient melodic content` and the verdict gate
refuses to call it a structural match.

## How to reproduce

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping
pip install -r requirements.txt
python scripts/fetch_samples.py        # fetches v1+v2+v3 release assets
python run_m4_1_benchmark.py           # locked benchmark, prints table above
python run_m5_1_diagnostics.py         # per-onset failure classification

# Retrieval (M6.3 / M6.4):
python run_m6_3_retrieval.py           # small-library retrieval
python run_m6_4_family_retrieval.py    # family-retrieval demo
python run_m6_5_multi_family.py        # multi-family validation (NEGATIVE)
```

The default extractor lives in `run_milestones.py`:

```python
DEFAULT_CONFIG = {
    "onset_mode":  "cqt_flux",            # locked in M5.3
    "pitch_mode":  "adaptive_rms_attack", # locked in M5.6
    "fmin": 50, "fmax": 16000, "tolerance_pct": 0.01,
    "onset_delta": 0.05,
}
```

Both locked modes have a `"baseline"` selectable for compatibility and
future comparisons (no destructive overwrite).

## Milestone log

See [MILESTONES.md](MILESTONES.md). Each milestone is one commit, has a
pre-set pass condition declared *before* the run, reports headline numbers,
notes regressions openly, and is reproducible from a fresh clone.

## What this does *not* claim

* It does not claim the algebraic relationship is preserved with arbitrary
  precision under arbitrary transforms.
* It does not claim polyphonic pitched material is solved (5/24).
* It does not claim CREPE or other neural pitch trackers were beaten —
  CREPE is currently skipped for environment reasons (see M5.7).

## Current limitations (M6 retrieval)

* Voice / weak-melodic clips remain hard. The pitch tracker is the
  bottleneck: when fewer than ~4 non-trivial intervals survive
  extraction, the similarity layer correctly refuses to claim a
  structural match (and family-retrieval falls back to the borderline
  path, as `twinkle_people` shows above).
* Retrieval is meaningful only when enough non-trivial intervals
  survive extraction in *both* the query and the candidate.
* The current extractor is locked at M5.6; M5.7 (pyin) and M5.8 (HPSS)
  were tested as alternatives and did not improve on it for melodic
  retrieval. M5.9 (CREPE) was abandoned mid-install — not benchmarked.
  See [MILESTONES.md](MILESTONES.md).
* **Multi-family generalization is not yet demonstrated.** M6.5 added a
  Mary-Had-a-Little-Lamb family and ran the same pipeline unchanged;
  family-2 retrieval failed all the per-family pre-set conditions, and
  Twinkle retrieval also degraded slightly because Lamb clips occupy
  near-identical score ranges. The next real improvement target is the
  front-end pitch tracker (voice / weak-melodic clips), not more
  retrieval engineering.

## License

See `LICENSE`.
