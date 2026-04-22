"""
M5.5 — Adaptive window routing ablation.

Last 'clever but still disciplined' step before architectural change.
Tests whether a single global deterministic rule can pick between two
fixed pitch-window strategies per onset and beat M5.3 without slipping
into per-clip tuning.

Strategies (only two allowed):
  baseline   window [t-0.15, t+0.25], YIN median   (M5.3 default)
  short_med  window [t+0.02, t+0.18], YIN median

The M5.3 cqt_flux onset detector remains locked.

Pre-set pass condition (set BEFORE run):

  1. polyphonic stays 8/8 detected on all three transforms
  2. polyphonic matches improve above 4/24
  3. highenergy improves above 9/24
  4. grand total > 100/144 (0.6944)
  5. orchestra / flute / synthetic do not drop by more than 1 each vs M5.3
  6. rule is global, deterministic, uses no clip-specific thresholds
  7. rock regression remains visible (or genuinely improved)

Routing rules (one global signal each):

  rms_attack_ratio   early-half RMS / late-half RMS in probe window
                     [t-0.05, t+0.20].  ratio > 1.5  -> short_med
                     (sharp transient onset)

  spectral_flatness  librosa.feature.spectral_flatness on probe window
                     [t-0.05, t+0.15].  median > 0.30 -> short_med
                     (broadband / noisy)

  harmonic_peak_ratio max FFT bin / mean FFT bin in probe window
                     [t-0.05, t+0.20].  ratio < 8.0  -> short_med
                     (no clear harmonic peak)

  local_pitch_stability  quick YIN on probe window [t-0.05, t+0.20];
                     std/mean of valid f0.  rel_std > 0.05 -> short_med
                     (unstable pitch -> dense or transient material)

Reported per variant: per-clip and grand totals, route counts so we can
catch a rule that has collapsed into 'always pick one side'.

Usage:
    python run_m5_5_adaptive_ablation.py
"""

import json
import os
from collections import Counter
from statistics import median

import numpy as np
import librosa

import run_milestones as RM
from run_milestones import (
    DEFAULT_CONFIG, SR, NUM_NOTES, SHIFT_FACTOR,
    score_pitch_shift, score_time_stretch, score_composition,
)
from run_m4_1_benchmark import synthetic_clip, load_audio_file

EXPECTED_RATIO = {
    "pitch_shift":  SHIFT_FACTOR,
    "time_stretch": 1.0,
    "composition":  SHIFT_FACTOR,
}

YIN_FRAME = 2048
YIN_HOP = 512


# ---------------------------------------------------------------------------
# Two fixed pitch-window strategies
# ---------------------------------------------------------------------------

def _seg(audio, t_start, t_end):
    s = max(0, int(t_start * SR))
    e = min(len(audio), int(t_end * SR))
    return audio[s:e]


def _yin_window_median(seg, cfg):
    if len(seg) < 512:
        return None
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) == 0:
        return None
    return float(np.median(valid))


def p_baseline(audio, t, cfg):
    return _yin_window_median(_seg(audio, t - 0.15, t + 0.25), cfg)


def p_short_med(audio, t, cfg):
    return _yin_window_median(_seg(audio, t + 0.02, t + 0.18), cfg)


# ---------------------------------------------------------------------------
# Routing signals  (return True to pick short_med, False to pick baseline)
# All thresholds are GLOBAL constants set in the docstring above.
# ---------------------------------------------------------------------------

THR_RMS_ATTACK = 1.5
THR_FLATNESS   = 0.30
THR_HARM_PEAK  = 8.0
THR_PITCH_STD  = 0.05


def route_rms_attack(audio, t, cfg):
    early = _seg(audio, t - 0.05, t + 0.075)
    late  = _seg(audio, t + 0.075, t + 0.20)
    if len(early) == 0 or len(late) == 0:
        return False
    e_rms = float(np.sqrt(np.mean(early ** 2) + 1e-12))
    l_rms = float(np.sqrt(np.mean(late ** 2) + 1e-12))
    return (e_rms / l_rms) > THR_RMS_ATTACK


