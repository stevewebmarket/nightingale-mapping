# Conversational loop transcript
Model: grok-4-latest
Start: Sun Apr 19 00:05:25 2026


## Iteration 1 (rc=0)

### Code
```python
import numpy as np

# Get original onsets and pitches for orchestra
original_onsets = detect_onsets(orchestra, sr_orch, max_onsets=8)
orig_pitches = yin_pitches_at_times(orchestra, original_onsets, sr_orch)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(orchestra, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_pitches = yin_pitches_at_times(shifted, shifted_onsets, sr_orch)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_pitches, shifted_pitches):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 0.1%
    matches = sum(1 for e in errors if abs(e) <= 0.1)
    print(f"Factor {factor}: Matches within 0.1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 0.1%: 7/8
Errors (%): [-0.0485, 0.0641, -0.0302, -0.0408, 0.0011, -0.0178, -0.0245, 7.822]
Factor 1.5: Matches within 0.1%: 5/8
Errors (%): [-0.1545, -0.1803, 0.0048, -0.0541, -0.01, -0.0317, -0.0173, 5.001]
Factor 1.75: Matches within 0.1%: 5/8
Errors (%): [-0.1975, -0.2836, -0.0118, -0.0678, -0.0408, -0.0553, -0.0275, 0.5282]
Factor 2.0: Matches within 0.1%: 5/8
Errors (%): [-0.3531, -0.1901, -0.0067, -0.0519, 0.0116, -0.0547, -0.0323, 1.1195]

```


## Iteration 2 (rc=0)

### Code
```python
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
```

### Output
```
Factor 1.25: Sequences match? False
Original seq: [(1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13)]
Shifted seq: [(1, 1), (125, 13), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13)]
Differences: [0.0, 0.0, 0.0, 0.0, 0.009615384615384616, 0.0, 0.0, 0.0]
Factor 1.5: Sequences match? False
Original seq: [(1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13)]
Shifted seq: [(1, 1), (125, 13), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13)]
Differences: [0.0, 0.0, 0.0, 0.0, 0.009615384615384616, 0.0, 0.0, 0.0]
Factor 1.75: Sequences match? True
Original seq: [(1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13)]
Shifted seq: [(1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13)]
Factor 2.0: Sequences match? False
Original seq: [(1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13)]
Shifted seq: [(1, 1), (77, 8), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13)]
Differences: [0.0, 0.009615384615384616, 0.0, 0.0, 0.009615384615384616, 0.0, 0.0, 0.0]

```


## Iteration 3 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Get sequence for original rock
orig_seq = get_sequence_from_melody(rock, 8)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(rock, factor)
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
```

### Output
```
Factor 1.25: Sequences match? True
Original seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Shifted seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Factor 1.5: Sequences match? True
Original seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Shifted seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Factor 1.75: Sequences match? True
Original seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Shifted seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Factor 2.0: Sequences match? True
Original seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]
Shifted seq: [(74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1)]

```


## Iteration 4 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Get sequence for original birdsong
orig_seq = get_sequence_from_melody(birdsong, 8)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(birdsong, factor)
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
```

### Output
```
Factor 1.25: Sequences match? True
Original seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Shifted seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Factor 1.5: Sequences match? True
Original seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Shifted seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Factor 1.75: Sequences match? True
Original seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Shifted seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Factor 2.0: Sequences match? True
Original seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]
Shifted seq: [(17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10)]

```


## Iteration 5 (rc=0)

