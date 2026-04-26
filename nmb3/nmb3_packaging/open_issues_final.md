# NMB3 Open-Issues Register (Final)

This register is the single tracked-not-hidden open-issues
artefact for NMB3 at session-end.  It enumerates:

  - every item from `MILESTONES.md` § "Open issues (tracked,
    not hidden)" verbatim (Section 1); and
  - every additional tracked-not-hidden item that surfaced
    during NMB3 phases P0 – P8 (Section 2),

with a current status line for each.

Per O040's forbidden-actions register, **no tracked issue is
dropped** and **no open issue is reclassified as resolved
without explicit Steve approval**.  The status lines below
report only what evidence exists for or against each item; they
do not retire any item.

---

## Section 1 — Items from `MILESTONES.md` "Open issues (tracked, not hidden)"

### 1.1  rock time_stretch = 4/8 since M5.3

- **Source verbatim** (`MILESTONES.md` § Open issues, item 1):
  "rock time_stretch = 4/8 since M5.3.  Diagnosed as upstream
  cqt onset placement on percussive material, not the pitch
  window."
- **Current status**: OPEN.  The locked M5.6 baseline preserves
  this cell (the canonical 6-clip M4.1 benchmark TOTAL =
  107/144 = 0.7431 includes the rock × time_stretch = 4/8 cell;
  reproduced bit-identically under O023, O033, and O039).  The
  diagnosis (upstream cqt onset placement on percussive
  material, not the pitch window) is documented but no fix has
  been authorised; M5.7 (pyin tracker swap, NEGATIVE), M5.8
  (HPSS / harmonic pre-filter, NEGATIVE) and M5.9 (CREPE,
  ABANDONED) did not resolve it.  Not reclassified.

### 1.2  polyphonic = 5/24 (pitch-tracker limited)

- **Source verbatim** (`MILESTONES.md` § Open issues, item 2):
  "polyphonic = 5/24 is now believed to be pitch-tracker
  limited (pyin gets 10/24 there but breaks other clips; CREPE
  not yet tested)."
- **Current status**: OPEN.  M5.7 (pyin tracker swap,
  NEGATIVE at SHA `7fd167e`) and M5.9 (CREPE pitch tracker,
  ABANDONED) confirmed the diagnosis without resolving it.
  The locked M5.6 baseline preserves the polyphonic = 5/24
  cell.  Not reclassified.

### 1.3  voice-query family retrieval (`twinkle_people`)

- **Source verbatim** (`MILESTONES.md` § Open issues, item 3):
  "voice-query family retrieval (`twinkle_people`) remains a
  real pipeline limit — needs a better front-end pitch tracker
  for voice, not more retrieval engineering."