def route_flatness(audio, t, cfg):
    seg = _seg(audio, t - 0.05, t + 0.15)
    if len(seg) < YIN_FRAME:
        return False
    sf = librosa.feature.spectral_flatness(y=seg)[0]
    return float(np.median(sf)) > THR_FLATNESS


def route_harm_peak(audio, t, cfg):
    seg = _seg(audio, t - 0.05, t + 0.20)
    if len(seg) < YIN_FRAME:
        return False
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    mean = float(np.mean(spec) + 1e-12)
    peak = float(np.max(spec))
    return (peak / mean) < THR_HARM_PEAK   # weak peak -> short_med


def route_pitch_stability(audio, t, cfg):
    seg = _seg(audio, t - 0.05, t + 0.20)
    if len(seg) < YIN_FRAME:
        return False
    f0 = librosa.yin(seg, fmin=cfg.get("fmin", 50),
                     fmax=cfg.get("fmax", 16000), sr=SR,
                     frame_length=YIN_FRAME, hop_length=YIN_HOP)
    valid = f0[f0 > cfg.get("fmin", 50)]
    if len(valid) < 3:
        return True   # too little signal to trust -> short_med
    rel_std = float(np.std(valid) / (np.mean(valid) + 1e-12))
    return rel_std > THR_PITCH_STD


# ---------------------------------------------------------------------------
# Variant builders
# ---------------------------------------------------------------------------

def make_adaptive(route_fn, route_log):
    def fn(audio, t, cfg):
        use_short = route_fn(audio, t, cfg)
        route_log["short_med" if use_short else "baseline"] += 1
        return p_short_med(audio, t, cfg) if use_short else p_baseline(audio, t, cfg)
    return fn


def make_fixed(p_fn, route_log, label):
    def fn(audio, t, cfg):
        route_log[label] += 1
        return p_fn(audio, t, cfg)
    return fn


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate(name, build_fn, clips, cfg):
    """build_fn(route_log) returns the pitch_at function bound to the log."""
    route_log = Counter()
    pitch_fn = build_fn(route_log)
    original = RM.pitch_at
    RM.pitch_at = lambda audio, t, cfg=cfg: pitch_fn(audio, t, cfg)
    try:
        out = {}
        for clip_name, audio in clips:
            per_test = {}
            for sfn in (score_pitch_shift, score_time_stretch, score_composition):
                r = sfn(audio, clip_name, cfg)
                test = r["test"]
                expected = EXPECTED_RATIO[test]
                rel_errs = [abs(v - expected) / abs(expected)
                            for v in r["folded"] if v is not None]
                per_test[test] = {
                    "detected": r["total"],
                    "matches":  r["folded_score"],
                    "median_rel_error": float(median(rel_errs)) if rel_errs else None,
                }
            out[clip_name] = per_test
        return out, dict(route_log)
    finally:
        RM.pitch_at = original