### Code
```python
import numpy as np

# Get original onsets and pitches for birdsong
original_onsets = detect_onsets(birdsong, sr_bird, max_onsets=8)
orig_pitches = yin_pitches_at_times(birdsong, original_onsets, sr_bird)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(birdsong, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_pitches = yin_pitches_at_times(shifted, shifted_onsets, sr_bird)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_pitches, shifted_pitches):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 0.1%
    matches = sum(1 for e in errors if abs(e) <= 0.1)
    print(f"Factor {factor}: Matches within 0.1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 0.1%: 0/8
Errors (%): [110.4361, -0.133, -65.4012, 3.9916, -4.6202, 15.6432, -0.1688, 7.315]
Factor 1.5: Matches within 0.1%: 0/8
Errors (%): [213.295, -65.0019, -65.6431, 22.138, 4.4436, 10.5271, -12.29, 2.4837]
Factor 1.75: Matches within 0.1%: 0/8
Errors (%): [214.1152, -65.6932, -66.3581, 22.2262, 19.8857, 13.2352, -2.3296, -7.433]
Factor 2.0: Matches within 0.1%: 0/8
Errors (%): [210.0689, -65.998, -66.2371, 24.5936, 22.9626, 17.1154, -2.7605, -7.3212]

```


## Iteration 6 (rc=0)

### Code
```python
import numpy as np
import librosa

# Function to get spectral centroids at specific times
def centroids_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    centroids = librosa.feature.spectral_centroid(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)[0]
    time_bins = librosa.frames_to_time(np.arange(len(centroids)), sr=sr_in, hop_length=hop_length)
    interp_centroids = np.interp(times, time_bins, centroids)
    return interp_centroids

# Get original onsets and centroids for birdsong
original_onsets = detect_onsets(birdsong, sr_bird, max_onsets=8)
orig_centroids = centroids_at_times(birdsong, original_onsets, sr_bird)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(birdsong, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_centroids = centroids_at_times(shifted, shifted_onsets, sr_bird)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_centroids, shifted_centroids):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 1% (looser tolerance for centroid)
    matches = sum(1 for e in errors if abs(e) <= 1)
    print(f"Factor {factor}: Matches within 1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 1%: 3/8
Errors (%): [np.float64(-1.9664), np.float64(0.5134), np.float64(2.8167), np.float64(0.9096), np.float64(-1.6715), np.float64(0.0801), np.float64(7.0231), np.float64(1.3576)]
Factor 1.5: Matches within 1%: 3/8
Errors (%): [np.float64(-3.1222), np.float64(-0.3968), np.float64(3.6484), np.float64(0.83), np.float64(-3.2569), np.float64(-0.9765), np.float64(9.2836), np.float64(1.2461)]
Factor 1.75: Matches within 1%: 1/8
Errors (%): [np.float64(-3.203), np.float64(-1.1396), np.float64(4.7265), np.float64(2.201), np.float64(-2.7067), np.float64(0.4289), np.float64(9.9797), np.float64(1.5768)]
Factor 2.0: Matches within 1%: 1/8
Errors (%): [np.float64(-2.4281), np.float64(-2.3557), np.float64(4.3799), np.float64(2.625), np.float64(-2.6714), np.float64(0.8317), np.float64(10.3275), np.float64(2.4438)]

```


## Iteration 7 (rc=0)

### Code
```python
import numpy as np
import librosa

# Function to get spectral centroids at specific times
def centroids_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    centroids = librosa.feature.spectral_centroid(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)[0]
    time_bins = librosa.frames_to_time(np.arange(len(centroids)), sr=sr_in, hop_length=hop_length)
    interp_centroids = np.interp(times, time_bins, centroids)
    return interp_centroids

# Get original onsets and centroids for orchestra
original_onsets = detect_onsets(orchestra, sr_orch, max_onsets=8)
orig_centroids = centroids_at_times(orchestra, original_onsets, sr_orch)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(orchestra, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_centroids = centroids_at_times(shifted, shifted_onsets, sr_orch)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_centroids, shifted_centroids):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 1%
    matches = sum(1 for e in errors if abs(e) <= 1)
    print(f"Factor {factor}: Matches within 1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 1%: 0/8
Errors (%): [np.float64(-1.5249), np.float64(-15.4651), np.float64(-5.9505), np.float64(-2.3368), np.float64(32.4926), np.float64(-13.4148), np.float64(-3.1976), np.float64(-4.0871)]
Factor 1.5: Matches within 1%: 1/8
Errors (%): [np.float64(-2.5069), np.float64(-17.0172), np.float64(-1.7896), np.float64(0.6061), np.float64(42.8497), np.float64(-12.168), np.float64(-1.4728), np.float64(7.0102)]
Factor 1.75: Matches within 1%: 0/8
Errors (%): [np.float64(-4.3746), np.float64(-26.6103), np.float64(-10.7471), np.float64(11.6556), np.float64(33.3902), np.float64(-27.3999), np.float64(-4.0257), np.float64(6.4987)]
Factor 2.0: Matches within 1%: 0/8
Errors (%): [np.float64(-3.96), np.float64(-26.1348), np.float64(-11.446), np.float64(11.2891), np.float64(37.0269), np.float64(-32.9517), np.float64(-7.3908), np.float64(16.453)]

```