- **Current status**: OPEN.  Reproduced as the locked M6.4
  weak-evidence query under O033 (run id 24914929… at SHA
  `3929fbc`) and O039 (run id 24945531211 at SHA `766cff6`);
  the cond4 honesty self-check ("weak-evidence honestly flagged
  AND `twinkle_people` still weak: PASS") is preserved on every
  re-dispatch.  Not reclassified.

### 1.4  multi-family generalization (M6.5 NEGATIVE)

- **Source verbatim** (`MILESTONES.md` § Open issues, item 4):
  "multi-family generalization (M6.5 NEGATIVE) — the locked
  extractor + similarity pipeline does not generalise to a
  second independently-recorded melodic family without
  per-family tuning.  The honest read is that the Twinkle
  result is closer to a special case than to a general
  retrieval claim at the current pipeline maturity."
- **Current status**: OPEN here because `MILESTONES.md` § Open
  issues lists it.  Reproduced bit-identically under O034 (M6.5
  FAIL re-validation).  Note: the M6 phase closure
  recommendation (`nmb3/nmb3_reports/m6_phase_closure_recommendation.md`)
  reframes M6.5 as "part of the closed result, not as an open
  issue, not as a scheduled improvement"; that reframing is
  Steve-gated boundary doctrine and is recorded there, not
  here.  This register does NOT reclassify item 1.4 as
  resolved on the strength of that reframing.

---

## Section 2 — Items added during P0 – P8 (tracked-not-hidden)

### 2.1  M3.1 mid-range non-monotonicity

- **Added in**: P0 / `nmb3/nmb3_reports/m3_1_closure_recommendation.md`
  § "Open Questions That Closure Does Not Resolve" (item 1).
- **Source verbatim**: "Mid-range non-monotonicity.  Scores at
  0.10, 0.15, 0.20 sit in the −3 to −4 flip band but are not
  monotone (0.7917, 0.8125, 0.7917).  Real or sample-specific?
  Would need either per-case decomposition or an additional
  sample set to answer."
- **Current status**: OPEN.  M3.1 was closed by Steve at
  2026-04-25T16:34:20Z on the narrow reading defined in the
  closure recommendation; the non-monotonicity is part of that
  closure as a known characteristic, not contested.  No new
  evidence has been added since.

### 2.2  M3.1 perceptual correspondence untested

- **Added in**: P0 / m3_1_closure_recommendation.md
  § "Open Questions" (item 2).
- **Source verbatim**: "Perceptual correspondence.  Whether the
  score tracks human judgements of structural preservation is
  untested and is the strongest single thing that could either
  ratify or undermine the metric's broader meaning."
- **Current status**: OPEN.  Not tested in P0 – P8.
  `nmb3/nmb3_reports/boundary.md` § 5 explicitly excludes
  perceptual-validity studies from the current scope.

### 2.3  M3.1 sensitivity to non-`onset_delta` parameters untested

- **Added in**: P0 / m3_1_closure_recommendation.md
  § "Open Questions" (item 3).
- **Source verbatim**: "Other parameters.  Sensitivity to
  anything other than `onset_delta` is untested."
- **Current status**: OPEN.  Block 005 confirmed this remains
  out of scope; M5.4 (pitch-window ablation, NEGATIVE) and
  M5.5 (adaptive routing) explored adjacent parameters but did
  not perform a full sensitivity sweep over the M3.1 metric's
  parameter space.

### 2.4  M3.1 cross-corpus generalisation untested

- **Added in**: P0 / m3_1_closure_recommendation.md
  § "Open Questions" (item 4).
- **Source verbatim**: "Cross-corpus generalisation.
  Behaviour on samples outside the canonical 6-case set is
  unknown."
- **Current status**: OPEN.  M6.5 (multi-family on the Lamb
  family, NEGATIVE) provided a single second-corpus probe at
  the M6 retrieval layer; broader cross-corpus behaviour at
  the M3.1 metric layer remains untested.

### 2.5  Reproducibility gap on 13 of the 16 cited milestones

- **Added in**: P8 / O037 /
  `nmb3/nmb3_packaging/reproducibility_appendix.md` § Section B.
- **Source**: 13 milestones (M3.1, M3.2, M3.3, M3.4, M4.1, M5.1,
  M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3) lack a SHA-pinned
  no-cache CI run on canonical.  Only M5.6 (in Section A.1),
  M6.4 (Section A.2), and M6.5 (Section A.3) carry the no-cache
  CI guarantee documented in Section A of the reproducibility
  appendix.
- **Current status**: OPEN as gap, not failure.  An external
  reviewer who needs to verify any of the 13 must rely on
  `MILESTONES.md` and the named scripts in the canonical repo,
  without the no-cache CI evidence that Section A entries
  carry.  Backfilling these gaps would require Steve-authorised
  per-milestone objectives (e.g. O030 for M6.1, O031 for M6.2,
  O032 for M6.3 — currently PROPOSED, not authorised); the
  reproducibility appendix's Section B itself is forbidden by
  Steve's O037 rewrite from running a broader CI-pinning
  campaign within O037's scope.

### 2.6  Backend-version drift risk on `.m4a` decoding

- **Added in**: P6 / O033 § 7 risk table; reproduced as a
  documented risk under O039 § 4.
- **Source**: ffmpeg is the canonical decoder for `.m4a`; both
  canonical samples and the no-cache CI runner now use ffmpeg.
  Different ffmpeg versions across runners could in theory
  produce sub-percent feature drift on compressed clips (the
  M6.4 script's docstring warns of this).
- **Current status**: OPEN as risk; LOW probability of
  materialising.  No drift observed in the O023 / O033 / O039
  dispatches, all of which used `ubuntu-latest`'s bundled
  ffmpeg.  Mitigations recorded in O033 § 7: (a) the no-cache
  workflow re-installs ffmpeg on every runner so the cached-
  binary failure mode is excluded; (b) M5.6, M6.4, and M6.5
  reproductions match cell-for-cell on every dispatch to date.

---

## Section 3 — What this register does NOT do

  - It does NOT reclassify any `MILESTONES.md` "Open issues"
    item as resolved.
  - It does NOT advance any other objective (only O040 moves
    to SUCCEEDED).
  - It does NOT authorise the upstream re-validations
    (O030 / O031 / O032) implied by item 2.5; those remain
    PROPOSED awaiting Steve.
  - It does NOT reopen M3.1, M5.6, M6.4, M6.5, or any other
    closed milestone.
  - It does NOT make any improvement, funding, commercial, or
    perceptual-validity claim.

---

## Section 4 — Cross-reference index

| Register item | Original source | Re-validation evidence to date (if any) |
|---|---|---|
| 1.1 — rock 4/8 | `MILESTONES.md` § Open issues, item 1 | M5.6 reproduction in O023 / O033 / O039 (the cell appears in TOTAL = 107/144) |
| 1.2 — polyphonic 5/24 | `MILESTONES.md` § Open issues, item 2 | M5.6 reproduction in O023 / O033 / O039; M5.7 NEGATIVE at `7fd167e`; M5.9 ABANDONED |
| 1.3 — voice-query (`twinkle_people`) | `MILESTONES.md` § Open issues, item 3 | M6.4 weak-evidence query in O033 (run 24914929… @ `3929fbc`) and O039 (run 24945531211 @ `766cff6`); cond4 PASS preserved |
| 1.4 — M6.5 NEGATIVE | `MILESTONES.md` § Open issues, item 4 | M6.5 FAIL re-validation in O034; closure-doctrine reframing recorded in `m6_phase_closure_recommendation.md` (NOT applied here) |
| 2.1 — M3.1 mid-range non-monotonicity | `m3_1_closure_recommendation.md` § Open Questions | Block 005 |
| 2.2 — M3.1 perceptual correspondence | `m3_1_closure_recommendation.md` § Open Questions | None (out of scope per boundary.md § 5) |
| 2.3 — M3.1 other-parameters sensitivity | `m3_1_closure_recommendation.md` § Open Questions | Block 005 (in-scope-only); M5.4 / M5.5 adjacent |
| 2.4 — M3.1 cross-corpus | `m3_1_closure_recommendation.md` § Open Questions | M6.5 (single second-corpus probe, NEGATIVE) |
| 2.5 — reproducibility gap on 13 | `reproducibility_appendix.md` § Section B | Section A covers M5.6 / M6.4 / M6.5 only |
| 2.6 — ffmpeg drift | O033 § 7 risk table; O039 § 4 | O023 / O033 / O039 dispatches all clean |