def main():
    cfg = dict(DEFAULT_CONFIG)

    print("Loading clips...")
    clips = []
    file_clips = [
        ("orchestra",  "orchestra.wav"),
        ("rock",       "rock.wav"),
        ("flute",      "flute.mp3"),
        ("polyphonic", "polyphonic.mp3"),
        ("highenergy", "highenergy.wav"),
    ]
    for name, path in file_clips:
        if not os.path.isfile(path):
            raise FileNotFoundError(
                f"Missing {path}.  Run: python scripts/fetch_samples.py"
            )
        clips.append((name, load_audio_file(path)))
    clips.append(("synthetic_just", synthetic_clip()))

    variants = [
        ("baseline",                     lambda log: make_fixed(p_baseline,  log, "baseline")),
        ("short_med",                    lambda log: make_fixed(p_short_med, log, "short_med")),
        ("adaptive_rms_attack",          lambda log: make_adaptive(route_rms_attack,      log)),
        ("adaptive_spectral_flatness",   lambda log: make_adaptive(route_flatness,        log)),
        ("adaptive_harmonic_peak_ratio", lambda log: make_adaptive(route_harm_peak,       log)),
        ("adaptive_local_pitch_stab",    lambda log: make_adaptive(route_pitch_stability, log)),
    ]

    print("=" * 100)
    print("M5.5 — adaptive window routing ablation  (no per-clip tuning)")
    print(f"  base config: {cfg}")
    print(f"  thresholds:  rms_attack>{THR_RMS_ATTACK}  flatness>{THR_FLATNESS}  "
          f"harm_peak<{THR_HARM_PEAK}  pitch_rel_std>{THR_PITCH_STD}")
    print("=" * 100)

    all_results = {}
    for vname, builder in variants:
        per_clip, route_log = evaluate(vname, builder, clips, cfg)
        all_results[vname] = {"per_clip": per_clip, "routes": route_log}
        print(f"\n[{vname}]   routes: {route_log}")
        print(f"  {'clip':16s} {'pitch':>10s} {'time':>10s} {'comp':>10s}   {'total':>9s}")
        gw, gt = 0, 0
        for clip_name in [c for c, _ in clips]:
            t = per_clip[clip_name]
            ds_w = sum(t[k]["matches"]  for k in t)
            ds_t = sum(t[k]["detected"] for k in t)
            gw += ds_w; gt += ds_t
            print(f"  {clip_name:16s} "
                  f"{t['pitch_shift']['matches']:>3d}/{t['pitch_shift']['detected']:<2d}    "
                  f"{t['time_stretch']['matches']:>3d}/{t['time_stretch']['detected']:<2d}    "
                  f"{t['composition']['matches']:>3d}/{t['composition']['detected']:<2d}    "
                  f"{ds_w:>3d}/{ds_t:<3d}")
        print(f"  {'TOTAL':16s}                                     "
              f"{gw:>3d}/{gt:<3d}   score={gw/gt:.4f}")

    # Summary table
    print("\n" + "=" * 100)
    print("Summary  vs  M5.3 baseline (orch=24 flute=22 synth=23 rock_t=4 poly=4 high=9 total=100/144)")
    print("=" * 100)
    print(f"  {'variant':28s}  {'poly':>5s} {'high':>5s} {'orch':>5s} {'flute':>6s} {'synth':>6s} "
          f"{'rk_t':>5s}  {'route base/short':>18s}  {'total':>10s}  pass[1-7]")
    M5_3 = dict(orchestra=24, rock=18, flute=22, polyphonic=4, highenergy=9, synthetic_just=23,
                total=100, rock_time=4)
    for vname, _ in variants:
        per = all_results[vname]["per_clip"]
        rl = all_results[vname]["routes"]
        def total(c):
            return sum(per[c][k]["matches"] for k in per[c])
        gw = sum(total(c) for c in per)
        gt = sum(per[c][k]["detected"] for c in per for k in per[c])
        poly_det_ok = all(per["polyphonic"][k]["detected"] == 8 for k in per["polyphonic"])
        c1 = poly_det_ok
        c2 = total("polyphonic") > 4
        c3 = total("highenergy") > 9
        c4 = gw / gt > 100 / 144
        c5 = (total("orchestra") >= 23) and (total("flute") >= 21) and (total("synthetic_just") >= 22)
        c6 = True   # by construction: thresholds are global constants in this file
        rock_t = per["rock"]["time_stretch"]["matches"]
        c7 = True   # always-visible: we report rock_t in the row
        flags = "".join("Y" if c else "n" for c in [c1, c2, c3, c4, c5, c6, c7])
        rb = rl.get("baseline", 0)
        rs = rl.get("short_med", 0)
        rstr = f"{rb}/{rs}"
        print(f"  {vname:28s}  "
              f"{total('polyphonic'):>5d} {total('highenergy'):>5d} "
              f"{total('orchestra'):>5d} {total('flute'):>6d} {total('synthetic_just'):>6d} "
              f"{rock_t:>5d}  {rstr:>18s}  "
              f"{gw:>4d}/{gt:<4d}  {flags}")

    with open("m5_5_adaptive_ablation.json", "w") as f:
        json.dump({"config": cfg, "thresholds": {
            "rms_attack": THR_RMS_ATTACK, "flatness": THR_FLATNESS,
            "harm_peak": THR_HARM_PEAK, "pitch_rel_std": THR_PITCH_STD,
        }, "results": all_results}, f, indent=2)
    print("\nWrote m5_5_adaptive_ablation.json")


if __name__ == "__main__":
    main()