## Iteration 8 (rc=0)

### Code
```python
import numpy as np
import librosa

# Function to get spectral centroids at specific times
def centroids_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    centroids = librosa.feature.spectral_centroid(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)[0]
    time_bins = librosa.frames_to_time(np.arange(len(centroids)), sr=sr_in, hop_length=hop_length)
    interp_centroids = np.interp(times, time_bins, centroids)
    return interp_centroids

# Get original onsets and centroids for rock
original_onsets = detect_onsets(rock, sr_rock, max_onsets=8)
orig_centroids = centroids_at_times(rock, original_onsets, sr_rock)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(rock, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_centroids = centroids_at_times(shifted, shifted_onsets, sr_rock)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_centroids, shifted_centroids):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 1%
    matches = sum(1 for e in errors if abs(e) <= 1)
    print(f"Factor {factor}: Matches within 1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 1%: 0/8
Errors (%): [np.float64(-16.084), np.float64(-15.8804), np.float64(-14.023), np.float64(-13.5442), np.float64(-13.7101), np.float64(-8.9026), np.float64(-7.6934), np.float64(-6.6441)]
Factor 1.5: Matches within 1%: 0/8
Errors (%): [np.float64(-23.5013), np.float64(-23.8825), np.float64(-18.6871), np.float64(-17.048), np.float64(-18.1752), np.float64(-12.2184), np.float64(-10.0117), np.float64(-8.7529)]
Factor 1.75: Matches within 1%: 0/8
Errors (%): [np.float64(-28.4658), np.float64(-27.4472), np.float64(-22.8566), np.float64(-21.6387), np.float64(-21.8674), np.float64(-14.4217), np.float64(-12.9537), np.float64(-11.8855)]
Factor 2.0: Matches within 1%: 0/8
Errors (%): [np.float64(-29.9287), np.float64(-29.7138), np.float64(-23.4086), np.float64(-21.3353), np.float64(-22.5081), np.float64(-15.4723), np.float64(-13.3333), np.float64(-10.9842)]

```


## Iteration 9 (rc=0)

### Code
```python
import numpy as np
import librosa
from scipy.spatial.distance import cosine

# Function to get chroma vectors at specific times
def chroma_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)
    time_bins = librosa.frames_to_time(np.arange(chroma.shape[1]), sr=sr_in, hop_length=hop_length)
    interp_chroma = np.array([np.interp(times, time_bins, chroma[i]) for i in range(12)])
    return interp_chroma.T  # shape (len(times), 12)

# Get original onsets and chroma for rock
original_onsets = detect_onsets(rock, sr_rock, max_onsets=8)
orig_chroma = chroma_at_times(rock, original_onsets, sr_rock)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(rock, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_chroma = chroma_at_times(shifted, shifted_onsets, sr_rock)
    
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
```

