# O040 Interpreter Output — Open-Issues Register (Final)

Generated:   2026-04-26T02:45:00Z
Objective:   O040 — Open-issues register (final)
             (`nmb3/nmb3_objective_map.md`, P8 packaging arc,
             after O039 independent reproduction protocol)
Verdict:     **PASS — register artefact written; every
             `MILESTONES.md` "Open issues" item appears verbatim;
             6 additional tracked-not-hidden items added during
             P0 – P8 included with current status; no
             reclassification.**

---

## 1. Pinning

  - **Register artefact:**     `nmb3/nmb3_packaging/open_issues_final.md`
                               (207 source lines).
  - **Authoritative-text SHA:**  introduced at the commit that
                               closes O040 on `main`; this
                               interpreter output is the
                               companion evidence.
  - **CI run:**                NONE.  O040 is documentation-only
                               per its spec; the register
                               aggregates evidence from prior
                               objectives (O023 / O033 / O034 /
                               O037 / O039 dispatches and
                               m3_1 P0 closure work).  No CI
                               dispatch was performed for O040.
  - **Workflow inputs:**       N/A.

## 2. What was written and how

A single markdown register at
`nmb3/nmb3_packaging/open_issues_final.md` with four sections:

  1. **Section 1** — every item from `MILESTONES.md` § "Open
     issues (tracked, not hidden)" reproduced verbatim, each
     with a current status line that does NOT reclassify the
     item as resolved.
  2. **Section 2** — six tracked-not-hidden items that surfaced
     during NMB3 phases P0 – P8 (4 from `m3_1_closure_recommendation.md`
     § "Open Questions That Closure Does Not Resolve"; 1 from
     `reproducibility_appendix.md` § Section B; 1 from O033 § 7
     risk table re-recorded under O039 § 4).
  3. **Section 3** — explicit non-claim register (what the
     register does NOT do).
  4. **Section 4** — cross-reference index linking each item
     to its original source and to any re-validation evidence.

No script edited; no pipeline file edited; no policy file
edited; no `MILESTONES.md` edited; no `nmb3_README.md` edited.
No CI workflow file edited or dispatched.

## 3. Success criteria check

O040 spec verbatim:

> Success criteria: `nmb3/nmb3_packaging/open_issues_final.md`
> exists; every item from `MILESTONES.md` "Open issues" appears.

### 3.1  Register file exists

| Property | Value |
|---|---|
| Path | `nmb3/nmb3_packaging/open_issues_final.md` |
| Source line count | 207 lines markdown source |
| Sections | Header / Section 1 (4 items) / Section 2 (6 items) / Section 3 (non-claim register) / Section 4 (cross-reference index) |

**PASS.**  Register written and committed.

### 3.2  Every `MILESTONES.md` "Open issues" item appears verbatim

`MILESTONES.md` § "Open issues (tracked, not hidden)" contains
exactly four items.  All four are reproduced verbatim in the
register's Section 1:

| `MILESTONES.md` item (verbatim trigger phrase) | Register § | Reproduced verbatim |
|---|---|---|
| "rock time_stretch = 4/8 since M5.3.  Diagnosed as upstream cqt onset placement on percussive material, not the pitch window." | § 1.1 | ✅ |
| "polyphonic = 5/24 is now believed to be pitch-tracker limited (pyin gets 10/24 there but breaks other clips; CREPE not yet tested)." | § 1.2 | ✅ |
| "voice-query family retrieval (`twinkle_people`) remains a real pipeline limit — needs a better front-end pitch tracker for voice, not more retrieval engineering." | § 1.3 | ✅ |
| "multi-family generalization (M6.5 NEGATIVE) — the locked extractor + similarity pipeline does not generalise to a second independently-recorded melodic family without per-family tuning.  The honest read is that the Twinkle result is closer to a special case than to a general retrieval claim at the current pipeline maturity." | § 1.4 | ✅ |

**PASS.**  4 of 4 `MILESTONES.md` open-issue items reproduced
verbatim.

### 3.3  Forbidden actions check

O040 spec forbids: "dropping any tracked issue; reclassifying
any open issue as resolved without explicit Steve approval".

| Forbidden action | Status in register |
|---|---|
| Dropping any `MILESTONES.md` "Open issues" item | NOT done; all 4 present in § 1.1–1.4 |
| Dropping any P0–P8-added tracked item | NOT done; 4 from m3_1_closure_recommendation.md § "Open Questions" + reproducibility-gap + ffmpeg-drift all present in § 2.1–2.6 |
| Reclassifying item 1.4 (M6.5) as resolved on the strength of the m6_phase_closure_recommendation.md reframing | NOT done; § 1.4 explicitly notes the reframing exists in that closure doc but does NOT apply it here ("This register does NOT reclassify item 1.4 as resolved on the strength of that reframing") |
| Reclassifying any other item as resolved | NOT done; every status line reads "OPEN" with evidence-summary text only |

