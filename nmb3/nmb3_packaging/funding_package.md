# Nightingale Mapping — Funder-facing package (O044 draft)

**Repository:** `stevewebmarket/nightingale-mapping`
**HEAD this draft is built against:** `4d6ebc1` (main).
**CI workflow this draft is built against:** `.github/workflows/nmb3_no_cache_repro.yml` at canonical SHA `3929fbc`.
**Audience (per O042 element (a), verbatim):**

> Technical research funders / AI labs (e.g. xAI, OpenAI-level research groups)

**Ask (per O042 element (b), verbatim):**

> €250k-€750k initial funding

**Status of this document:** DRAFT — not for external distribution
until Steve has explicitly written `Funding package final draft
approved` in `nmb3/nmb3_decisions.log`. No external use is authorised
before that string exists.

---

## 0.  How to read this document

This package frames the funding ask as **continuation work funded by
validated existing evidence**.  Every claim made in §1 (executive
summary) maps to an appendix pointer in §4; every continuation item
named in §5 maps back to the O042 funding-scope-decision string
(element (d)) and to the O043 scope-and-out-of-scope register
(Part (i)).

The set of claims permitted in this document is exactly the set
declared by Steve in the O042 string (element (c) "Locked claims").
That set is restated verbatim in §1 below and is the only claim
envelope used anywhere in this document.

The M6.5 failure boundary is named in the executive summary, not
hidden in the appendices.  Per the O042 string element (e), the M6.5
boundary is the **primary motivation** for the continuation work and
is not softened.

No continuation outcome is claimed as already-proven.  The
continuation work plan in §5 names the items from the O042 element
(d) list and refers each to the O043 scope register, which itself
labels every continuation candidate as `unstarted`.

---

## 1.  Executive summary

### 1.1  What has been validated (verbatim from O042 element (c))

The locked claims, exactly as written by Steve in the O042
funding-scope-decision string:

> - Metric runs end-to-end
> - Reproduces exactly on clean CI
> - Responds to timing changes (real signal)
> - Has a clear failure boundary (M6.5)
> - M5.6, M6.4, M6.5 results are reproducible and SHA-pinned

These five claims, and only these five claims, are used as the
"validated existing evidence" envelope for the ask.  See §4 for
appendix pointers proving each claim; see §6 for the explicit
non-claim register.

### 1.2  The M6.5 boundary (per O042 element (e))

The pipeline as locked at M5.6 / M6.4 has a clear, honestly-reported
failure boundary at M6.5 (multi-family validation, Lamb corpus): the
M6.4 family-retrieval result on the Twinkle corpus does not
generalise to a second, independently-recorded melodic family
without per-family tuning.  This is reported in `MILESTONES.md` as
"complete (**honest FAIL / boundary**)" and is the only place a
`FAIL` verdict is issued in the locked milestone tree.

The M6.5 boundary is the **primary motivation for the continuation
work** described in §5.  The boundary is not softened; the
continuation work is required *because of* the boundary, not as a
characterisation that the boundary has a known remediation path.

### 1.3  Continuation scope (verbatim from O042 element (d))

Steve's funding-scope-decision string defines the continuation work
as exactly four items, in this order:

> - Voice-friendly / polyphonic-capable extractor
> - Extension beyond canonical 6-case dataset
> - Cross-corpus generalisation
> - Perceptual validation layer

These four items, and only these four items, define the continuation
scope.  Each is expanded in §5 with a pointer to the corresponding
O043 Part (i) row.

### 1.4  The ask

The ask, per O042 element (b), verbatim:

> €250k-€750k initial funding

to begin the four continuation work items in §1.3 against the
validated baseline in §1.1, in order to address the M6.5 boundary
in §1.2.  No continuation outcome is claimed as already-proven.

---

## 2.  Technical brief

### 2.1  Pipeline shape (locked through M5.6, retrieval chain
M6.1 – M6.4, boundary M6.5)

```
audio in
  -> M3 onset / pitch extraction (1% tolerance, octave-folded,
                                  YIN front-end pitch tracker)
  -> M5 adaptive routing (M5.6: pitch_at() dispatches on
                          pitch_mode; baseline / short_med
                          remain selectable for comparisons)
  -> M6.1-M6.3 retrieval primitives (similarity, ranking,
                                     query-side comparator)
  -> M6.4 family-retrieval demo (Twinkle corpus)              => PASS
  -> M6.5 multi-family validation (Lamb corpus)               => FAIL
                                                                 (boundary)
```