### Output
```
Factor 1.25 (shift 4): Avg similarity: 0.2758, Matches >=0.9: 0/8
Similarities: [np.float64(0.2179), np.float64(0.2253), np.float64(0.3224), np.float64(0.3082), np.float64(0.4179), np.float64(0.2189), np.float64(0.2943), np.float64(0.2013)]
Factor 1.5 (shift 7): Avg similarity: 0.169, Matches >=0.9: 0/8
Similarities: [np.float64(0.1098), np.float64(0.1663), np.float64(0.1356), np.float64(0.1438), np.float64(0.2861), np.float64(0.0832), np.float64(0.3204), np.float64(0.1066)]
Factor 1.75 (shift 10): Avg similarity: 0.2641, Matches >=0.9: 0/8
Similarities: [np.float64(0.217), np.float64(0.1876), np.float64(0.3195), np.float64(0.3024), np.float64(0.3946), np.float64(0.2101), np.float64(0.2851), np.float64(0.1968)]
Factor 2.0 (shift 0): Avg similarity: 0.9863, Matches >=0.9: 8/8
Similarities: [np.float64(0.9978), np.float64(0.9264), np.float64(0.9988), np.float64(0.9943), np.float64(0.9878), np.float64(0.9975), np.float64(0.9945), np.float64(0.9929)]

```


## Iteration 10 (rc=0)

### Code
```python
import numpy as np
import librosa
from scipy.spatial.distance import cosine

# Function to get chroma vectors at specific times
def chroma_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)
    time_bins = librosa.frames_to_time(np.arange(chroma.shape[1]), sr=sr_in, hop_length=hop_length)
    interp_chroma = np.array([np.interp(times, time_bins, chroma[i]) for i in range(12)])
    return interp_chroma.T  # shape (len(times), 12)

# Get original onsets and chroma for orchestra
original_onsets = detect_onsets(orchestra, sr_orch, max_onsets=8)
orig_chroma = chroma_at_times(orchestra, original_onsets, sr_orch)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(orchestra, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_chroma = chroma_at_times(shifted, shifted_onsets, sr_orch)
    
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
```

### Output
```
Factor 1.25 (shift 4): Avg similarity: 0.5635, Matches >=0.9: 0/8
Similarities: [np.float64(0.6487), np.float64(0.5327), np.float64(0.6922), np.float64(0.5152), np.float64(0.5171), np.float64(0.4979), np.float64(0.4914), np.float64(0.6124)]
Factor 1.5 (shift 7): Avg similarity: 0.7676, Matches >=0.9: 0/8
Similarities: [np.float64(0.8439), np.float64(0.7524), np.float64(0.7578), np.float64(0.6652), np.float64(0.7429), np.float64(0.7701), np.float64(0.7727), np.float64(0.836)]
Factor 1.75 (shift 10): Avg similarity: 0.5159, Matches >=0.9: 0/8
Similarities: [np.float64(0.6231), np.float64(0.4519), np.float64(0.5826), np.float64(0.4409), np.float64(0.6689), np.float64(0.4078), np.float64(0.4109), np.float64(0.5409)]
Factor 2.0 (shift 0): Avg similarity: 0.9308, Matches >=0.9: 8/8
Similarities: [np.float64(0.909), np.float64(0.9254), np.float64(0.9208), np.float64(0.9532), np.float64(0.9052), np.float64(0.9464), np.float64(0.9549), np.float64(0.9314)]

```


## Iteration 11 (rc=0)

### Code
```python
import numpy as np
import librosa
from scipy.spatial.distance import cosine

# Function to get chroma vectors at specific times
def chroma_at_times(audio, times, sr_in, hop_length=512, n_fft=2048):
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr_in, hop_length=hop_length, n_fft=n_fft)
    time_bins = librosa.frames_to_time(np.arange(chroma.shape[1]), sr=sr_in, hop_length=hop_length)
    interp_chroma = np.array([np.interp(times, time_bins, chroma[i]) for i in range(12)])
    return interp_chroma.T  # shape (len(times), 12)

# Get original onsets and chroma for birdsong
original_onsets = detect_onsets(birdsong, sr_bird, max_onsets=8)
orig_chroma = chroma_at_times(birdsong, original_onsets, sr_bird)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(birdsong, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_chroma = chroma_at_times(shifted, shifted_onsets, sr_bird)
    
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
```

