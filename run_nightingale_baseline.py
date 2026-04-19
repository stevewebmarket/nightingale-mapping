# =============================================================================
# The Nightingale Mapping — Baseline Bidirectional Test
# Run this file to see the current state
# =============================================================================

import numpy as np
from fractions import Fraction
import librosa

sr = 44100

# Core helpers
def generate_tone(freq, dur=0.8):
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def normalize(sound):
    return sound / (np.max(np.abs(sound)) + 1e-8)

def extract_pitch_sequence_hybrid(audio, sr=44100, sound_type='harmonic', max_onsets=8):
    if len(audio) < sr:
        return []
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    onsets_time = librosa.onset.onset_detect(y=audio, sr=sr, units='time', delta=0.05, wait=4, backtrack=True)
    onsets_time = onsets_time[:max_onsets]

    pitch_sequence = []
    for onset_time in onsets_time:
        start = int((onset_time - 0.15) * sr)
        end = int((onset_time + 0.25) * sr)
        if start < 0: start = 0
        if end > len(audio): end = len(audio)
        segment = audio[start:end]
        if len(segment) < 512:
            continue
        f0 = librosa.yin(segment, fmin=50, fmax=16000, sr=sr)
        valid_f0 = f0[f0 > 50]
        if len(valid_f0) > 0:
            pitch = np.median(valid_f0)
            pitch_sequence.append(pitch)

    if not pitch_sequence:
        return []

    base = pitch_sequence[0]
    ratio_seq = [Fraction(p / base).limit_denominator(16) for p in pitch_sequence]
    return ratio_seq

def extract_ladder_from_audio(audio, sr, sound_type='harmonic'):
    ratio_seq = extract_pitch_sequence_hybrid(audio, sr, sound_type)
    if not ratio_seq:
        return None
    return {'ratios': ratio_seq, 'num_notes': len(ratio_seq)}

def generate_sound_from_ladder(ladder, sr=44100):
    if not ladder or 'ratios' not in ladder:
        return None
    numeric_seq = [float(f) for f in ladder['ratios']]
    tones = [generate_tone(220 * v) for v in numeric_seq]
    return normalize(np.concatenate(tones))

def run_bidirectional_test(audio, sr, label, sound_type='harmonic'):
    print(f"\n=== Bidirectional Test: {label} ===")
    ladder = extract_ladder_from_audio(audio, sr, sound_type)
    if not ladder:
        print("  Failed to extract ladder")
        return
    print(f"  Extracted {ladder['num_notes']} elements: {[str(f) for f in ladder['ratios']]}")

    regenerated = generate_sound_from_ladder(ladder, sr)
    if regenerated is None:
        print("  Failed to regenerate")
        return

    # Fixed slicing round-trip
    num_notes = ladder['num_notes']
    segment_length = len(regenerated) // num_notes
    re_extracted = []
    for i in range(num_notes):
        segment = regenerated[i*segment_length:(i+1)*segment_length]
        spec = np.abs(np.fft.rfft(segment))
        freqs = np.fft.rfftfreq(len(segment), 1/sr)
        dominant = freqs[np.argmax(spec)]
        ratio = dominant / 220.0
        frac = Fraction(ratio).limit_denominator(16)
        re_extracted.append(frac)

    print(f"  Re-extracted: {[str(f) for f in re_extracted]}")
    matches = sum(1 for a, b in zip(ladder['ratios'], re_extracted) if a == b)
    print(f"  Round-trip exact match: {matches}/{num_notes}")
    print(f"✅ Test completed for {label}\n")

# =============================================================================
# Run baseline
# =============================================================================
print("The Nightingale Mapping — Baseline Bidirectional Test\n")

# Load your files (update paths if needed)
orchestra, sr_orch = librosa.load("orchestra.wav", sr=sr)
rock, sr_rock = librosa.load("rock.wav", sr=sr)

run_bidirectional_test(orchestra, sr_orch, "Orchestra sample", sound_type='harmonic')
run_bidirectional_test(rock, sr_rock, "Rock band sample", sound_type='harmonic')

print("Baseline test finished. Push this file + results to the repo.")
