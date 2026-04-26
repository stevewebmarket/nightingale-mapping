# O041 Interpreter Output — Risk Register (Final)

Generated:   2026-04-26T03:20:00Z
Objective:   O041 — Risk register
             (`nmb3/nmb3_objective_map.md`, P8 packaging arc,
             after O040 open-issues register)
Verdict:     **PASS — risk register artefact written; all five
             spec'd risk categories present; each row has
             likelihood, impact, and mitigation columns;
             perceptual-validity risk included; M6.5 boundary
             risk rated REALISED × SIGNIFICANT (not
             understated).**

---

## 1. Pinning

  - **Register artefact:**     `nmb3/nmb3_packaging/risk_register.md`
                               (131 source lines).
  - **Authoritative-text SHA:**  introduced at the commit that
                               closes O041 on `main`; this
                               interpreter output is the
                               companion evidence.
  - **CI run:**                NONE.  O041 is documentation-only
                               per spec; the register aggregates
                               risk material from prior
                               objectives' risk-assessment
                               sections (O023 / O033 / O034 /
                               O037 / O039), the M3.1 closure
                               recommendation, the M6 phase
                               closure recommendation, the
                               boundary doc, the open-issues
                               register, the autonomous-loop
                               policy, and the decision policy.
  - **Workflow inputs:**       N/A.

## 2. What was written and how

A single markdown register at
`nmb3/nmb3_packaging/risk_register.md` with seven sections:

  1. **Sections 1 – 5** — one per spec-required risk category,
     each as a markdown table with the spec-required columns
     (Likelihood, Impact, Mitigation) plus an ID column for
     cross-reference and a Risk-description column carrying
     the verbatim formulation:
       - § 1: Scientific risk — boundary at M6.5 (1 row)
       - § 2: Reproducibility risk — CI infrastructure drift
         (2 rows: SHA-pinned vs unpinned)
       - § 3: Perceptual-validity risk (1 row)
       - § 4: Corpus risk — canonical 6-case set (1 row)
       - § 5: Process risk — autonomous loop failure modes
         (5 rows: metric gaming; aggregation drift; yml
         mutation creep; cherry-picking; forbidden-action
         violation)
  2. **Section 6** — explicit non-claim register (what the
     register does NOT do).
  3. **Section 7** — cross-reference index linking each row
     to its original source(s) and to any re-validation
     evidence.

A "Scales used" preamble between the introduction and Section 1
defines the Likelihood scale (VERY LOW < LOW < MEDIUM < HIGH <
REALISED) and the Impact scale (LIMITED < MODERATE <
SIGNIFICANT < SEVERE < CATASTROPHIC).

No script edited; no pipeline file edited; no policy file
edited; no `MILESTONES.md` edited; no `nmb3_README.md` edited.
No CI workflow file edited or dispatched.

## 3. Success criteria check

O041 spec verbatim:

> Success criteria: `nmb3/nmb3_packaging/risk_register.md`
> exists; each risk has a likelihood, impact, and mitigation
> column.

### 3.1  Register file exists

| Property | Value |
|---|---|
| Path | `nmb3/nmb3_packaging/risk_register.md` |
| Source line count | 131 lines markdown source |
| Sections | Header / Scales used / Section 1 (1 row) / Section 2 (2 rows) / Section 3 (1 row) / Section 4 (1 row) / Section 5 (5 rows) / Section 6 (non-claim register) / Section 7 (cross-reference index) |
| Total risk rows | 10 |

**PASS.**  Register written and committed.

### 3.2  Each risk has Likelihood, Impact, and Mitigation columns

Every table in Sections 1 – 5 carries the column header row
`| ID | Risk description | Likelihood | Impact | Mitigation |`.
Spot-check across all 10 rows:

| Section | Row count | Likelihood column populated | Impact column populated | Mitigation column populated |
|---|---|---|---|---|
| § 1 (scientific) | 1 | ✅ (REALISED) | ✅ (SIGNIFICANT) | ✅ (co-citation discipline; open-issues § 1.4; boundary doc) |
| § 2 (reproducibility) | 2 | ✅ (LOW; REALISED) | ✅ (SIGNIFICANT; MODERATE) | ✅ (no-cache workflow; reproducibility appendix § B; per-milestone closure) |
| § 3 (perceptual) | 1 | ✅ (REALISED) | ✅ (SIGNIFICANT) | ✅ (boundary § 5; Steve-gated probe; non-claim sections) |
| § 4 (corpus) | 1 | ✅ (REALISED) | ✅ (SIGNIFICANT) | ✅ (corpus-scope language; M6.5 second-corpus probe; Steve-gated extension) |
| § 5 (process) | 5 | ✅ (VERY LOW; LOW × 4) | ✅ (CATASTROPHIC; MODERATE; SIGNIFICANT; SEVERE × 2) | ✅ (decision policy; loop policy; architect review; cumulative-diff check) |