### Output
```
Factor 1.25 (shift 4): Avg similarity: 0.3962, Matches >=0.9: 1/8
Similarities: [np.float64(0.5414), np.float64(0.1306), np.float64(0.4456), np.float64(0.0812), np.float64(0.9703), np.float64(0.6756), np.float64(0.2689), np.float64(0.0557)]
Factor 1.5 (shift 7): Avg similarity: 0.554, Matches >=0.9: 1/8
Similarities: [np.float64(0.7344), np.float64(0.3536), np.float64(0.5117), np.float64(0.2993), np.float64(0.963), np.float64(0.7518), np.float64(0.7353), np.float64(0.0829)]
Factor 1.75 (shift 10): Avg similarity: 0.3995, Matches >=0.9: 1/8
Similarities: [np.float64(0.5249), np.float64(0.1411), np.float64(0.4453), np.float64(0.1251), np.float64(0.9693), np.float64(0.6813), np.float64(0.2256), np.float64(0.0837)]
Factor 2.0 (shift 0): Avg similarity: 0.9668, Matches >=0.9: 7/8
Similarities: [np.float64(0.9899), np.float64(0.9885), np.float64(0.9866), np.float64(0.9835), np.float64(0.9866), np.float64(0.9939), np.float64(0.823), np.float64(0.9821)]

```


## Iteration 12 (rc=0)

### Code
```python
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
```

### Output
```
Factor 1.25 (shift 4): Avg similarity: 0.0491, Matches >=0.9: 0/7
Similarities: [np.float64(0.1818), np.float64(0.0029), np.float64(0.0004), np.float64(0.0421), np.float64(0.0001), np.float64(0.1109), np.float64(0.0054)]
Factor 1.5 (shift 7): Avg similarity: 0.1392, Matches >=0.9: 0/7
Similarities: [np.float64(0.4943), np.float64(0.1158), np.float64(0.0466), np.float64(0.0385), np.float64(0.0281), np.float64(0.2219), np.float64(0.0293)]
Factor 1.75 (shift 10): Avg similarity: 0.0531, Matches >=0.9: 0/7
Similarities: [np.float64(0.1289), np.float64(0.0101), np.float64(0.006), np.float64(0.1172), np.float64(0.0113), np.float64(0.0864), np.float64(0.0118)]
Factor 2.0 (shift 0): Avg similarity: 0.9704, Matches >=0.9: 7/7
Similarities: [np.float64(0.9497), np.float64(0.9813), np.float64(0.994), np.float64(0.9964), np.float64(0.9991), np.float64(0.9124), np.float64(0.9598)]

```


## Iteration 13 (rc=0)

### Code
```python
import numpy as np

# Create synthetic melody: concatenate 8 tones with increasing freqs (harmonic series)
freqs = [220, 440, 660, 880, 1100, 1320, 1540, 1760]  # A3 and harmonics
dur = 0.8
synthetic = np.concatenate([generate_tone(f, dur) for f in freqs])
synth_sr = sr  # 44100

# Get original onsets and pitches
original_onsets = detect_onsets(synthetic, synth_sr, max_onsets=8)
orig_pitches = yin_pitches_at_times(synthetic, original_onsets, synth_sr)

factors = [1.25, 1.5, 1.75, 2.0]

for factor in factors:
    shifted = pitch_shift_real(synthetic, factor)
    shifted_onsets = [t / factor for t in original_onsets]
    shifted_pitches = yin_pitches_at_times(shifted, shifted_onsets, synth_sr)
    
    # Compute relative errors: (shifted / (orig * factor) - 1) * 100%
    errors = []
    for o, s in zip(orig_pitches, shifted_pitches):
        if o > 0 and s > 0:
            err = (s / (o * factor) - 1) * 100
            errors.append(err)
    
    # Count how many within 0.1%
    matches = sum(1 for e in errors if abs(e) <= 0.1)
    print(f"Factor {factor}: Matches within 0.1%: {matches}/{len(errors)}")
    print(f"Errors (%): {[round(e, 4) for e in errors]}")
```