The locked baseline at M5.6 is reported in `MILESTONES.md` at commit
`d332f54` as "Locked headline: 107/144 = 0.7431".  M5.6 is a pure
integration step: numbers reproduce byte-identically to M5.5, and
fresh-clone validation has been performed.

The M6.4 family-retrieval demo on the Twinkle corpus passes its
pre-set conditions; the M6.5 multi-family validation on the Lamb
corpus fails 4 of its 7 pre-set conditions.  Both M6.4 and M6.5
declared their pre-set conditions before the run; no tuning was
applied to make M6.5 pass.

### 2.2  Independent reproduction

The pipeline is run end-to-end on clean CI (no cache, no host
state) by `.github/workflows/nmb3_no_cache_repro.yml` at canonical
SHA `3929fbc`.  Every milestone row in §3 below is SHA-pinned to a
specific main-branch commit.  An independent reproduction protocol
is documented in O039 (see §4).

### 2.3  What this pipeline does *not* yet do

The pipeline as locked does not generalise to a second
independently-recorded melodic family without per-family tuning.
The honest read, recorded in `MILESTONES.md`, is that the M6.4
Twinkle result is closer to a special case than to a general
retrieval claim at the current pipeline maturity.  This is the M6.5
boundary; it is the **primary motivation** for the continuation
work in §5.

The pipeline also does not yet handle voice queries with the same
quality as instrumental queries (`twinkle_people` is a real pipeline
limit at the current pitch tracker), nor has it been demonstrated
on a corpus larger than the canonical 6-case set, nor against
a second independently-collected corpus, nor with a perceptual
validation layer on top of the metric.  These are exactly the four
continuation work items in §5.

---

## 3.  Headline numbers

| Milestone | Quantity | Verdict | Source (locked) |
|---|---|---|---|
| **M3.1 baseline** | 44 / 48 = 0.9167 | baseline established | `MILESTONES.md` § "M3.1 — Audio Transform Invariance Metric" |
| **M5.6 locked headline** | 107 / 144 = 0.7431 | LOCKED baseline | `MILESTONES.md` § "M5.6 — Lock adaptive routing (commit `d332f54`)"; "Locked headline: 107/144 = 0.7431." |
| **M6.4 family-retrieval demo (Twinkle)** | n/a (verdict-gated) | **PASS** | `MILESTONES.md` § "M6.4 — Family-retrieval demo"; pre-set pass conditions declared before the run |
| **M6.5 multi-family validation (Lamb)** | 4 of 7 pre-set conditions fail | **honest FAIL / boundary** | `MILESTONES.md` § "M6.5 — Multi-family retrieval validation"; "M6.5 result: FAIL (4 of 7 pre-set conditions fail)" |

All four rows are reproducible on clean CI by the canonical workflow
named in §2.2 and SHA-pinned to a specific main-branch commit
(M5.6 = `d332f54`).  Nothing in this table is outside the O042
element (c) claim envelope: each row is either a baseline number, a
locked headline, or a verdict on a pre-set condition set declared
before the run.

---

## 4.  Appendix pointers

Every claim made in §1 / §2 / §3 maps to one or more of the
following appendices, all of which are checked into the repository
on `main`:

| Origin objective | Appendix file | What it documents |
|---|---|---|
| **O037** | `nmb3/nmb3_packaging/reproducibility_appendix.md` | end-to-end reproducibility appendix; clean-CI invariants; SHA-pin discipline |
| **O038** | `nmb3/nmb3_packaging/methodology_appendix.md` | methodology appendix; metric definition; pre-set-condition discipline; pitch-tracker / similarity choices |
| **O039** | `nmb3/nmb3_packaging/independent_reproduction_protocol.md` | independent reproduction protocol; how an external party reproduces the M3 / M5 / M6 numbers without operator assistance |
| **O040** | `nmb3/nmb3_packaging/open_issues_final.md` | final open-issues register; known limits beyond the M6.5 boundary, tracked not hidden |
| **O041** | `nmb3/nmb3_packaging/risk_register.md` | risk register; M6.5 = REALISED × SIGNIFICANT; perceptual = REALISED × SIGNIFICANT; categorical mitigations |
| **O043** | `nmb3/nmb3_packaging/scope_and_out_of_scope.md` | scope-and-out-of-scope register; Part (i) continuation scope (4 items, in element-(d) order); Part (ii) explicit out-of-scope set; Part (iii) mechanical-derivation audit |

