# Independent Reproduction Protocol — NMB3 M5.6 + M6.4 (one page)

A copy-pasteable protocol an external reviewer can run on a fresh
`ubuntu-latest` CI runner with no caches, to bit-identically reproduce:

  - the **M5.6 baseline (107/144 = 0.7431)** on the canonical 6-clip
    M4.1 benchmark; and
  - **at least one M6.4 PASS query** (`twinkle_box`: top3=3, top5=3,
    outranks-all-nonfam=YES — the strongest of the three; the run
    also produces the `twinkle_harmonica` and `twinkle_people` rows).

## Pinning

  - **Repo:**          `stevewebmarket/nightingale-mapping`
  - **Pin SHA:**       `766cff65c2f868e37d344065c5188d69db88cf90` (exact;
                       no other SHA is in scope of this protocol).
  - **Workflow file:** `.github/workflows/nmb3_no_cache_repro.yml`
                       (created in O023 at SHA `1368524`,
                       ffmpeg-extended in O033 at SHA `3929fbc`; reused
                       unmodified).
  - **Targets:**       `run_m4_1_benchmark.py` and
                       `run_m6_4_family_retrieval.py` run unmodified.

## Mode B — CI re-dispatch (recommended)

Pre-requisites: a GitHub account; a fork of the upstream repo (so
you have `Actions: write`).  The `gh` CLI install instructions
below are for Ubuntu/Debian; non-Debian platforms use the official
installer at `https://cli.github.com/manual/installation`.

```bash
# 1. Install + authenticate the gh CLI
sudo apt-get update && sudo apt-get install -y gh
gh auth login                          # interactive; or set GH_TOKEN

# 2. Fork upstream in the GitHub UI, then clone your fork:
git clone https://github.com/<YOU>/nightingale-mapping.git
cd nightingale-mapping

# 3. Fetch the pin SHA from upstream and push it to a branch on your fork
#    (gh workflow run --ref needs a branch or tag, not a raw SHA).
git remote add upstream https://github.com/stevewebmarket/nightingale-mapping.git
git fetch upstream 766cff65c2f868e37d344065c5188d69db88cf90
git push origin 766cff65c2f868e37d344065c5188d69db88cf90:refs/heads/o039-pin

# 4. Dispatch the shared no-cache workflow
gh workflow run nmb3_no_cache_repro.yml --repo <YOU>/nightingale-mapping \
  --ref o039-pin \
  -f target=m6_4_repro_smoke \
  -f script='python run_m4_1_benchmark.py && python run_m6_4_family_retrieval.py'

# 5. Watch + view the run
gh run list --workflow=nmb3_no_cache_repro.yml --repo <YOU>/nightingale-mapping --limit 1
gh run watch <run-id>  --repo <YOU>/nightingale-mapping
gh run view  <run-id>  --log --repo <YOU>/nightingale-mapping | tail -200
```

## Mode A — Local fresh clone (equivalent)

Requires `python>=3.11`, `git`, `ffmpeg` on `PATH`.

```bash
git clone https://github.com/stevewebmarket/nightingale-mapping.git
cd nightingale-mapping
git checkout 766cff65c2f868e37d344065c5188d69db88cf90
python -m venv .venv && source .venv/bin/activate
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir numpy scipy librosa soundfile
python scripts/fetch_samples.py
python run_m4_1_benchmark.py
python run_m6_4_family_retrieval.py
```

## Expected output (verify all four lines verbatim)

  - `TOTAL                                                      107/144   0.7431`
  - `  twinkle_box               top3=3 top5=3 outranks-all-nonfam=YES`
  - `  4. weak-evidence honestly flagged AND twinkle_people still weak: PASS`
  - `M6.4 PASS`

If any line is absent or differs, the reproduction has not
succeeded — do NOT silently accept partial matches.

## Out of scope

  - M3.1–M3.4, M4.1, M5.1–M5.5, M6.1–M6.3 (not SHA-pinned; see
    `nmb3/nmb3_packaging/reproducibility_appendix.md` § B).
  - M5.7 / M5.8 / M5.9 (NEGATIVE / FAIL / ABANDONED) and M6.5 (FAIL
    preserved; reproduced under O034).
  - Any claim of improvement, funding, commercial, or
    perceptual-validity.

## Reference dispatch

CI run id, headline-line verifications, and 90-day artefact name
for the reference dispatch performed under O039 are recorded in
`nmb3/nmb3_reports/o039_independent_reproduction_protocol.md`.