### Output
```
Factor 1.25: Matches within 0.1%: 5/7
Errors (%): [-0.0112, -0.0093, 1.646, 0.013, 1.1875, 0.0526, 0.042]
Factor 1.5: Matches within 0.1%: 5/7
Errors (%): [-0.0219, -0.0142, 1.8692, 0.0095, 1.224, 0.0994, 0.0207]
Factor 1.75: Matches within 0.1%: 4/7
Errors (%): [-0.0213, 0.0063, 1.8747, 0.0454, 1.2728, 0.095, 0.1142]
Factor 2.0: Matches within 0.1%: 4/7
Errors (%): [-0.0183, -0.0043, 1.919, 0.0803, 1.2395, 0.1601, -0.0022]

```


## Iteration 14 (rc=0)

### Code
```python
import numpy as np

# Create synthetic melody: concatenate 8 tones with increasing freqs (harmonic series)
freqs = [220, 440, 660, 880, 1100, 1320, 1540, 1760]  # A3 and harmonics
dur = 0.8
synthetic = np.concatenate([generate_tone(f, dur) for f in freqs])
synth_sr = sr  # 44100

# Get original onsets and pitches
original_onsets = detect_onsets(synthetic, synth_sr, max_onsets=8)
orig_pitches = yin_pitches_at_times(synthetic, original_onsets, synth_sr)

factor = 2.0
shifted = pitch_shift_real(synthetic, factor)
shifted_onsets = [t / factor for t in original_onsets]
shifted_pitches = yin_pitches_at_times(shifted, shifted_onsets, synth_sr)

expected_orig = freqs[:len(orig_pitches)]  # in case fewer detected
expected_shifted = [f * factor for f in expected_orig]

print("Original pitches (detected):", [round(p, 2) for p in orig_pitches])
print("Expected original:", expected_orig)
print("Shifted pitches (detected):", [round(p, 2) for p in shifted_pitches])
print("Expected shifted:", expected_shifted)

# Compute errors for original and shifted
orig_errors = [(p - e) / e * 100 if e > 0 else 0 for p, e in zip(orig_pitches, expected_orig)]
shifted_errors = [(p - e) / e * 100 if e > 0 else 0 for p, e in zip(shifted_pitches, expected_shifted)]

print("Orig errors (%):", [round(e, 4) for e in orig_errors])
print("Shifted errors (%):", [round(e, 4) for e in shifted_errors])
```

### Output
```
Original pitches (detected): [440.33, 660.34, 864.25, 1100.61, 1305.34, 1540.75, 1761.66]
Expected original: [220, 440, 660, 880, 1100, 1320, 1540]
Shifted pitches (detected): [880.49, 1320.62, 1761.67, 2202.98, 2643.04, 3086.44, 3523.24]
Expected shifted: [440.0, 880.0, 1320.0, 1760.0, 2200.0, 2640.0, 3080.0]
Orig errors (%): [100.1479, 50.0766, 30.947, 25.0688, 18.6675, 16.7237, 14.3935]
Shifted errors (%): [100.1114, 50.0702, 33.4599, 25.1692, 20.1384, 16.9105, 14.391]

```


## Iteration 15 (rc=1)

