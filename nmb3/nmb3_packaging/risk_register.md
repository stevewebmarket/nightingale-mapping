# NMB3 Risk Register (Final)

This register makes explicit the principal risks to the NMB3
result corpus at session-end.  It covers five categories
(per O041's spec):

  1. **Scientific risk** — boundary at M6.5
  2. **Reproducibility risk** — CI infrastructure drift
  3. **Perceptual-validity risk** — untested human-judgement
     correspondence
  4. **Corpus risk** — canonical 6-case set
  5. **Process risk** — autonomous loop failure modes

Per O041's forbidden-actions register:

  - the **perceptual-validity risk** (Section 3) is included
    in full and is not omitted; and
  - the **M6.5 boundary risk** (Section 1) is rated REALISED
    × SIGNIFICANT and is not understated, softened to "open
    issue", or reframed as "scheduled improvement".

---

## Scales used

**Likelihood scale**
| Code | Meaning |
|---|---|
| VERY LOW  | <1% chance over the next session-equivalent of activity |
| LOW       | 1–10% |
| MEDIUM    | 10–50% |
| HIGH      | >50% |
| REALISED  | the risk has already materialised; this is a current-state finding, not a future-risk forecast |

**Impact scale**
| Code | Meaning |
|---|---|
| LIMITED      | confined to a single milestone or interpreter output; correctable in-loop |
| MODERATE     | requires a packaging-arc revision; does not invalidate any locked baseline |
| SIGNIFICANT  | bounds the scope of an external citation; locked baselines remain valid but their cited reach must be narrowed |
| SEVERE       | invalidates a locked baseline or a packaging artefact; requires Steve-authorised re-validation |
| CATASTROPHIC | invalidates the entire NMB3 result chain |

---

## Section 1 — Scientific risk: boundary at M6.5

| ID | Risk description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1.1 | The locked M5.6 extractor + M6.1/M6.2/M6.3-derived similarity pipeline does not generalise to a second independently-recorded melodic family (the Lamb family) without per-family tuning.  M6.5 returned a NEGATIVE multi-family-retrieval verdict, reproduced bit-identically under O034.  Any external citation that quotes the M6.4 Twinkle PASS without co-citing the M6.5 Lamb FAIL risks misrepresenting the scope of validity. | REALISED | SIGNIFICANT | Co-citation discipline binding: M6.4 PASS and M6.5 FAIL must be cited together (`m6_phase_closure_recommendation.md` item 1; `boundary.md` § 2/3 enforces co-location).  Open-issues register `open_issues_final.md` § 1.4 carries M6.5 as OPEN.  Any future second-corpus claim requires Steve-authorised per-family tuning + new CI evidence; extrapolation from M6.4 is forbidden.  M6.5 boundary doc reframing (`m6_phase_closure_recommendation.md`) is recorded as closure doctrine but is NOT applied as a resolution in the open-issues register. |

---

## Section 2 — Reproducibility risk: CI infrastructure drift

| ID | Risk description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 2.1 | Drift on the 3 SHA-pinned milestones (M5.6, M6.4, M6.5) caused by external infrastructure change: backend-version drift (ffmpeg `.m4a` decoder), library-version drift (numpy / scipy / librosa / soundfile), sample drift, caching contamination, or runner-image change on `ubuntu-latest`. | LOW | SIGNIFICANT | Shared no-cache workflow `.github/workflows/nmb3_no_cache_repro.yml` (canonical at SHA `3929fbc` since O033, unmodified through O039 / O040 / O041): no `actions/cache` step; `pip install --no-cache-dir`; checkout fresh; `scripts/fetch_samples.py` fetches samples on every run.  Independent reproduction protocol `independent_reproduction_protocol.md` documents both Mode A (local fresh clone) and Mode B (CI re-dispatch).  Reference dispatches O023 / O033 / O039 produced bit-identical M5.6 cells (18/18) and M6.4 rows (3/3) on three independent runner images; no drift observed to date.  Periodic re-dispatch is Steve-authorised and recorded under each objective. |
| 2.2 | Reproducibility gap on the 13 unpinned milestones (M3.1, M3.2, M3.3, M3.4, M4.1, M5.1, M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3): no SHA-pinned no-cache CI run on canonical exists for any of these.  External reviewers must currently rely on `MILESTONES.md` and the named scripts in the canonical repo for these 13. | REALISED | MODERATE | Documented in `reproducibility_appendix.md` § Section B (gap list) and `open_issues_final.md` § 2.5.  Locked baselines in `MILESTONES.md` remain the operative results for any current citation.  Backfilling these gaps would require Steve-authorised per-milestone objectives (O030 / O031 / O032 currently PROPOSED for M6.1 / M6.2 / M6.3); no aggregate backfill campaign is in scope.  Incidental reproduction inside the M6.4 / M6.5 leaderboards (O033 § 6, O034 § 5) provides observational evidence that M6.1 / M6.2 / M6.3 baselines reproduce on the M6.4 / M6.5 head SHAs, but is NOT formal re-validation. |

---

## Section 3 — Perceptual-validity risk

| ID | Risk description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 3.1 | The M3.1 metric correlates with known structural perturbations (pitch_shift, time_stretch, composition) on the canonical 6-case set, but its correspondence with human judgements of structural preservation is untested.  Per `m3_1_closure_recommendation.md` § Open Questions item 2 (verbatim): "Whether the score tracks human judgements of structural preservation is untested and is the strongest single thing that could either ratify or undermine the metric's broader meaning."  Any external citation that uses the M3.1 metric as a proxy for human-perceived similarity is currently unsupported. | REALISED | SIGNIFICANT | Explicitly excluded from current scope: `boundary.md` § 5 lists perceptual-validity studies as out-of-scope; `open_issues_final.md` § 2.2 carries the risk as OPEN.  Any future perceptual-validity probe is Steve-gated and requires its own corpus design (human-rater protocol + sample selection) and its own objective; no autonomous-loop authorisation will be sufficient.  All current packaging artefacts (reproducibility appendix, methodology appendix, independent reproduction protocol, open-issues register, this risk register) explicitly disclaim any perceptual-validity claim in their non-claim sections. |

---

## Section 4 — Corpus risk: canonical 6-case set

| ID | Risk description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 4.1 | The canonical 6-clip M4.1 benchmark set drives every M4 / M5 number (M5.6 TOTAL = 107/144 = 0.7431 is computed over this set).  The M6 family-retrieval evidence is built on a single Twinkle family (4 clips) + 5-clip non-family library (M6.4 PASS) and a single Lamb family (M6.5 FAIL).  Cross-corpus generalisation at the M3.1 metric layer is untested.  Cross-family generalisation at the M6 retrieval layer is exactly the M6.5 boundary (Section 1).  Any external citation that omits the canonical-set caveat risks overstating the corpus reach. | REALISED | SIGNIFICANT | Every milestone in `MILESTONES.md` carries explicit corpus-scope language; every interpreter output's "What this report does NOT claim" section disclaims corpus extension; `open_issues_final.md` § 2.4 carries cross-corpus generalisation as OPEN.  Cross-corpus probes are Steve-gated.  The M6.5 Lamb probe (the only second-corpus probe to date) returned NEGATIVE and is co-cited under § 1.1 above as the realised boundary. |

---

## Section 5 — Process risk: autonomous loop failure modes

This section enumerates the loop-discipline failure modes that
the autonomous research loop must defend against.  Each row
maps to a specific clause in `nmb3_autonomous_loop_policy.md`,
`nmb3_decision_policy.md`, or one of the prior interpreter
outputs' risk tables.

| ID | Risk description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 5.1 | **Metric gaming.**  The loop optimises for verbatim-string approval rather than for measurement integrity (e.g. relaxing a self-check threshold to make a query PASS; reclassifying a NEGATIVE result as "scheduled improvement"). | VERY LOW | CATASTROPHIC | `nmb3_decision_policy.md` § measurement integrity binds the loop.  `nmb3_autonomous_loop_policy.md` § Early Stop Conditions: "Stop immediately ... metric gaming is suspected".  M6.4 cond4 honesty self-check ("weak-evidence honestly flagged AND `twinkle_people` still weak: PASS") is preserved on every dispatch (O033 / O039).  Architect review on every objective checks for self-check tampering.  Open-issues register § 1.3 explicitly preserves the `twinkle_people` weak-evidence flag.  M6.5 NEGATIVE preserved without softening.  No metric-gaming incident has been recorded across phases P0 – P8. |
| 5.2 | **Aggregation drift / scope creep.**  An interpreter output for objective O_n implicitly advances another objective O_m by reporting incidental observations as if they were formal evidence (e.g. claiming O030 / O031 / O032 are SUCCEEDED on the strength of O033 § 6 incidental reproduction). | LOW | MODERATE | Every interpreter output carries a "What this report does NOT claim" section listing exactly which other objectives it does NOT advance.  Objective-map Status field is the single source of truth for objective state; only the architect-approved interpreter output for objective O_n is allowed to move O_n's status.  `m6_phase_closure_recommendation.md` § 6 row 3 explicitly flags this as a closure-governance risk addressed by enumerating each objective by current canonical status. |
| 5.3 | **Workflow yml mutation creep.**  The shared no-cache workflow `.github/workflows/nmb3_no_cache_repro.yml` becomes coupled to per-objective logic over time, undermining its role as a neutral reproduction substrate. | LOW | SIGNIFICANT | Workflow yml-edit budget: 2 edits per session maximum, recorded in each objective's decisions.log entry.  Shared workflow yml unchanged from canonical at SHA `3929fbc` since O033's ffmpeg add; loops 1 – 3 of the current session consumed 0 of 2.  Each interpreter output records the workflow yml status under its risk-assessment section.  Any new workflow file creation is forbidden by O033 / O039 / O040 / O041 specs. |
| 5.4 | **Cherry-picking / silent retry.**  A first dispatch returns an unfavourable result and is silently discarded; the second dispatch's favourable result is reported as the reproduction. | LOW | SEVERE | `nmb3_decision_policy.md` forbids cherry-picking.  Every retry must be documented honestly in the interpreter output (e.g. O033 § 5 documents the missing-ffmpeg infrastructure failure on the first dispatch and the second-dispatch reproduction; O039 first dispatch produced the reproduction so no retry was needed).  Architect review on every objective checks for undocumented-retry patterns.  Per Block 022 plan and subsequent interpreter outputs: only infrastructure failures (e.g. missing ffmpeg) may be retried; result-driven retries are forbidden. |
| 5.5 | **Forbidden-action violation.**  An autonomous loop edits a file it is forbidden to edit (script, pipeline file, policy file, `MILESTONES.md`, `nmb3_README.md`); creates a new workflow file when forbidden; or dispatches more than the spec-permitted number of CI runs (e.g. O039's "ONCE" wording). | LOW | SEVERE | Each interpreter output and each decisions.log entry explicitly enumerates the forbidden-file set and confirms "no script edited; no pipeline file edited; no policy file edited; no MILESTONES.md edited; no nmb3_README.md edited".  Architect review uses `git diff` against canonical to enforce the cumulative diff scope.  CI dispatch counts are recorded in each objective's interpreter output § Pinning section. |

---

## Section 6 — What this register does NOT do

  - It does NOT propose any mitigation that would require
    Steve-gated authorisation; every mitigation listed above
    is already in force at session-end.
  - It does NOT advance, revise, or retire any objective other
    than O041 itself.
  - It does NOT downgrade the M6.5 boundary risk (Section 1) to
    LOW likelihood, MODERATE impact, "open issue", or
    "scheduled improvement".  M6.5 remains REALISED ×
    SIGNIFICANT.
  - It does NOT omit the perceptual-validity risk (Section 3).
  - It does NOT make any improvement, funding, commercial, or
    perceptual-validity claim.
  - It does NOT formally re-validate any milestone (the
    SHA-pinned reference dispatches recorded in O023 / O033 /
    O034 / O039 are the operative reproduction evidence; this
    register cites them but does not re-run them).

---

## Section 7 — Cross-reference index

| Section | Original source(s) | Re-validation evidence (if any) |
|---|---|---|
| 1.1 (M6.5 boundary) | `MILESTONES.md` § M6.5; `open_issues_final.md` § 1.4; `boundary.md` § 2/3; `m6_phase_closure_recommendation.md` items 1 – 2 | O034 (M6.5 FAIL re-validation, bit-identical) |
| 2.1 (drift on SHA-pinned 3) | O023 / O033 / O039 § risk tables; `independent_reproduction_protocol.md` | O023 (M5.6), O033 (M6.4), O034 (M6.5), O039 (M5.6 + M6.4) |
| 2.2 (gap on 13 unpinned) | `reproducibility_appendix.md` § Section B; `open_issues_final.md` § 2.5 | Incidental observations only (O033 § 6, O034 § 5, O039 § 5); no formal re-validation |
| 3.1 (perceptual validity) | `m3_1_closure_recommendation.md` § Open Questions item 2; `boundary.md` § 5; `open_issues_final.md` § 2.2 | None (out of scope) |
| 4.1 (corpus) | `MILESTONES.md` § M3.1 / M4.1 / M6.4 / M6.5; `m3_1_closure_recommendation.md` § Open Questions item 4; `open_issues_final.md` § 2.4 | M6.5 (single second-corpus probe, NEGATIVE, O034) |
| 5.1 (metric gaming) | `nmb3_decision_policy.md` § measurement integrity; `nmb3_autonomous_loop_policy.md` § Early Stop Conditions | M6.4 cond4 PASS preserved (O033, O039); M6.5 NEGATIVE preserved (O034) |
| 5.2 (aggregation drift) | `m6_phase_closure_recommendation.md` § 6 row 3; every interpreter output's "What this report does NOT claim" section | All P0 – P8 interpreter outputs carry the disclaimer |
| 5.3 (yml mutation creep) | O033 / O039 / O040 / O041 specs; each decisions.log entry's "Workflow yml-edit budget consumed" line | Workflow yml unchanged from canonical at SHA `3929fbc` since O033 |
| 5.4 (cherry-picking) | `nmb3_decision_policy.md`; Block 022 plan; O033 § 5; O039 § 4 row 4 | O033 single-retry honestly documented; O039 single-dispatch no retry |
| 5.5 (forbidden-action) | Each objective's spec; each interpreter output's risk-assessment section | Architect `git diff` review on every objective |
