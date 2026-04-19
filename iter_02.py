"""Persistent helpers prepended to every Grok-proposed iteration."""
import numpy as np
from fractions import Fraction
from scipy.io import wavfile
import librosa
import warnings
warnings.filterwarnings('ignore')

sr = 44100

def generate_tone(freq, dur=0.8, sample_rate=sr):
    t = np.linspace(0, dur, int(sample_rate * dur), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def normalize(s):
    return s / (np.max(np.abs(s)) + 1e-8)

def pitch_shift_real(sound, factor=1.5):
    """REAL pitch shift via resampling. Changes pitch by factor, duration by 1/factor."""
    if factor <= 0:
        factor = 1.0
    new_len = max(1, int(len(sound) / factor))
    indices = np.linspace(0, len(sound), new_len)
    return normalize(np.interp(indices, np.arange(len(sound)), sound))

def time_stretch_real(sound, factor=1.5):
    """REAL time stretch via resampling. Changes duration by 1/factor, but ALSO changes pitch
    (true pitch-preserving stretch needs phase vocoder; this is the simple version)."""
    if factor <= 0:
        factor = 1.0
    new_len = max(1, int(len(sound) * factor))
    indices = np.linspace(0, len(sound), new_len)
    return normalize(np.interp(indices, np.arange(len(sound)), sound))

def get_sequence_from_melody(sound, num_notes):
    seg_len = len(sound) // num_notes
    seq = []
    for i in range(num_notes):
        seg = sound[i*seg_len:(i+1)*seg_len]
        spec = np.abs(np.fft.rfft(seg))
        freqs = np.fft.rfftfreq(len(seg), 1/sr)
        seq.append(freqs[np.argmax(spec)])
    if not seq:
        return tuple()
    mn = min(seq)
    if mn == 0:
        return tuple((int(round(v)), 1) for v in seq)
    out = []
    for v in seq:
        f = Fraction(v/mn).limit_denominator(16)
        out.append((f.numerator, f.denominator))
    return tuple(out)

def yin_pitches_at_times(audio, times, sr_in=sr, fmin=50, fmax=16000):
    """YIN-extract median pitch at each onset time."""
    out = []
    for t in times:
        s = max(0, int((t - 0.15) * sr_in))
        e = min(len(audio), int((t + 0.25) * sr_in))
        seg = audio[s:e]
        if len(seg) < 2048:
            continue
        f0 = librosa.yin(seg, fmin=fmin, fmax=fmax, sr=sr_in)
        valid = f0[f0 > fmin]
        if len(valid) > 0:
            out.append(float(np.median(valid)))
    return out

def detect_onsets(audio, sr_in=sr, max_onsets=8, delta=0.05, wait=4):
    return list(librosa.onset.onset_detect(
        y=audio, sr=sr_in, units='time',
        delta=delta, wait=wait, backtrack=True
    ))[:max_onsets]

def load_audio(fn):
    rate, a = wavfile.read(fn)
    if a.ndim > 1:
        a = np.mean(a, axis=1)
    return a.astype(np.float32) / np.max(np.abs(a)), rate

birdsong, sr_bird   = load_audio("birdsong.wav")
orchestra, sr_orch  = load_audio("orchestra.wav")
rock, sr_rock       = load_audio("rock.wav")
SAMPLES = {"birdsong": (birdsong, sr_bird),
           "orchestra": (orchestra, sr_orch),
           "rock":      (rock, sr_rock)}


# === Grok-proposed iteration ===
import numpy as np
from fractions import Fraction

# Get sequence for original orchestra
orig_seq = get_sequence_from_melody(orchestra, 8)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(orchestra, factor)
    shifted_seq = get_sequence_from_melody(shifted, 8)
    
    # Check if sequences match exactly
    match = shifted_seq == orig_seq
    
    # Compute differences if not match
    if not match:
        diffs = [(Fraction(n1,d1) - Fraction(n2,d2)) for (n1,d1),(n2,d2) in zip(shifted_seq, orig_seq)]
    else:
        diffs = []
    
    print(f"Factor {factor}: Sequences match? {match}")
    print(f"Original seq: {[(n,d) for n,d in orig_seq]}")
    print(f"Shifted seq: {[(n,d) for n,d in shifted_seq]}")
    if diffs:
        print(f"Differences: {[float(f) for f in diffs]}")
