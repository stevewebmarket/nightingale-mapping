# The Nightingale Mapping

**A bidirectional translation layer between mathematical structures and sound.**

### Vision
We are building a ladder of structure-preserving correspondences so that mathematical structures (ratios, sequences, symmetries, scaling, recursion, hierarchies…) can be rendered as sound, and real sound can be decoded back into its underlying mathematical form.

### Current Achievements
- Clean ladder: Levels 2–7 (ratios, sequences, symmetries, scaling, recursion) with Fraction decoder
- Real-audio invariance demonstrated on orchestral and rock recordings
- Working bidirectional prototype: sound → ladder → regenerated sound with measurable round-trip fidelity

### Latest Results (orchestra + rock)

| Test                        | Orchestra          | Rock                        |
|-----------------------------|--------------------|-----------------------------|
| Pitch shift 1.5×            | 7/8                | 8/8 (octave-folded)         |
| Time stretch 1.5×           | 8/8                | 7/8 (octave-folded)         |
| Bidirectional round-trip    | 8/8                | 8/8 (non-trivial)           |

### How to Run (start here)

```bash
# Clone the repo
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping

# Run the baseline bidirectional test
python run_nightingale_baseline.py
```

This will:

- Load orchestra and rock samples
- Extract ladder structures
- Regenerate sound from the ladder
- Show round-trip fidelity

### Repository Structure

- `run_nightingale_baseline.py` — canonical entry point (run this)
- `bidirectional_prototype.py` — core bidirectional code
- `ladder/` — core ladder implementation (Levels 2–7)
- `/archive` — old experiments (not needed for baseline)

### Next Steps

- Scale self-improvement loops
- Improve extractor for more complex audio
- Reach stable bidirectional layer suitable for broader applications
