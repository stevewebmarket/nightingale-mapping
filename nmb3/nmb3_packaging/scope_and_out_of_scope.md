# NMB3 Scope and Out-of-Scope (Continuation-Work Framing)

This register makes explicit, for any funder reading the
NMB3 funding package, exactly which results the ask buys
and which it does not.

It is derived mechanically from two fixed inputs:

  - **Steve's O042 funding scope declaration**, recorded
    verbatim in `nmb3/nmb3_decisions.log` at entry
    `2026-04-26T04:00:00Z` between `BEGIN STEVE VERBATIM` /
    `END STEVE VERBATIM` delimiters; element (d)
    enumerates the continuation-work scope.
  - **`MILESTONES.md` § "Current boundary"** (lines 40-53;
    canonical SHA recorded at `boundary.md` § 6), which
    enumerates "What works" and "What does not yet work".

Per O043's forbidden-actions register and the architect's
forward-looking guidance carried out of O042: in-scope items
in Part (i) are framed as *needed because of M6.5*, not as
*resolves M6.5*.  The M6.5 boundary is treated as the
motivating constraint and is **not** framed as
easily-fixable; no specific continuation outcome is promised;
no in-scope item is implied to be already proven achievable.

---

## Part (i) — In continuation scope (per O042 element (d))

The four candidate continuation milestones below are exactly
those named in Steve's O042 element (d), reproduced in
element-(d) order with Steve's verbatim wording.  Each is
treated as an unstarted candidate.  Success criteria for
each candidate are themselves Steve-gated and out of scope
for O043.

