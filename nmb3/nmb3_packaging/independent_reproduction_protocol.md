# Independent Reproduction Protocol — NMB3 M5.6 + M6.4 (one page)

A copy-pasteable protocol an external reviewer can run to
independently reproduce, on a fresh `ubuntu-latest` CI runner with
no caches:

  - the **M5.6 baseline (107/144 = 0.7431)** on the canonical
    6-clip M4.1 benchmark, AND
  - **at least one M6.4 PASS query** from the canonical Twinkle
    family-retrieval table (`twinkle_box`: top3=3, top5=3,
    outranks-all-nonfam=YES — the strongest of the three M6.4 PASS
    queries; the run also produces the `twinkle_harmonica` and
    `twinkle_people` rows alongside it).

Both reproductions are produced by a single CI dispatch.

---

## Pinning

  - **Repository:**    `stevewebmarket/nightingale-mapping`
  - **Pinning SHA:**   the head SHA recorded in the O039 interpreter
                       output `nmb3/nmb3_reports/o039_independent_reproduction_protocol.md`
                       (§ Pinning).  Equivalently: any canonical SHA
                       at or after that commit; intervening commits
                       are doc-only and do not change pipeline
                       behaviour.
  - **Workflow file:** `.github/workflows/nmb3_no_cache_repro.yml`
                       (created in O023 at SHA `1368524`,
                       ffmpeg-extended in O033 at SHA `3929fbc`;
                       reused unmodified here).
  - **Reproduction
    targets:**         M5.6 baseline + M6.4 family-retrieval table,
                       both via canonical scripts run unmodified
                       (`run_m4_1_benchmark.py`,
                       `run_m6_4_family_retrieval.py`).

## Mode B — CI re-dispatch (recommended; no local install)

Pre-requisites: a GitHub account with `Actions: write` on either
`stevewebmarket/nightingale-mapping` or a fork of it.

```bash
# Substitute <PIN_SHA> with the value from the Pinning section above,
# and <REPO> with the upstream repo or your fork.

gh workflow run nmb3_no_cache_repro.yml \
  --repo <REPO> \
  --ref <PIN_SHA-or-branch-pointing-at-PIN_SHA> \
  -f target=m6_4_repro_smoke \
  -f script='python run_m4_1_benchmark.py && python run_m6_4_family_retrieval.py'

gh run list --workflow=nmb3_no_cache_repro.yml --repo <REPO> --limit 1
gh run watch <run-id> --repo <REPO>
gh run view <run-id> --log --repo <REPO> | tail -200
```

Note: `gh workflow run --ref` accepts a branch or tag name, not an
arbitrary SHA; if your fork's `main` is at the pinned SHA, use
`--ref main`, otherwise push the pinned SHA to a branch and pass
that branch name.

## Mode A — Local fresh clone (equivalent to Mode B)

Requires: `python>=3.11`, `git`, `ffmpeg` on `PATH`.

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping
git checkout <PIN_SHA>
python -m venv .venv && source .venv/bin/activate
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir numpy scipy librosa soundfile
python scripts/fetch_samples.py
python run_m4_1_benchmark.py
python run_m6_4_family_retrieval.py
```

## Expected output (lines to verify)

  - From `run_m4_1_benchmark.py`, the final `TOTAL` row:
    `TOTAL` ... `107/144   0.7431` (within-tolerance count /
    note total / score, formatted to 4 decimal places).
  - From `run_m6_4_family_retrieval.py`, the family-retrieval
    summary block:
    `twinkle_box               top3=3 top5=3 outranks-all-nonfam=YES`
  - From the same script, the cond4 honesty self-check:
    `4. weak-evidence honestly flagged AND twinkle_people still weak: PASS`
  - The script's final line: `M6.4 PASS`.

If any of these four lines is absent or differs, the reproduction
has not succeeded — do NOT silently accept partial matches.

## Out of scope

  - Milestones M3.1–M3.4, M4.1, M5.1–M5.5, M6.1–M6.3 (not SHA-pinned;
    see `nmb3/nmb3_packaging/reproducibility_appendix.md` § B for the
    full list of explicit gaps and the "gap, not failure" framing).
  - Milestones M5.7 / M5.8 / M5.9 (NEGATIVE / FAIL / ABANDONED — not
    reproductions of a positive baseline; see MILESTONES.md and
    `reproducibility_appendix.md` § C for the non-claim register).
  - M6.5 (FAIL preserved; reproduced under O034 separately).
  - Any claim of improvement over the canonical numbers.
  - Any funding, commercial, or perceptual-validity claim.

## Reference dispatch

The CI run id, head SHA, dispatch timestamp, headline-line
verifications, and 90-day artefact name for the reference dispatch
performed under O039 are recorded in
`nmb3/nmb3_reports/o039_independent_reproduction_protocol.md`.