**PASS.**  No forbidden action performed.

### 3.4  Items added during P0 – P8 (audit trail)

Per O040 spec wording "every tracked-not-hidden item from
`MILESTONES.md` 'Open issues' **plus any added during P1–P7**",
this audit was performed across the P0 – P8 corpus to identify
tracked-not-hidden additions.  P0 is included alongside P1 – P7
because the M3.1 closure work was the first NMB3 phase under
the autonomous-loop discipline and produced the largest single
batch of added open questions.  P8 is included for the
reproducibility-gap item (O037) and the ffmpeg-drift item
(O039) which are also tracked-not-hidden.

| Phase | Source | Items added |
|---|---|---|
| P0 (M3.1 closure) | `m3_1_closure_recommendation.md` § "Open Questions That Closure Does Not Resolve" | 4 (mid-range non-monotonicity; perceptual correspondence; other parameters; cross-corpus) → § 2.1 – 2.4 |
| P1 (M3.2/M3.3/M3.4 re-validation) | objective map, no new tracked-not-hidden items recorded | 0 |
| P2 (M4.1 re-validation) | objective map, no new tracked-not-hidden items recorded | 0 |
| P3 (M5.1/M5.2/M5.3 re-validation) | objective map, no new tracked-not-hidden items recorded | 0 |
| P4 (M5.4/M5.5/M5.6 re-validation) | objective map + `m5_phase_p4_closure_recommendation.md`, no new tracked-not-hidden items beyond what's already in `MILESTONES.md` § Open issues | 0 |
| P5 (M5.7/M5.8/M5.9 re-documentation) | objective map, NEGATIVE/ABANDONED outcomes recorded in `MILESTONES.md` status table; no new tracked-not-hidden items | 0 |
| P6 (M6.1–M6.4 re-validation) | O033 § 7 risk table | 1 (ffmpeg backend-version drift risk) → § 2.6 |
| P7 (M6.5 multi-family) | O034 + boundary doc; M6.5 NEGATIVE itself is already `MILESTONES.md` § Open issues item 4 | 0 |
| P8 (packaging artefacts) | `reproducibility_appendix.md` § Section B (gap list) | 1 (reproducibility gap on 13 milestones) → § 2.5 |

**Total**: 4 verbatim `MILESTONES.md` items + 6 P0–P8-added
items = 10 tracked-not-hidden open issues, all in the register.

## 4. Risk assessment

| Risk | Status | Notes |
|---|---|---|
| Drop-tracked-issue violation | None | All 4 `MILESTONES.md` items + all P0–P8-added items present and accounted for. |
| Reclassification violation | None | Every § 1 / § 2 status line reads "OPEN" with evidence-summary text only.  The boundary-doc reframing of M6.5 is recorded as an existing-elsewhere fact but explicitly NOT applied. |
| Drift / scope creep | None | Register limits itself to existing tracked items; no new claims, no improvement claims, no funding claims. |
| Workflow-yml edit | None | No CI workflow file edited or dispatched.  Workflow yml-edit budget consumed this loop: 0 of 2. |
| MILESTONES.md / README edit | None | Neither file edited. |
| Forbidden-action violation | None | See § 3.3 above. |

## 5. What this report does NOT claim

  - It does not advance any objective other than O040.
  - It does not formally re-validate any of the 13
    reproducibility-gap milestones in § 2.5.
  - It does not authorise the upstream re-validations (O030,
    O031, O032).
  - It does not retire the M6.5 NEGATIVE result on the strength
    of the m6_phase_closure_recommendation.md reframing.
  - It does not make any improvement, funding, commercial, or
    perceptual-validity claim.

## 6. Recommended next move

Per the autonomous loop policy "Session Completion Rule", the
loop stops on objective success and proposes the next objective
without beginning it.  Standing constraint "do not execute the
whole preferred path yet" still active.

Natural next options after O040, given the packaging arc is
now four artefacts deep (O037 reproducibility appendix + O038
methodology appendix + O039 independent reproduction protocol +
O040 open-issues register):

  - **O041** if it exists in the objective map as the next
    packaging step.
  - Authorise the upstream M6.1 / M6.2 / M6.3 formal
    re-validations (O030 / O031 / O032), which would convert
    the incidental observations in O033 § 6, O034 § 5, and
    O039 § 5 into formal evidence and would close
    register § 2.5 (reproducibility gap on 13).
  - **Pause.**

Awaiting Steve.
