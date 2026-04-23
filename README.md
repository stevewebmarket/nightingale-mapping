# The Nightingale Mapping

> **Status: locked for evaluation / packaging.**
> No active algorithm changes. The pipeline (extractor / similarity /
> retrieval) is frozen at the state described below. See
> [MILESTONES.md](MILESTONES.md) for the full milestone log.

---

## What this project does

A research probe into whether **mathematical structure survives
translation into sound**.

We test this by running real audio through systematic transforms (pitch
shift, time stretch, composition), extracting per-onset pitch ratios,
and measuring how many fall within 1% of the algebraically expected
value. The same extracted ratio sequences are then used as a relational
similarity feature for small-library retrieval.

Each milestone is one commit, declares its pass condition *before* the
run, reports headline numbers, and is reproducible from a fresh clone.

## Current strongest capability

**Small-library retrieval by structural similarity works on clean
instrumental melody families.**

In a 9-clip mixed library (3 real Twinkle recordings on different
instruments + 1 synthetic Twinkle time-stretch + 5 unrelated clips),
all 3 Twinkle queries retrieve a Twinkle-family relative in the top 3
dense ranks (M6.4):

| Query                | Family in top 3 | Family in top 5 | Best family outranks all non-family |
|----------------------|:---------------:|:---------------:|:-----------------------------------:|
| `twinkle_box`        | 3               | 3               | YES                                 |
| `twinkle_harmonica`  | 2               | 3               | YES                                 |
| `twinkle_people`     | 1 (borderline)  | 1 (borderline)  | NO (weak-evidence, flagged)         |

Underlying that is the locked M5.6 extractor (107/144 = 0.7431 on the
six-clip transform benchmark).

## Current limitation

**Retrieval does not yet generalize to voice-heavy clips when too
little non-trivial melodic structure survives extraction.**

M6.5 added a second melodic family (Mary Had a Little Lamb, three
timbres) and ran the same locked pipeline unchanged — no per-family
tuning, no scoring changes. The result is honestly NEGATIVE:

* Lamb queries: 1/3 got a family member into top 3; 0/3 outranked all
  other clips.
* Twinkle behaviour also degraded once Lamb was in the library
  (`twinkle_box` top-3 family hits dropped 3 → 2; `twinkle_harmonica`
  dropped 2 → 1).

The bottleneck is upstream — the M5.6 pitch tracker on weak-melodic
material — not the retrieval layer. M5.7 (pyin) and M5.8 (HPSS) were
tested and did not improve on M5.6; M5.9 (CREPE) was deferred /
abandoned mid-install (never benchmarked). Details in
[MILESTONES.md § M6.5](MILESTONES.md).

## Exact reproduction commands

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping
pip install -r requirements.txt

# Fetch all sample clips (samples-v1 + v2 + v3 from GitHub Releases):
python scripts/fetch_samples.py

# Working capability (M6.4):
python run_m6_4_family_retrieval.py

# Boundary case (M6.5 -- honest NEGATIVE result):
python run_m6_5_multi_family.py
```

Optional, to reproduce earlier headline numbers:

```bash
python run_m4_1_benchmark.py           # M5.6 locked benchmark, prints 107/144 table
python run_m5_1_diagnostics.py         # per-onset failure classification
python run_m6_3_retrieval.py           # small-library retrieval (M6.3)
```

## Results summary

| Milestone | Headline                                                   | Status |
|-----------|------------------------------------------------------------|--------|
| M5.6      | Locked transform-invariance baseline: **107/144 = 0.7431** | LOCKED |
| M6.4      | Twinkle family retrieval works (top-3 hits = 3 / 2 / 1)    | PASS   |
| M6.5      | Second sung family (Lamb) fails honestly under same pipeline | FAIL (boundary) |

## Repo status

Locked for evaluation / packaging at canonical `main`. No new milestone
scripts, no algorithm / metric / extraction / similarity / retrieval
changes from this point. Documentation, hygiene, and verification only.

## What this does *not* claim

* It does not claim the algebraic relationship is preserved with arbitrary
  precision under arbitrary transforms.
* It does not claim polyphonic pitched material is solved (5/24).
* It does not claim CREPE or other neural pitch trackers were beaten —
  CREPE was deferred / abandoned mid-install (M5.9), not benchmarked.
* It does not claim multi-family / cross-genre retrieval generalisation
  (M6.5 NEGATIVE).

## Reference: locked extractor

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

## Reference: M5.6 transform benchmark

| Clip            | Total      | Score  |
|-----------------|------------|--------|
| orchestra       | 24/24      | 1.0000 |
| flute           | 22/24      | 0.9167 |
| synthetic_just  | 23/24      | 0.9583 |
| rock            | 18/24      | 0.7500 |
| highenergy      | 15/24      | 0.6250 |
| polyphonic      |  5/24      | 0.2083 |
| **TOTAL**       | **107/144**| **0.7431** |

6 clips × 3 transforms (pitch_shift 1.5×, time_stretch 1.5×, composition)
× 8 notes each, octave-folded, deterministic across runs.

## License

See `LICENSE`.