### Code
```python
import numpy as np
from fractions import Fraction

# Create synthetic melody: concatenate 8 tones with harmonic series freqs
freqs = [220, 440, 660, 880, 1100, 1320, 1540, 1760]
dur = 0.8
synthetic = np.concatenate([generate_tone(f, dur) for f in freqs])

# Get sequence for original
orig_seq = get_sequence_from_melody(synthetic, num_notes=7)  # 7 ratios for 8 notes

factors = [1.25, 1.5, 1.75, 2.0]

print("Original sequence:", [(f.numerator, f.denominator) for f in orig_seq])

for factor in factors:
    shifted = pitch_shift_real(synthetic, factor)
    shifted_seq = get_sequence_from_melody(shifted, num_notes=7)
    
    # Check how many match original
    matches = sum(1 for o, s in zip(orig_seq, shifted_seq) if o == s)
    print(f"Factor {factor}: Matches: {matches}/{len(orig_seq)}")
    print("Shifted sequence:", [(f.numerator, f.denominator) for f in shifted_seq])
```

### Output
```

[STDERR]
Traceback (most recent call last):
  File "/home/runner/workspace/iter_15.py", line 103, in <module>
    print("Original sequence:", [(f.numerator, f.denominator) for f in orig_seq])
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/workspace/iter_15.py", line 103, in <listcomp>
    print("Original sequence:", [(f.numerator, f.denominator) for f in orig_seq])
                                  ^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'numerator'

```


## Iteration 16 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Create synthetic melody: concatenate 8 tones with harmonic series freqs
freqs = [220, 440, 660, 880, 1100, 1320, 1540, 1760]
dur = 0.8
synthetic = np.concatenate([generate_tone(f, dur) for f in freqs])

# Get sequence for original
orig_seq = get_sequence_from_melody(synthetic, num_notes=7)  # 7 ratios for 8 notes

factors = [1.25, 1.5, 1.75, 2.0]

print("Original sequence:", orig_seq)

for factor in factors:
    shifted = pitch_shift_real(synthetic, factor)
    shifted_seq = get_sequence_from_melody(shifted, num_notes=7)
    
    # Check how many match original
    matches = sum(1 for o, s in zip(orig_seq, shifted_seq) if o == s)
    print(f"Factor {factor}: Matches: {matches}/{len(orig_seq)}")
    print("Shifted sequence:", shifted_seq)
```

### Output
```
Original sequence: ((1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1), (8, 1))
Factor 1.25: Matches: 7/7
Shifted sequence: ((1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1), (8, 1))
Factor 1.5: Matches: 7/7
Shifted sequence: ((1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1), (8, 1))
Factor 1.75: Matches: 7/7
Shifted sequence: ((1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1), (8, 1))
Factor 2.0: Matches: 7/7
Shifted sequence: ((1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1), (8, 1))

```


## Iteration 17 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Get sequence for original orchestra
orig_seq = get_sequence_from_melody(orchestra, num_notes=8)

factors = [1.25, 1.5, 1.75, 2.0]

print("Original sequence:", orig_seq)

for factor in factors:
    shifted = pitch_shift_real(orchestra, factor)
    shifted_seq = get_sequence_from_melody(shifted, num_notes=8)
    
    # Check how many match original
    matches = sum(1 for o, s in zip(orig_seq, shifted_seq) if o == s)
    print(f"Factor {factor}: Matches: {matches}/{len(orig_seq)}")
    print("Shifted sequence:", shifted_seq)
```

### Output
```
Original sequence: ((1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13))
Factor 1.25: Matches: 7/8
Shifted sequence: ((1, 1), (125, 13), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13))
Factor 1.5: Matches: 7/8
Shifted sequence: ((1, 1), (125, 13), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13))
Factor 1.75: Matches: 8/8
Shifted sequence: ((1, 1), (125, 13), (19, 16), (77, 8), (125, 13), (77, 8), (125, 13), (125, 13))
Factor 2.0: Matches: 6/8
Shifted sequence: ((1, 1), (77, 8), (19, 16), (77, 8), (77, 8), (77, 8), (125, 13), (125, 13))

```


## Iteration 18 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Get sequence for original rock
orig_seq = get_sequence_from_melody(rock, num_notes=8)

factors = [1.25, 1.5, 1.75, 2.0]

print("Original sequence:", orig_seq)

