# O042 Interpreter Output — Funding Scope Declaration (Steve gate)

Generated:   2026-04-26T04:00:00Z
Objective:   O042 — Funding package scope decision
             (`nmb3/nmb3_objective_map.md`, P9 funding-package
             phase, after O041 risk register SUCCEEDED clean
             at SHA `c25451a`)
Verdict:     **PASS — Steve verbatim 5-element string recorded
             in `nmb3/nmb3_decisions.log` at 2026-04-26T04:00:00Z;
             all five elements (a)-(e) present and explicit; no
             funder-facing prose drafted at this gate; no
             autonomous-loop suggestion of ask amount or
             continuation scope; M6.5 boundary condition (e)
             confirmed by Steve.**

---

## 1. Pinning

  - **Steve string location:**  `nmb3/nmb3_decisions.log`,
                                entry timestamped
                                `2026-04-26T04:00:00Z`,
                                between the `BEGIN STEVE
                                VERBATIM` / `END STEVE
                                VERBATIM` delimiters.
  - **Authoritative-text SHA:** introduced at the commit that
                                closes O042 on `main`; this
                                interpreter output is the
                                companion verification.
  - **CI run:**                 NONE.  O042 is a Steve gate;
                                the artefact is the log entry
                                itself.
  - **Prior-objective SHA:**    O041 SUCCEEDED clean at SHA
                                `c25451a` (P8 packaging arc
                                complete; risk register § 1.1
                                M6.5 boundary at REALISED ×
                                SIGNIFICANT).

## 2. What was recorded and how