Every claim made in §1 traces back to one of these six appendices.
Specifically:

- §1.1 claim 1 (Metric runs end-to-end) → O037, O038, O039.
- §1.1 claim 2 (Reproduces exactly on clean CI) → O037, O039;
  enforced by `.github/workflows/nmb3_no_cache_repro.yml` (SHA
  `3929fbc`).
- §1.1 claim 3 (Responds to timing changes — real signal) →
  O038 (methodology, time-stretch / pitch-shift behaviour).
- §1.1 claim 4 (Has a clear failure boundary — M6.5) →
  `MILESTONES.md` § M6.5; O040; O041 (M6.5 = REALISED ×
  SIGNIFICANT row).
- §1.1 claim 5 (M5.6, M6.4, M6.5 results are reproducible and
  SHA-pinned) → O037, O039; M5.6 commit `d332f54`; CI workflow
  SHA `3929fbc`.
- §1.2 (M6.5 boundary as primary continuation motivation) →
  O040, O041, O043 Part (i) row headers.
- §1.3 / §5 (continuation scope from O042 element (d)) →
  O043 Part (i.1) – Part (i.4); O042 string in
  `nmb3/nmb3_decisions.log` entry `2026-04-26T04:00:00Z` between
  the `BEGIN STEVE VERBATIM` / `END STEVE VERBATIM` delimiters.

---

## 5.  Continuation work plan

The continuation work scope is **exactly** the four items named in
the O042 string element (d).  No additional item is added.  Each
item is expanded with a pointer to its corresponding O043 Part (i)
row, which itself labels the item as `unstarted candidate` and
states explicitly that no claim of achievability is made.

### 5.1  Voice-friendly / polyphonic-capable extractor
- O042 element (d) wording (verbatim): "Voice-friendly /
  polyphonic-capable extractor".
- O043 cross-reference: `nmb3/nmb3_packaging/scope_and_out_of_scope.md`
  § (i.1).
- Why this is the headline continuation item: the M6.5 boundary
  reflects that on weak-melodic material the locked YIN-based
  front-end pitch tracker recovers too few non-trivial intervals
  (2 – 3 per clip on the Lamb recordings) for the locked
  similarity layer to maintain family-level separation.  The same
  upstream constraint also caps `polyphonic` (5 / 24 in the M5.6
  baseline, believed pitch-tracker-limited) and gates
  voice-query family retrieval (`twinkle_people` as documented in
  `MILESTONES.md` "Open issues").  Continuation work on a
  voice-friendly / polyphonic-capable extractor is needed
  *because of* the M6.5 boundary; no part of this plan
  characterises M6.5 as having a known remediation path.
- Status: `unstarted candidate` (per O043 (i.1)).
- No specific outcome is promised; success criteria for this
  candidate are themselves Steve-gated (per O043 (i.1)
  sub-scope bullet).

### 5.2  Extension beyond canonical 6-case dataset
- O042 element (d) wording (verbatim): "Extension beyond canonical
  6-case dataset".
- O043 cross-reference: `nmb3/nmb3_packaging/scope_and_out_of_scope.md`
  § (i.2).
- Why this is in scope: the locked headline 107 / 144 = 0.7431 is
  measured on the canonical 6-case dataset.  Extending beyond
  that dataset is necessary to support the cross-corpus
  generalisation item in §5.3 and is named in the O042 string;
  it is not a re-baselining of the locked M5.6 number, which
  remains LOCKED.
- Status: `unstarted candidate` (per O043 (i.2)).
- No specific outcome is promised.

### 5.3  Cross-corpus generalisation
- O042 element (d) wording (verbatim): "Cross-corpus
  generalisation".
- O043 cross-reference: `nmb3/nmb3_packaging/scope_and_out_of_scope.md`
  § (i.3).
