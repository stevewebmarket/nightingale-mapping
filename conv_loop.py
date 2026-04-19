"""Conversational loop: run experiment -> Grok feedback -> Grok proposes next -> repeat."""
import os, sys, json, subprocess, time, re, requests, textwrap

XAI_API_KEY = os.environ["XAI_API_KEY"]
MODEL = os.environ.get("GROK_MODEL", "grok-4-latest")
N_ITERATIONS = int(os.environ.get("N_ITERS", "20"))
ITER_TIMEOUT_S = 120
MAX_OUTPUT_CHARS = 4000

BOILERPLATE_PATH = "conv_boilerplate.py"
LOG_PATH = "conv_loop_transcript.md"

with open(BOILERPLATE_PATH) as f:
    BOILERPLATE = f.read()

SYSTEM_PROMPT = textwrap.dedent("""
You are a research collaborator on the Nightingale Mapping / Rosetta Stone project.

MISSION
Test whether mathematical structure (ratios, sequences, symmetries, scaling, recursion)
survives translation between sound and structured representation, on both synthetic
signals and three real-world samples (birdsong, orchestra, rock).

WHAT IS ALREADY ESTABLISHED
- Synthetic Levels 2-7 round-trip cleanly through generate_tone / get_sequence_from_melody.
- pitch_shift_real(sound, factor) genuinely shifts pitch (verified on pure tones AND on
  three real samples: dominant frequencies move by exactly factor).
- The OLD pitch_shift_whole that upsampled-then-downsampled was a NO-OP. Do NOT use it.
- Real-audio invariance under pitch_shift_real with matched onsets:
  Orchestra 7/8 at 0.1% precision, Rock 8/8 octave-folded, Birdsong 2/8 (YIN mismatch
  for broadband non-harmonic content).

PERSISTENT HELPERS YOU CAN USE (already imported and ready):
  numpy as np, librosa, Fraction, sr=44100
  generate_tone(freq, dur=0.8)
  normalize(s)
  pitch_shift_real(sound, factor=1.5)        <-- USE THIS, not pitch_shift_whole
  time_stretch_real(sound, factor=1.5)
  get_sequence_from_melody(sound, num_notes) -> tuple of (num,den) Fraction pairs
  yin_pitches_at_times(audio, times, sr_in=sr, fmin=50, fmax=16000)
  detect_onsets(audio, sr_in=sr, max_onsets=8)
  birdsong, orchestra, rock      (numpy arrays, mono float32 normalized)
  sr_bird, sr_orch, sr_rock      (sample rates, all 44100)
  SAMPLES dict {"birdsong": (audio, sr), ...}

RULES FOR YOUR REPLIES
1. Reply with ONLY a single Python code block (no prose, no markdown fences, no commentary).
   Just raw runnable Python that uses the helpers above.
2. Each iteration must test ONE specific, falsifiable hypothesis or extend the previous
   result in one concrete way.
3. ALWAYS use pitch_shift_real (never pitch_shift_whole — it does not exist here).
4. When comparing original vs transformed audio, use MATCHED onsets:
   shifted_onsets = [t/factor for t in original_onsets]
5. Use librosa.yin for harmonic content. For broadband signals like birdsong, consider
   spectral centroid, chroma, or onset-density features instead.
6. Print results with clear labels. Keep total output under ~3000 chars.
7. If a previous iteration failed or produced surprising output, propose a diagnostic next.
8. Do NOT redefine the helpers above; just use them.
9. Do NOT use input(), sys.exit(), os.system, subprocess, or write files outside /tmp.
""").strip()

def call_grok(history):
    body = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + history,
        "temperature": 0.4,
    }
    r = requests.post("https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {XAI_API_KEY}",
                 "Content-Type": "application/json"},
        json=body, timeout=120)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        lines = content.splitlines()
        if lines[0].startswith("```"): lines = lines[1:]
        if lines and lines[-1].startswith("```"): lines = lines[:-1]
        content = "\n".join(lines).strip()
    return content