A single delimited block was appended to `nmb3_decisions.log`
under a new dated section.  The block contains Steve's 5-element
declaration verbatim (preserving Steve's bullet structure and
parenthetical examples).  No prose was added inside the
delimiters; the only autonomous-loop additions in this commit
are:

  - the dated section header line,
  - the brief framing line that names this entry as the O042
    evidence (per spec "Evidence required: log entry containing
    all five elements (a)-(e)"),
  - the 4-line "Loop posture" footer that records dependency
    state for the next objective (O043) without beginning it.

No funder-facing prose has been drafted.  No ask amount or
continuation scope has been suggested by the autonomous loop.
The autonomous loop's role under this gate, per the O042 spec
"Allowed autonomous actions" register, is exhausted by:

  - presenting the five-element question to Steve (done in the
    O041 close-out next-options menu),
  - restating the Decision Policy "no funding claim without
    Steve approval" rule (carried by every prior packaging
    artefact's non-claim register; restated in § 5 below), and
  - quoting the `MILESTONES.md` "Current boundary" section
    verbatim (§ 4 below).

## 3. Success-criteria check

O042 spec verbatim:

> Success criteria: Steve string in `nmb3_decisions.log`
> specifying:
> (a) funder type / audience;
> (b) ask amount or range;
> (c) the locked claim set the package is allowed to assert
>     about *existing* validated evidence;
> (d) the continuation-work scope the ask funds, named at the
>     level of milestone candidates (e.g., "CREPE integration
>     as the first continuation milestone, voice-friendly
>     extractor as the second, second-corpus generalisation as
>     the third");
> (e) explicit confirmation that the M6.5 boundary will be
>     stated honestly in the funder-facing material as the
>     *reason* for the continuation ask, not hidden by it.

### 3.1  Element-by-element coverage

| Spec element | Steve's verbatim wording (paraphrase-free) | Coverage |
|---|---|---|
| (a) funder type / audience | "Technical research funders / AI labs (e.g. xAI, OpenAI-level research groups)" | PASS — specific funder type ("technical research funders / AI labs") plus two named exemplars. |
| (b) ask amount or range | "€250k-€750k initial funding" | PASS — explicit range with currency and the qualifier "initial". |
| (c) locked-claim set about existing validated evidence | 5 bullets: "Metric runs end-to-end / Reproduces exactly on clean CI / Responds to timing changes (real signal) / Has a clear failure boundary (M6.5) / M5.6, M6.4, M6.5 results are reproducible and SHA-pinned" | PASS — five distinct claims, each anchored in the locked record (M3.1 metric end-to-end; O023 / O033 / O039 SHA-pinned no-cache CI; M3.1 / M5.6 perturbation responses; M6.5 boundary; SHA-pinned reproduction across M5.6 / M6.4 / M6.5). |
| (d) continuation-work scope at milestone-candidate level | 4 bullets: "Voice-friendly / polyphonic-capable extractor / Extension beyond canonical 6-case dataset / Cross-corpus generalisation / Perceptual validation layer" | PASS — four named candidate continuation milestones at the same granularity as the spec example. |
| (e) M6.5 boundary stated honestly as the reason for the continuation ask, not hidden | "The M6.5 failure boundary will be stated explicitly and used as the primary motivation for the continuation work, not hidden or softened." | PASS — Steve's wording uses "primary motivation" (= "reason for the continuation ask" in the spec) and "not hidden or softened" (= "not hidden by it" in the spec). |

All five elements present.  **PASS.**

### 3.2  Forbidden-actions check

O042 spec forbids: "drafting any funder-facing prose before the
five-element string exists; suggesting an ask amount or a
continuation scope on Steve's behalf; proposing continuation
work whose success criteria would require softening the M6.5
boundary; treating any new algorithmic work as *executed* under
this objective".

| Forbidden action | Status |
|---|---|
| Drafting any funder-facing prose | NOT done.  Only the verbatim Steve string + interpreter output + objective-map status update were written; no funder-facing copy authored. |
| Suggesting an ask amount on Steve's behalf | NOT done.  The €250k-€750k range is Steve's, not the loop's. |
| Suggesting a continuation scope on Steve's behalf | NOT done.  The 4 continuation-work bullets in element (d) are Steve's, not the loop's.  Note: Steve named "Voice-friendly / polyphonic-capable extractor" rather than the spec example "CREPE integration"; the loop preserved Steve's wording without substitution. |
| Proposing continuation work that would soften the M6.5 boundary | NOT done.  Each of Steve's 4 continuation items pushes *past* the M6.5 boundary by changing the front-end (extractor / corpus / perceptual layer); none of them re-classifies M6.5 as resolved within the locked pipeline.  Element (e) explicitly reaffirms the boundary will be stated, not hidden. |
| Treating new algorithmic work as *executed* under O042 | NOT done.  No code was written; no script edited; no scope item is recorded as anything other than an unstarted continuation candidate.  All four (d)-bullets remain candidate scopes for separately-funded follow-on programmes, per the spec's framing. |

**PASS.**  No forbidden action performed.

### 3.3  Cross-check against O042 dependencies

O042 declares Dependencies: O041.  At session-end:

| Dependency | Status | Evidence |
|---|---|---|
| O041 (risk register, final) | SUCCEEDED clean at SHA `c25451a` | `nmb3/nmb3_packaging/risk_register.md` (131 lines); architect APPROVED CLEAN on first review; risk register § 1.1 rates M6.5 REALISED × SIGNIFICANT, exactly the framing element (e) reaffirms. |

Dependency satisfied.

## 4. Anchoring the continuation-scope discussion in the locked record

Per O042 "Allowed autonomous actions": *quote the `MILESTONES.md`
"Current boundary" section verbatim so the continuation-scope
discussion is anchored in the locked record.*

`MILESTONES.md` § "Current boundary" (lines 40-53), verbatim:

> ## Current boundary
>
> * **What works:** small-library retrieval by structural similarity on
>   **clean instrumental melodic families** (M6.4 Twinkle result).
> * **What does not yet work:** **voice-heavy / weak-melodic extraction**
>   -- when the M5.6 pitch tracker recovers fewer than ~4 non-trivial
>   intervals from a clip, similarity scores collapse into the same band
>   as unrelated clips and family-level separation disappears (M6.5 Lamb
>   result, and the `twinkle_people` borderline case).
>
> The bottleneck is the front-end pitch tracker on weak-melodic material,
> not the retrieval layer. Improving past this boundary would mean
> swapping the front-end tracker (e.g. CREPE, never benchmarked here) --
> explicitly out of scope for the current locked repo.

Mapping Steve's element (d) continuation items onto this
locked-record framing:

| Steve element-(d) item | Maps to locked-record formulation |
|---|---|
| Voice-friendly / polyphonic-capable extractor | "swapping the front-end tracker" — the bottleneck named in the locked-record paragraph; Steve's framing is broader than CREPE alone (encompasses any voice-friendly / polyphonic alternative). |
| Extension beyond canonical 6-case dataset | Pushes past the M4.1 corpus-scope boundary (risk register § 4.1); not directly addressed by the "Current boundary" paragraph but covered by the risk-register canonical-set risk. |
| Cross-corpus generalisation | The M6 family-retrieval extension implied by the M6.5 NEGATIVE result; risk register § 1.1. |
| Perceptual validation layer | Risk register § 3.1 (perceptual-validity risk REALISED × SIGNIFICANT); m3_1 closure recommendation Open Questions item 2 ("the strongest single thing that could either ratify or undermine the metric's broader meaning"). |

All four are *external to the current locked repo* and would be
new programmes, exactly matching the spec's framing of O042 as
*continuation work funded by validated existing evidence*.

## 5. Decision-policy restatement

Per `nmb3_decision_policy.md` and the O042 spec's "Allowed
autonomous actions": no funding claim, no funder-facing prose,
no ask quantification, and no continuation-scope commitment may
be issued by the autonomous loop without Steve's explicit
approval.  This entry is the Steve-approval artefact for the
*scope* of the funding package; any subsequent funder-facing
text (pitch deck, one-pager, narrative) remains its own
Steve-gated objective and is not authorised by O042 alone.

## 6. Risk assessment (of this gate close)

| Risk | Status | Notes |
|---|---|---|
| Steve string paraphrased rather than verbatim | None | The decisions.log block is delimited `BEGIN STEVE VERBATIM` / `END STEVE VERBATIM`; Steve's bullets / hyphens / parentheticals preserved.  The only character-level substitutions are the two `–` (en-dash) characters in Steve's "(b) €250k–€750k" and "(c) – Metric runs end-to-end" rendered as ASCII `-` to keep the log file ASCII-clean per the prior decisions.log convention; meaning is preserved. |
| Funder-facing prose drafted under this gate (forbidden) | None | No such prose authored. |
| Autonomous-loop suggestion of ask amount or scope (forbidden) | None | All quantification and scope items are Steve's. |
| Continuation work whose success criteria would soften M6.5 (forbidden) | None | All 4 continuation items push past M6.5 by changing the front-end; none re-litigates the M6.5 result inside the locked pipeline. |
| Treating any new algorithmic work as executed (forbidden) | None | No code written; no script edited; no algorithmic work claimed. |
| Workflow yml mutation | None | No CI workflow file edited or dispatched.  Workflow yml-edit budget consumed this loop: 0 of 2. |
| MILESTONES.md / nmb3_README.md / policy edit | None | None edited. |
| Cumulative-diff scope | Clean | Three files only this commit: `nmb3_decisions.log` (Steve string), this interpreter output (verification), `nmb3_objective_map.md` (status field). |

## 7. What this report does NOT claim

  - It does not advance any objective other than O042.
  - It does not authorise drafting of any funder-facing prose;
    that requires its own Steve gate.
  - It does not begin O043 (out-of-scope register); O043 is
    PROPOSED with auto-execute YES per its spec, but standing
    constraint "do not execute the whole preferred path yet" is
    in force; O043 awaits Steve's "Execute O043" string.
  - It does not commit to delivering any continuation milestone
    named in element (d); those are scope candidates for
    separately-funded follow-on programmes, not in-scope work
    for the current locked repo.
  - It does not retire the M6.5 boundary, the perceptual-
    validity gap, the canonical-corpus limitation, or any other
    open issue carried by `open_issues_final.md` (O040) or
    rated in `risk_register.md` (O041).

## 8. Recommended next move

Per the autonomous loop policy "Session Completion Rule" and
the standing constraint "do not execute the whole preferred
path yet", loop stops on objective success and proposes the
next objective without beginning it.

Natural next options after O042:

  - **O043 — Out-of-scope register (continuation-work framing).**
    Spec at `nmb3_objective_map.md`; Dependencies = O042 (now
    SUCCEEDED, dependency satisfied); auto-execute YES
    (documentation-only).  Would derive Part (i) (in
    continuation scope per Steve's element (d)) and Part (ii)
    (out-of-scope even for the continuation work) mechanically
    from the O042 string and the `MILESTONES.md` "Current
    boundary" paragraph, with no item silently dropped.
  - Authorise the upstream M6.1 / M6.2 / M6.3 formal
    re-validations (O030 / O031 / O032).
  - **Pause.**

Awaiting Steve.
