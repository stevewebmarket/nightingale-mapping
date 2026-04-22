"""
The Nightingale Mapping — Milestone Tests M1.2 and M1.4

Single reproducible entry point. Run with:

    python run_milestones.py

Requires `orchestra.wav` and `rock.wav` in the same directory.
Get them via:  python scripts/fetch_samples.py

What this script measures, on each clip independently:

  M1.2 (Pitch shift)
    - Pitch-shift the waveform by 1.5x via resampling.
    - Detect 8 onsets in the original.
    - Sample the shifted waveform at the matched onsets (orig_onset / 1.5).
    - For each note, take the median YIN pitch and compute
      shifted_pitch / original_pitch.  Expect ~1.5.
    - Score = how many of the 8 notes land within 1% of 1.5,
      after octave-folding (YIN can lock onto any harmonic).

  Time stretch
    - Phase-vocoder time-stretch by 1.5x longer (librosa rate=1/1.5).
    - Sample stretched waveform at orig_onset * 1.5.
    - Pitch should be preserved.  Expect stretched/original ~1.0.
    - Score = within 1% of 1.0, octave-folded.

  M1.4 (Composition: pitch shift + time stretch)
    - Apply both transforms back-to-back: shift first, then stretch.
    - Sample at orig_onset * 1.5 / 1.5 = orig_onset (since the
      shift compresses time by 1/1.5 and the stretch re-expands by 1.5).
    - Pitch should be ~1.5x.  Expect within 1% of 1.5 octave-folded.
    - This is the "no drift" check: the two transforms compose.
"""

import os
import sys
import numpy as np
import librosa

SR = 44100
CLIP_SECONDS = 15
NUM_NOTES = 8
SHIFT_FACTOR = 1.5
TOLERANCE_PCT = 0.01  # within 1%


def load_clip(path):
    audio, _ = librosa.load(path, sr=SR, duration=CLIP_SECONDS)
    return audio


def detect_onsets(audio, n=NUM_NOTES):
    onsets = librosa.onset.onset_detect(
        y=audio, sr=SR, units='time', delta=0.05, wait=4, backtrack=True
    )
    return onsets[:n]


def pitch_at(audio, t, fmax=16000):
    # Match the proposal's analysis window: t-0.15s to t+0.25s (0.4s total)
    start = max(0, int((t - 0.15) * SR))
    end = min(len(audio), int((t + 0.25) * SR))
    seg = audio[start:end]
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=50, fmax=fmax, sr=SR)
    valid = f0[f0 > 50]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


def octave_fold(ratio, target):
    """Fold ratio by powers of 2 toward target.  YIN can lock onto any harmonic."""
    if ratio is None or ratio <= 0:
        return ratio
    r = ratio
    # bring into the octave around target
    while r < target / 1.5:
        r *= 2
    while r > target * 1.5:
        r /= 2
    return r


def within_tolerance(value, target, pct=TOLERANCE_PCT):
    return abs(value - target) / target <= pct


def pitch_shift_resample(audio, factor=SHIFT_FACTOR):
    """Pure-resampling pitch shift: the audio plays 'factor'x faster, raising
    pitch by 'factor'x AND compressing duration by 1/factor.  This matches
    the methodology used to produce the published baseline numbers."""
    # Lie to librosa: pretend the source was at SR*factor, ask for output at SR.
    # This compresses duration by 1/factor and raises pitch by factor.
    return librosa.resample(audio, orig_sr=int(SR * factor), target_sr=SR)


def score_pitch_shift(audio, label):
    onsets = detect_onsets(audio)
    shifted_audio = pitch_shift_resample(audio, SHIFT_FACTOR)

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t)
        # resample compressed time by 1/SHIFT_FACTOR, so onset lands at t/SHIFT_FACTOR
        p_shift = pitch_at(shifted_audio, t / SHIFT_FACTOR)
        if p_orig is None or p_shift is None:
            raw.append(None)
            folded.append(None)
            continue
        ratio = p_shift / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, SHIFT_FACTOR))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, SHIFT_FACTOR))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, SHIFT_FACTOR))
    return {
        'label': label, 'test': 'pitch_shift',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def score_time_stretch(audio, label):
    onsets = detect_onsets(audio)
    stretched = librosa.effects.time_stretch(y=audio, rate=1 / SHIFT_FACTOR)

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t)
        p_stretch = pitch_at(stretched, t * SHIFT_FACTOR)
        if p_orig is None or p_stretch is None:
            raw.append(None)
            folded.append(None)
            continue
        ratio = p_stretch / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, 1.0))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, 1.0))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, 1.0))
    return {
        'label': label, 'test': 'time_stretch',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def score_composition(audio, label):
    """Apply resample-shift (1.5x faster, +5th) THEN time-stretch (1.5x longer),
    so durations cancel out.  Pitch should still be 1.5x original at orig time."""
    onsets = detect_onsets(audio)
    shifted = pitch_shift_resample(audio, SHIFT_FACTOR)         # 1/1.5x duration, 1.5x pitch
    composed = librosa.effects.time_stretch(y=shifted, rate=1 / SHIFT_FACTOR)  # back to orig duration

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t)
        # net duration change = (1/1.5) * 1.5 = 1.0, so onset stays at t
        p_comp = pitch_at(composed, t)
        if p_orig is None or p_comp is None:
            raw.append(None)
            folded.append(None)
            continue
        ratio = p_comp / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, SHIFT_FACTOR))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, SHIFT_FACTOR))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, SHIFT_FACTOR))
    return {
        'label': label, 'test': 'composition',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def fmt(x):
    return f"{x:.3f}" if x is not None else "  -  "


def print_result(r):
    print(f"  [{r['label']}] {r['test']}")
    print(f"    raw ratios:    [{', '.join(fmt(v) for v in r['raw'])}]")
    print(f"    folded ratios: [{', '.join(fmt(v) for v in r['folded'])}]")
    print(f"    score: {r['raw_score']}/{r['total']} raw  |  {r['folded_score']}/{r['total']} octave-folded")


def main():
    for f in ("orchestra.wav", "rock.wav"):
        if not os.path.isfile(f):
            sys.stderr.write(f"Missing {f}.  Run: python scripts/fetch_samples.py\n")
            sys.exit(1)

    orchestra = load_clip("orchestra.wav")
    rock = load_clip("rock.wav")

    results = []
    print("=" * 70)
    print("Nightingale Mapping — Milestone Tests M1.2 + M1.4")
    print("=" * 70)
    for clip, label in [(orchestra, "Orchestra"), (rock, "Rock")]:
        print()
        for fn in (score_pitch_shift, score_time_stretch, score_composition):
            r = fn(clip, label)
            results.append(r)
            print_result(r)

    print()
    print("=" * 70)
    print("SUMMARY (octave-folded)")
    print("=" * 70)
    for label in ("Orchestra", "Rock"):
        rows = [r for r in results if r['label'] == label]
        print(f"\n{label}:")
        for r in rows:
            name = {'pitch_shift': 'Pitch shift', 'time_stretch': 'Time stretch',
                    'composition': 'Composition'}[r['test']]
            print(f"  {name:14s} {r['folded_score']}/{r['total']}")


if __name__ == "__main__":
    main()