- Why this is in scope: the M6.5 result establishes that
  family-level retrieval on a single in-house Twinkle corpus does
  not extend to a second independently-recorded melodic family
  without per-family tuning.  Continuation work on cross-corpus
  generalisation is needed *because of* the M6.5 boundary; no
  part of this plan characterises M6.5 as having a known
  remediation path.
- Status: `unstarted candidate` (per O043 (i.3)).
- No specific outcome is promised.

### 5.4  Perceptual validation layer
- O042 element (d) wording (verbatim): "Perceptual validation
  layer".
- O043 cross-reference: `nmb3/nmb3_packaging/scope_and_out_of_scope.md`
  § (i.4).
- Why this is in scope: the M3 / M5 / M6 metric is a
  notes-within-tolerance retrieval-style metric.  A perceptual
  validation layer (human-in-the-loop or psychoacoustic-model
  agreement) is named in the O042 string as a continuation work
  item in its own right; it is also the only continuation item
  that does not depend on the upstream pitch tracker, and so is
  partially de-risked relative to §5.1 / §5.3.
- Status: `unstarted candidate` (per O043 (i.4)).
- No specific outcome is promised.

### 5.5  Mapping back to the O042 string

| §5 item | O042 element (d) wording (verbatim) | O043 cross-reference |
|---|---|---|
| §5.1 Voice-friendly / polyphonic-capable extractor | "Voice-friendly / polyphonic-capable extractor" | (i.1) |
| §5.2 Extension beyond canonical 6-case dataset | "Extension beyond canonical 6-case dataset" | (i.2) |
| §5.3 Cross-corpus generalisation | "Cross-corpus generalisation" | (i.3) |
| §5.4 Perceptual validation layer | "Perceptual validation layer" | (i.4) |

Coverage: 4 of 4 element-(d) items; each row points to its O043
Part (i) row; no item is added beyond the four.

---

## 6.  Non-claim register (this document)

This document explicitly does **not** claim:

1. that any continuation work item in §5 has been started or has a
   guaranteed outcome.  Each item is labelled `unstarted candidate`
   in O043 Part (i) and is so labelled here.
2. that the M6.5 boundary has a known remediation path or is
   characterised as easy to overcome.  M6.5 is reported as
   "**honest FAIL / boundary**" in `MILESTONES.md` and is the
   primary motivation for the continuation work in §5; it is not
   softened.
3. any claim outside the O042 element (c) "Locked claims" set
   restated verbatim in §1.1.  No additional retrieval claim, no
   additional generalisation claim, no additional perceptual claim
   is made anywhere in this document.
4. that the continuation work scope in §5 contains any item not
   in the O042 element (d) list.  §5 contains exactly the four
   element-(d) items, in element-(d) order.
5. that this document has been authorised for external use.  This
   document is a DRAFT until Steve has explicitly written
   `Funding package final draft approved` in
   `nmb3/nmb3_decisions.log`; no external use is authorised before
   that string exists.

---

## 7.  Provenance and versioning

- **This package draft built against repository HEAD:** `4d6ebc1` on
  `main` (post-O043 close-out bookkeeping commit).
- **Source artefacts (all on `main`):** the six appendix files in §4;
  `MILESTONES.md` (locked); `nmb3/nmb3_decisions.log` entry
  `2026-04-26T04:00:00Z` (O042 Steve verbatim block).
- **Canonical clean-CI workflow:** `.github/workflows/nmb3_no_cache_repro.yml`
  at SHA `3929fbc`; not modified by O044.
- **No policy file edited by O044.** No edit to
  `nmb3/nmb3_decision_policy.md`,
  `nmb3/nmb3_autonomous_loop_policy.md`, `MILESTONES.md`, or
  `nmb3_README.md`.
- **No CI dispatch fired by O044.** O044 is a packaging objective
  and has no CI side effects.
- **Steve approval still required.** The success criterion for O044
  requires Steve to have explicitly written `Funding package final
  draft approved` in `nmb3/nmb3_decisions.log` before any external
  use of this document.  As of HEAD `4d6ebc1`, that string does not
  yet exist; this document is therefore a DRAFT and is held inside
  the repository awaiting Steve's verbatim approval.