### (i.1)  Voice-friendly / polyphonic-capable extractor

  - **Verbatim from O042 element (d):** "Voice-friendly /
    polyphonic-capable extractor"
  - **Why needed (motivated by M6.5):** the locked M5.6
    pitch tracker fails the family-retrieval test on the
    M6.5 Lamb corpus precisely because it recovers fewer
    than ~4 non-trivial intervals on weak-melodic /
    voice-heavy material; this is the bottleneck named in
    `MILESTONES.md` § "Current boundary" ("The bottleneck
    is the front-end pitch tracker on weak-melodic
    material, not the retrieval layer").  The continuation
    work is needed *because of* M6.5; no part of this row
    characterises M6.5 as having a known remediation path
    or a guaranteed improvement path.
  - **Maps from `MILESTONES.md` "What does not yet work":**
    "voice-heavy / weak-melodic extraction" — covered here.
  - **Sub-scope candidates Steve's wording encompasses:**
    front-end-tracker swap (e.g., CREPE-class deep-learning
    pitch trackers, never benchmarked in the locked repo per
    the `MILESTONES.md` Current boundary paragraph);
    polyphonic-capable extraction; voice-friendly onset /
    timbre features.  Naming any of these as the *first*
    continuation milestone is itself a separate Steve gate.
  - **Status:** unstarted candidate; no claim of
    achievability is made by this register; M6.5 is not
    characterised here as having a known remediation path.

### (i.2)  Extension beyond canonical 6-case dataset

  - **Verbatim from O042 element (d):** "Extension beyond
    canonical 6-case dataset"
  - **Why needed (motivated by corpus risk + M6.5):** every
    M4 / M5 number is computed over the canonical 6-clip
    M4.1 benchmark; cross-corpus generalisation at the M3.1
    metric layer is untested (risk register § 4.1, REALISED
    × SIGNIFICANT; open-issues register § 2.4).  Extending
    the dataset is a pre-condition for any broader claim
    about the metric.
  - **Maps from `MILESTONES.md` "What does not yet work":**
    not directly enumerated in § "Current boundary" (which
    focuses on the front-end bottleneck), but the canonical
    6-case scope is the corpus axis of the same locked
    record.
  - **Status:** unstarted candidate.

### (i.3)  Cross-corpus generalisation

  - **Verbatim from O042 element (d):** "Cross-corpus
    generalisation"
  - **Why needed (motivated by M6.5):** M6.5 is the only
    second-corpus probe to date and returned NEGATIVE; the
    locked pipeline does not generalise to a second
    independently-recorded melodic family without per-family
    tuning (risk register § 1.1, REALISED × SIGNIFICANT).
    Continuation work is needed *because of* M6.5; M6.5 is
    not characterised here as having a known remediation
    path.
  - **Maps from `MILESTONES.md` "What does not yet work":**
    co-located with the front-end bottleneck (the "M6.5
    Lamb result" reference); the cross-corpus generalisation
    gap is the M6.5 boundary itself, framed at the dataset
    axis.
  - **Status:** unstarted candidate.

### (i.4)  Perceptual validation layer

  - **Verbatim from O042 element (d):** "Perceptual
    validation layer"
  - **Why needed (motivated by perceptual-validity risk):**
    the M3.1 metric correlates with known structural
    perturbations but its correspondence with human
    judgements of structural preservation is untested (risk
    register § 3.1, REALISED × SIGNIFICANT, quoting
    `m3_1_closure_recommendation.md` Open Questions item 2:
    "the strongest single thing that could either ratify or
    undermine the metric's broader meaning").  The
    perceptual-validity risk is distinct from the M6.5
    boundary; both are realised risks, and Steve's element
    (d) elects to fund work that addresses each.
  - **Maps from `MILESTONES.md` "What does not yet work":**
    not directly enumerated in § "Current boundary"; carried
    by risk register § 3.1, open-issues register § 2.2, the
    m3_1 closure recommendation, and `boundary.md` § 5.
  - **Status:** unstarted candidate.

---

## Part (ii) — Out-of-scope even for the continuation work

The items below are NOT named in Steve's O042 element (d),
NOT covered as sub-scope of any (i.x) item, and remain
out-of-scope even for the continuation programme that the
funding ask supports.  The funder must read this list as
binding: no part of the ask buys any of the items in Part
(ii).

### (ii.1)  Real-time / low-latency deployment

  - **Why out-of-scope:** Steve's element (d) specifies
    research-axis continuation work (extractor / corpus /
    perceptual layer); real-time deployment is a
    deployment-axis topic and is not named.
  - **Source:** `boundary.md` § 5 lists "real-time
    deployment" as out-of-scope for the locked repo; Steve
    did not include it in O042 element (d).

### (ii.2)  Commercial productisation / SaaS / mobile app

  - **Why out-of-scope:** Steve's O042 element (a) frames
    the audience as "Technical research funders / AI labs",
    not commercial investors; element (d) names no
    productisation work.  A separate commercial-funding
    objective with its own Steve gate would be required to
    bring any productisation work into scope.
  - **Source:** `boundary.md` § 5 lists "commercial
    productisation" as out-of-scope; Steve did not include
    it in O042 element (d).

### (ii.3)  Copyright / IP / forensic / royalty applications

  - **Why out-of-scope:** these are downstream applications
    of a similarity metric; none is named in O042 element
    (d).  The locked metric was developed for structural-
    similarity research, not for forensic or royalty
    determination.
  - **Source:** open-issues register § 2 carries no
    forensic/IP entry; Steve did not include it in O042
    element (d).

### (ii.4)  End-user UI / consumer product surfaces

  - **Why out-of-scope:** Steve's element (d) is purely
    research-axis; no UI / UX work is named.
  - **Source:** Steve did not include it in O042 element
    (d).

### (ii.5)  Streaming-deployment infrastructure

  - **Why out-of-scope:** infrastructure-axis, not
    research-axis; not named in O042 element (d).
  - **Source:** Steve did not include it in O042 element
    (d).

### (ii.6)  Softening or re-classifying the M6.5 boundary

  - **Why out-of-scope:** explicitly forbidden by O042
    element (e), which requires that the M6.5 failure
    boundary "will be stated explicitly and used as the
    primary motivation for the continuation work, not
    hidden or softened".  No part of the continuation work
    may re-frame M6.5 as resolved within the locked
    pipeline, as a "scheduled improvement", as a
    "partial pass", or as an "open issue".
  - **Source:** O042 element (e); risk register § 1.1
    (REALISED × SIGNIFICANT, mitigation row binding
    co-citation discipline); `m6_phase_closure_recommendation.md`
    item 2 ("M6.5 FAIL is part of the result, not a blocker
    for closure"); `boundary.md` § 5.

---

## Part (iii) — Mechanical-derivation audit

This section certifies that O043's spec-required mapping
holds with no silent drops.

### (iii.1)  Every O042 element-(d) item appears in Part (i)

| O042 element (d) item (verbatim) | Part (i) row |
|---|---|
| Voice-friendly / polyphonic-capable extractor | (i.1) |
| Extension beyond canonical 6-case dataset | (i.2) |
| Cross-corpus generalisation | (i.3) |
| Perceptual validation layer | (i.4) |

4 of 4 element-(d) items present in Part (i), in
element-(d) order, with Steve's verbatim wording in each
row's first bullet.

### (iii.2)  Every "What does not yet work" item appears in Part (i) or Part (ii)

`MILESTONES.md` § "Current boundary" "What does not yet
work" enumeration (lines 44-49 verbatim):

> * **What does not yet work:** **voice-heavy / weak-melodic extraction**
>   -- when the M5.6 pitch tracker recovers fewer than ~4 non-trivial
>   intervals from a clip, similarity scores collapse into the same band
>   as unrelated clips and family-level separation disappears (M6.5 Lamb
>   result, and the `twinkle_people` borderline case).

| "What does not yet work" item | Routed to |
|---|---|
| voice-heavy / weak-melodic extraction (M6.5 Lamb result + `twinkle_people` borderline) | Part (i) row (i.1) (covered by Steve's element-(d) item "Voice-friendly / polyphonic-capable extractor") |

1 of 1 "What does not yet work" item routed.  No silent
drop.

### (iii.3)  Cross-reference to O042 log entry's element (d)

  - **O042 log-entry pinning:** `nmb3/nmb3_decisions.log`,
    entry timestamped `2026-04-26T04:00:00Z`, between
    `BEGIN STEVE VERBATIM` / `END STEVE VERBATIM`
    delimiters.
  - **Element (d) verbatim block (Steve's wording):**

        (d) Continuation work:
        - Voice-friendly / polyphonic-capable extractor
        - Extension beyond canonical 6-case dataset
        - Cross-corpus generalisation
        - Perceptual validation layer

---

## Part (iv) — What this register does NOT do

  - It does NOT imply that any in-continuation-scope item
    is already proven achievable.  All four (i.x) items are
    unstarted candidates.
  - It does NOT frame the M6.5 boundary as easily-fixable.
    Each (i.x) item's "Why needed" framing treats M6.5 as
    the motivating constraint, not as a problem with a
    known solution.
  - It does NOT add any continuation-scope item that was
    not named in the O042 string.  Part (i) contains
    exactly the 4 items in element (d), in element-(d)
    order.
  - It does NOT promise any specific continuation outcome.
    Success criteria for each candidate milestone are
    themselves Steve-gated and out of scope here.
  - It does NOT draft any funder-facing prose.  This
    register is a structural / mapping document; any
    pitch-deck or one-pager language remains its own
    Steve-gated objective.
  - It does NOT advance any objective other than O043.
  - It does NOT retire or downgrade any open issue listed
    in `open_issues_final.md` (O040) or any risk rated in
    `risk_register.md` (O041).
  - It does NOT make any improvement, funding, commercial,
    or perceptual-validity claim.
