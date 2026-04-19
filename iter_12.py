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
import librosa
from scipy.spatial.distance import cosine

# Function to get chroma vectors at specific times
def chroma_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)
    time_bins = librosa.frames_to_time(np.arange(chroma.shape[1]), sr=sr_in, hop_length=hop_length)
    interp_chroma = np.array([np.interp(times, time_bins, chroma[i]) for i in range(12)])
    return interp_chroma.T  # shape (len(times), 12)

# Create synthetic melody: concatenate 8 tones with increasing freqs (e.g., harmonic series)
freqs = [220, 440, 660, 880, 1100, 1320, 1540, 1760]  # A3 and harmonics
dur = 0.8
synthetic = np.concatenate([generate_tone(f, dur) for f in freqs])
synth_sr = sr  # 44100

# Detect onsets and get chroma
original_onsets = detect_onsets(synthetic, synth_sr, max_onsets=8)
orig_chroma = chroma_at_times(synthetic, original_onsets, synth_sr)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(synthetic, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_chroma = chroma_at_times(shifted, shifted_onsets, synth_sr)
    
    semitones = 12 * np.log2(factor)
    shift = int(round(semitones)) % 12
    
    similarities = []
    for i in range(len(original_onsets)):
        orig_vec = np.roll(orig_chroma[i], -shift)
        shift_vec = shifted_chroma[i]
        if np.linalg.norm(orig_vec) > 0 and np.linalg.norm(shift_vec) > 0:
            sim = 1 - cosine(orig_vec, shift_vec)
            similarities.append(sim)
    
    avg_sim = np.mean(similarities) if similarities else 0
    matches = sum(1 for s in similarities if s >= 0.9)
    print(f"Factor {factor} (shift {shift}): Avg similarity: {round(avg_sim, 4)}, Matches >=0.9: {matches}/{len(similarities)}")
    print(f"Similarities: {[round(s, 4) for s in similarities]}")
