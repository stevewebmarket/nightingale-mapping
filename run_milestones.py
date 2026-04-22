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

DEFAULT_CONFIG = {
    "onset_delta": 0.05,
    "fmin": 50,
    "fmax": 16000,
    "tolerance_pct": 0.01,
    # M5.2/M5.3: CQT-based onset envelope is the new default.  Beat the
    # baseline detector in the M5.2 ablation (commit 0a2790b): polyphonic
    # detected onsets 5/8 -> 8/8 across all transforms; orchestra/synthetic
    # held; flute 16/24 -> 22/24; documented regression: rock time_stretch
    # 7/8 -> 4/8.  Set onset_mode="baseline" to recover the M3.x detector.
    "onset_mode": "cqt_flux",
}


def load_clip(path):
    audio, _ = librosa.load(path, sr=SR, duration=CLIP_SECONDS)
    return audio


def _cqt_onset_envelope(audio):
    C = np.abs(librosa.cqt(y=audio, sr=SR))
    S = librosa.amplitude_to_db(C, ref=np.max)
    return librosa.onset.onset_strength(sr=SR, S=S)


def detect_onsets(audio, cfg=None, n=NUM_NOTES):
    cfg = cfg or DEFAULT_CONFIG
    mode = cfg.get("onset_mode", "cqt_flux")
    delta = cfg.get("onset_delta", 0.05)
    if mode == "cqt_flux":
        env = _cqt_onset_envelope(audio)
        onsets = librosa.onset.onset_detect(
            onset_envelope=env, sr=SR, units='time',
            delta=delta, wait=4, backtrack=True,
        )
    elif mode == "baseline":
        onsets = librosa.onset.onset_detect(
            y=audio, sr=SR, units='time',
            delta=delta, wait=4, backtrack=True,
        )
    else:
        raise ValueError(f"unknown onset_mode: {mode!r}")
    return onsets[:n]


def pitch_at(audio, t, cfg=None):
    cfg = cfg or DEFAULT_CONFIG
    # Match the proposal's analysis window: t-0.15s to t+0.25s (0.4s total)
    start = max(0, int((t - 0.15) * SR))
    end = min(len(audio), int((t + 0.25) * SR))
    seg = audio[start:end]
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50), fmax=cfg.get("fmax", 16000), sr=SR)
    valid = f0[f0 > cfg.get("fmin", 50)]
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


def within_tolerance(value, target, cfg=None):
    pct = (cfg or DEFAULT_CONFIG).get("tolerance_pct", TOLERANCE_PCT)
    return abs(value - target) / target <= pct


def pitch_shift_resample(audio, factor=SHIFT_FACTOR):
    """Pure-resampling pitch shift: the audio plays 'factor'x faster, raising
    pitch by 'factor'x AND compressing duration by 1/factor.  This matches
    the methodology used to produce the published baseline numbers."""
    # Lie to librosa: pretend the source was at SR*factor, ask for output at SR.
    # This compresses duration by 1/factor and raises pitch by factor.
    return librosa.resample(audio, orig_sr=int(SR * factor), target_sr=SR)


def score_pitch_shift(audio, label, cfg=None):
    cfg = cfg or DEFAULT_CONFIG
    onsets = detect_onsets(audio, cfg)
    shifted_audio = pitch_shift_resample(audio, SHIFT_FACTOR)

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t, cfg)
        p_shift = pitch_at(shifted_audio, t / SHIFT_FACTOR, cfg)
        if p_orig is None or p_shift is None:
            raw.append(None); folded.append(None); continue
        ratio = p_shift / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, SHIFT_FACTOR))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, SHIFT_FACTOR, cfg))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, SHIFT_FACTOR, cfg))
    return {
        'label': label, 'test': 'pitch_shift',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def score_time_stretch(audio, label, cfg=None):
    cfg = cfg or DEFAULT_CONFIG
    onsets = detect_onsets(audio, cfg)
    stretched = librosa.effects.time_stretch(y=audio, rate=1 / SHIFT_FACTOR)

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t, cfg)
        p_stretch = pitch_at(stretched, t * SHIFT_FACTOR, cfg)
        if p_orig is None or p_stretch is None:
            raw.append(None); folded.append(None); continue
        ratio = p_stretch / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, 1.0))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, 1.0, cfg))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, 1.0, cfg))
    return {
        'label': label, 'test': 'time_stretch',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def score_composition(audio, label, cfg=None):
    cfg = cfg or DEFAULT_CONFIG
    onsets = detect_onsets(audio, cfg)
    shifted = pitch_shift_resample(audio, SHIFT_FACTOR)
    composed = librosa.effects.time_stretch(y=shifted, rate=1 / SHIFT_FACTOR)

    raw = []
    folded = []
    for t in onsets:
        p_orig = pitch_at(audio, t, cfg)
        p_comp = pitch_at(composed, t, cfg)
        if p_orig is None or p_comp is None:
            raw.append(None); folded.append(None); continue
        ratio = p_comp / p_orig
        raw.append(ratio)
        folded.append(octave_fold(ratio, SHIFT_FACTOR))

    n_raw = sum(1 for r in raw if r is not None and within_tolerance(r, SHIFT_FACTOR, cfg))
    n_fold = sum(1 for r in folded if r is not None and within_tolerance(r, SHIFT_FACTOR, cfg))
    return {
        'label': label, 'test': 'composition',
        'raw': raw, 'folded': folded,
        'raw_score': n_raw, 'folded_score': n_fold,
        'total': len(onsets),
    }


def compute_milestone_scores(orchestra, rock, cfg=None):
    """Run the six milestone cases and return per-case results.
    Each result has 'within_tolerance' (folded_score) and 'total_notes' (total).
    """
    cfg = cfg or DEFAULT_CONFIG
    out = []
    for clip, label in [(orchestra, "Orchestra"), (rock, "Rock")]:
        for fn in (score_pitch_shift, score_time_stretch, score_composition):
            r = fn(clip, label, cfg)
            r["within_tolerance"] = r["folded_score"]
            r["total_notes"] = r["total"]
            out.append(r)
    return out


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
