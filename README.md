# The Nightingale Mapping

**A bidirectional translation layer between mathematical structures and sound.**

### Vision
We are building a ladder of structure-preserving correspondences so that mathematical structures (ratios, sequences, symmetries, scaling, recursion, hierarchies…) can be rendered as sound — and real sound can be decoded back into its underlying mathematical form.

### Current Achievements
- Clean ladder: Levels 2–7 (ratios, sequences, symmetries, scaling, recursion) with Fraction decoder for exact rational representation.
- Real-audio invariance demonstrated on orchestral and rock recordings (pitch shift + time stretch).
- Working bidirectional prototype: sound → ladder → regenerated sound with measurable round-trip fidelity.

### Latest Results (orchestra + rock)

Reproducible via `python run_milestones.py` — three identical runs. Full
method, table, and caveats in [MILESTONES.md](MILESTONES.md).

| Test                        | Orchestra          | Rock                          |
|-----------------------------|--------------------|-------------------------------|
| Pitch shift 1.5×            | 7/8                | 8/8 (octave-folded)           |
| Time stretch 1.5×           | 8/8                | 7/8 (octave-folded)           |
| Composition (shift+stretch) | 7/8                | 7/8 (octave-folded)           |
| Bidirectional round-trip    | 8/8                | 8/8 (non-trivial)             |

44 of 48 measurements within 1% of target across two clips × three transforms × eight notes.

### How to Run (start here)

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping

# Download reference samples (permanent links)
python fetch_samples.py   # or download manually from the samples-v1 release

# Run the baseline bidirectional test
python run_nightingale_baseline.py

# Or run the full milestone check (M1.2 pitch shift + time stretch + M1.4 composition)
python run_milestones.py