**PASS.**  All 10 rows carry all three required columns.

### 3.3  Forbidden actions check

O041 spec forbids: "omitting the perceptual-validity risk;
understating the M6.5 boundary risk".

| Forbidden action | Status in register |
|---|---|
| Omitting the perceptual-validity risk | NOT done; § 3.1 carries the verbatim quote from `m3_1_closure_recommendation.md` § Open Questions item 2 ("the strongest single thing that could either ratify or undermine the metric's broader meaning") and rates the risk REALISED × SIGNIFICANT |
| Understating the M6.5 boundary risk (rating it LOW likelihood, MODERATE impact, "open issue", or "scheduled improvement") | NOT done; § 1.1 rates M6.5 REALISED × SIGNIFICANT, names the M6.5 NEGATIVE result explicitly, requires co-citation with M6.4 PASS, and § 6 ("What this register does NOT do") explicitly forbids downgrading § 1 to LOW × MODERATE or "open issue" / "scheduled improvement" |

**PASS.**  No forbidden action performed.

### 3.4  Spec-category completeness check

O041 spec lists five required categories; all five are present
as their own dedicated section in the register:

| Spec-named category | Register section | Verbatim mapping |
|---|---|---|
| "scientific risk (boundary at M6.5)" | § 1 | § 1 title is "Scientific risk: boundary at M6.5"; § 1.1 names the M6.5 NEGATIVE result explicitly. |
| "reproducibility risk (CI infrastructure drift)" | § 2 | § 2 title is "Reproducibility risk: CI infrastructure drift"; § 2.1 covers SHA-pinned, § 2.2 covers gap. |
| "perceptual-validity risk (metric responds to known parameters but not to perceptual judgements, untested)" | § 3 | § 3 title is "Perceptual-validity risk"; § 3.1 quotes the m3_1 verbatim "untested" wording. |
| "corpus risk (canonical 6-case set)" | § 4 | § 4 title is "Corpus risk: canonical 6-case set"; § 4.1 names the 6-clip benchmark and the single-family M6.4/M6.5 corpora. |
| "process risk (autonomous loop failure modes)" | § 5 | § 5 title is "Process risk: autonomous loop failure modes"; 5 rows enumerate metric gaming, aggregation drift, yml mutation creep, cherry-picking, forbidden-action violation. |

**PASS.**  All five spec-named categories present.

## 4. Risk assessment (of this register itself)

| Risk | Status | Notes |
|---|---|---|
| Spec-required category omitted | None | All 5 spec-named categories carried; § 3.4 above tabulates the verbatim mapping. |
| Perceptual-validity risk omitted (forbidden) | None | § 3.1 carries the risk; verbatim m3_1 quote preserved. |
| M6.5 boundary risk understated (forbidden) | None | § 1.1 rated REALISED × SIGNIFICANT; § 6 explicitly forbids downgrade. |
| Scope creep into recommending mitigations not yet in force | None | § 6 first bullet: "It does NOT propose any mitigation that would require Steve-gated authorisation; every mitigation listed above is already in force at session-end." |
| Funding / improvement / commercial / perceptual-validity claim slip-in | None | § 6 explicit non-claim register. |
| Workflow yml mutation | None | No CI workflow file edited or dispatched.  Workflow yml-edit budget consumed this loop: 0 of 2. |
| MILESTONES.md / nmb3_README.md edit | None | Neither file edited. |
| Cumulative-diff scope | Clean | Three files only: register, this interpreter output, objective map status. |

## 5. What this report does NOT claim

  - It does not advance any objective other than O041.
  - It does not formally re-validate any milestone (the
    SHA-pinned reference dispatches recorded in O023 / O033 /
    O034 / O039 are the operative reproduction evidence).
  - It does not authorise any new mitigation; every mitigation
    listed in the register is already in force at session-end.
  - It does not retire or downgrade any open issue listed in
    `open_issues_final.md` (O040).
  - It does not make any improvement, funding, commercial, or
    perceptual-validity claim.

## 6. Recommended next move

Per the autonomous loop policy "Session Completion Rule", the
loop stops on objective success and proposes the next objective
without beginning it.  Standing constraint "do not execute the
whole preferred path yet" still active.

Natural next options after O041, given the packaging arc is
now five artefacts deep (O037 reproducibility appendix + O038
methodology appendix + O039 independent reproduction protocol +
O040 open-issues register + O041 risk register):

  - **O042 / next P9 objective** if the funding-package phase
    is now in scope (note: O041 spec's forbidden-actions list
    does not authorise funding work; any P9 work requires
    Steve's explicit authorisation per `nmb3_decision_policy.md`).
  - Authorise the upstream M6.1 / M6.2 / M6.3 formal
    re-validations (O030 / O031 / O032), which would close
    register § 2.2 (reproducibility gap on 13).
  - **Pause.**

Awaiting Steve.