def run_iteration(code, iter_num):
    path = f"iter_{iter_num:02d}.py"
    full = BOILERPLATE + "\n\n# === Grok-proposed iteration ===\n" + code + "\n"
    with open(path, "w") as f:
        f.write(full)
    try:
        proc = subprocess.run(
            ["python3", path],
            capture_output=True, text=True, timeout=ITER_TIMEOUT_S, cwd=os.getcwd()
        )
        out = (proc.stdout or "") + (("\n[STDERR]\n" + proc.stderr) if proc.stderr.strip() else "")
        if len(out) > MAX_OUTPUT_CHARS:
            out = out[:MAX_OUTPUT_CHARS] + f"\n...[truncated, {len(out)} chars total]"
        return proc.returncode, out
    except subprocess.TimeoutExpired:
        return -1, f"TIMEOUT after {ITER_TIMEOUT_S}s"

initial_user = (
    "Begin iteration 1. Based on the established findings, propose ONE concrete next "
    "experiment. A good first move: re-validate the Orchestra 7/8 result more rigorously "
    "(e.g. run pitch_shift_real at multiple factors like 1.25, 1.5, 1.75, 2.0 and verify "
    "the matched-onset YIN ratios scale linearly). Reply with raw Python only."
)
history = [{"role": "user", "content": initial_user}]
transcript = []

with open(LOG_PATH, "w") as f:
    f.write(f"# Conversational loop transcript\nModel: {MODEL}\nStart: {time.ctime()}\n\n")

def append_transcript(t):
    with open(LOG_PATH, "a") as f:
        f.write(f"\n## Iteration {t['iter']} (rc={t['rc']})\n\n")
        f.write("### Code\n```python\n" + t['code'] + "\n```\n\n")
        f.write("### Output\n```\n" + t['output'] + "\n```\n\n")

print(f"=== Conversational loop: {N_ITERATIONS} iterations, model={MODEL} ===\n", flush=True)
t_start = time.time()

for i in range(1, N_ITERATIONS + 1):
    print(f"\n----- Iteration {i}/{N_ITERATIONS} -----", flush=True)
    try:
        code = call_grok(history)
    except Exception as e:
        print(f"Grok call failed: {e}", flush=True)
        err_t = {"iter": i, "code": f"# Grok call failed: {e}", "rc": -2, "output": str(e)}
        transcript.append(err_t); append_transcript(err_t)
        time.sleep(5)
        continue
    code_preview = code[:300].replace("\n", " | ")
    print(f"[Grok proposed {len(code)} chars] {code_preview}...", flush=True)

    try:
        rc, out = run_iteration(code, i)
    except Exception as e:
        rc, out = -3, f"run_iteration crashed: {e}"
    print(f"[Run rc={rc}, output {len(out)} chars]", flush=True)
    print(out[:1500], flush=True)
    if len(out) > 1500:
        print(f"...[+{len(out)-1500} more chars]", flush=True)

    t = {"iter": i, "code": code, "rc": rc, "output": out}
    transcript.append(t)
    append_transcript(t)
    history.append({"role": "assistant", "content": code})
    history.append({
        "role": "user",
        "content": f"Iteration {i} output (rc={rc}):\n```\n{out}\n```\n\n"
                   f"Propose iteration {i+1}. Build on this result OR pivot if it failed. "
                   f"Raw Python only."
    })

    if len(history) > 22:
        history = history[:1] + history[-20:]

elapsed = time.time() - t_start
print(f"\n=== Done. {len(transcript)} iterations in {elapsed:.0f}s ===")
print(f"Full transcript: {LOG_PATH}")
print("\nQuick summary:")
for t in transcript:
    head = t['output'].splitlines()[0] if t['output'] else "(no output)"
    print(f"  iter {t['iter']:2d}  rc={t['rc']:>3}  {head[:100]}")