for factor in factors:
    shifted = pitch_shift_real(rock, factor)
    shifted_seq = get_sequence_from_melody(shifted, num_notes=8)
    
    # Check how many match original
    matches = sum(1 for o, s in zip(orig_seq, shifted_seq) if o == s)
    print(f"Factor {factor}: Matches: {matches}/{len(orig_seq)}")
    print("Shifted sequence:", shifted_seq)
```

### Output
```
Original sequence: ((74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1))
Factor 1.25: Matches: 8/8
Shifted sequence: ((74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1))
Factor 1.5: Matches: 8/8
Shifted sequence: ((74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1))
Factor 1.75: Matches: 8/8
Shifted sequence: ((74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1))
Factor 2.0: Matches: 8/8
Shifted sequence: ((74, 11), (10, 3), (4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (1, 1))

```


## Iteration 19 (rc=0)

### Code
```python
import numpy as np
from fractions import Fraction

# Get sequence for original birdsong
orig_seq = get_sequence_from_melody(birdsong, num_notes=8)

factors = [1.25, 1.5, 1.75, 2.0]

print("Original sequence:", orig_seq)

for factor in factors:
    shifted = pitch_shift_real(birdsong, factor)
    shifted_seq = get_sequence_from_melody(shifted, num_notes=8)
    
    # Check how many match original
    matches = sum(1 for o, s in zip(orig_seq, shifted_seq) if o == s)
    print(f"Factor {factor}: Matches: {matches}/{len(orig_seq)}")
    print("Shifted sequence:", shifted_seq)
```

### Output
```
Original sequence: ((17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10))
Factor 1.25: Matches: 8/8
Shifted sequence: ((17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10))
Factor 1.5: Matches: 8/8
Shifted sequence: ((17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10))
Factor 1.75: Matches: 8/8
Shifted sequence: ((17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10))
Factor 2.0: Matches: 8/8
Shifted sequence: ((17, 6), (11, 4), (1, 1), (11, 10), (36, 13), (11, 4), (45, 16), (23, 10))

```


## Iteration 20 (rc=0)

### Code
```python
import numpy as np

# Get original onsets and pitches for orchestra
original_onsets = detect_onsets(orchestra, sr_orch, max_onsets=8)
orig_pitches = yin_pitches_at_times(orchestra, original_onsets, sr_orch)

factor = 2.0
shifted = pitch_shift_real(orchestra, factor)
shifted_onsets = [t / factor for t in original_onsets]
shifted_pitches = yin_pitches_at_times(shifted, shifted_onsets, sr_orch)

# Compute detected ratios to first non-zero pitch
def compute_ratios(pitches):
    first = next((p for p in pitches if p > 0), 0)
    if first == 0: return []
    return [Fraction(p / first).limit_denominator(100) for p in pitches]

orig_ratios = compute_ratios(orig_pitches)
shifted_ratios = compute_ratios(shifted_pitches)

print("Original pitches:", [round(p, 2) for p in orig_pitches])
print("Shifted pitches:", [round(p, 2) for p in shifted_pitches])
print("Original ratios:", [(r.numerator, r.denominator) for r in orig_ratios])
print("Shifted ratios:", [(r.numerator, r.denominator) for r in shifted_ratios])

# Check matches
matches = sum(1 for o, s in zip(orig_ratios, shifted_ratios) if o == s)
print(f"Ratio matches: {matches}/{min(len(orig_ratios), len(shifted_ratios))}")
```

### Output
```
Original pitches: [82.99, 82.66, 82.51, 82.55, 82.48, 82.47, 82.53, 84.89]
Shifted pitches: [165.4, 165.01, 165.01, 165.01, 164.99, 164.85, 165.01, 171.68]
Original ratios: [(1, 1), (1, 1), (99, 100), (99, 100), (99, 100), (99, 100), (99, 100), (45, 44)]
Shifted ratios: [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (82, 79)]
Ratio matches: 2/8

```

