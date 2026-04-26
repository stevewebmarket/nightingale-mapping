# O044 — Funder-facing package final draft (interpreter output)

## 1.  Scope of this output

This is the Manager → Interpreter loop output for **O044
(Funder-facing package — final draft for Steve approval,
continuation-work framing per r1)**.  It accompanies the artefact
file `nmb3/nmb3_packaging/funding_package.md` produced this loop
and verifies, line by line against the O044 spec in
`nmb3/nmb3_objective_map.md`, that the artefact meets the
*autonomous* portion of the O044 success criteria.

The remaining (non-autonomous) portion of the O044 success criteria
is the verbatim Steve approval string `Funding package final draft
approved` in `nmb3_decisions.log`.  That string does **not** exist
as of this interpreter pass; this output therefore declares the
artefact as **DRAFT AWAITING STEVE APPROVAL**, not as `SUCCEEDED`.

## 2.  Inputs (Steve-approved artefacts only)

Per the O044 "Allowed autonomous actions" clause ("assemble the
file from Steve-approved artefacts only"), the package was assembled
from exactly these inputs, all of which are checked into `main`
prior to this loop:

| Input | Path | Steve-approval status |
|---|---|---|
| O042 funding-scope-decision string | `nmb3/nmb3_decisions.log` entry `2026-04-26T04:00:00Z`, between `BEGIN STEVE VERBATIM` / `END STEVE VERBATIM` delimiters | Steve verbatim, recorded |
| O043 scope-and-out-of-scope register | `nmb3/nmb3_packaging/scope_and_out_of_scope.md` (Part (i) used) | Architect APPROVED CLEAN at HEAD `2fb53c4` post-erratum; `SUCCEEDED` per `nmb3_decisions.log` entry `2026-04-26T05:10:00Z` |
| O037 reproducibility appendix | `nmb3/nmb3_packaging/reproducibility_appendix.md` | merged on `main`; pointer-only use in §4 |
| O038 methodology appendix | `nmb3/nmb3_packaging/methodology_appendix.md` | merged on `main`; pointer-only use in §4 |
| O039 independent reproduction protocol | `nmb3/nmb3_packaging/independent_reproduction_protocol.md` | merged on `main`; pointer-only use in §4 |
| O040 final open-issues register | `nmb3/nmb3_packaging/open_issues_final.md` | merged on `main`; pointer-only use in §4 |
| O041 risk register | `nmb3/nmb3_packaging/risk_register.md` | merged on `main`; pointer-only use in §4 |
| `MILESTONES.md` (locked) | `MILESTONES.md` | locked; baseline / headline / verdict numbers in §3 quoted verbatim |
| canonical CI workflow | `.github/workflows/nmb3_no_cache_repro.yml` (SHA `3929fbc`) | locked; not modified by O044 |

No external source was consulted; no funder-facing prose was
imported from outside the repository; no additional claim was
introduced.

## 3.  O044 success-criteria mapping

The O044 spec lists six success-criteria sub-clauses.  Each is
verified explicitly below.

### 3.1  "file exists"
PASS.  `nmb3/nmb3_packaging/funding_package.md` exists in the working
tree at this loop and is committed (see §6).

### 3.2  "every claim in the executive summary maps to an appendix pointer"
PASS.  Funding package §4 ("Appendix pointers") contains an explicit
per-claim mapping covering every numbered claim in §1.1
(claims 1 – 5) plus §1.2 (M6.5 boundary) and §1.3 / §5
(continuation scope).  Every §1 claim has at least one named
appendix file in §4.

| §1 claim | Appendix pointer (per funding-package §4) |
|---|---|
| §1.1 claim 1: Metric runs end-to-end | O037, O038, O039 |
| §1.1 claim 2: Reproduces exactly on clean CI | O037, O039; CI workflow SHA `3929fbc` |
| §1.1 claim 3: Responds to timing changes | O038 |
| §1.1 claim 4: Has a clear failure boundary (M6.5) | `MILESTONES.md` § M6.5; O040; O041 |
| §1.1 claim 5: M5.6 / M6.4 / M6.5 SHA-pinned & reproducible | O037, O039; M5.6 = commit `d332f54`; CI workflow SHA `3929fbc` |
| §1.2: M6.5 boundary as primary continuation motivation | O040, O041, O043 Part (i) |
| §1.3 / §5: continuation scope (4 element-(d) items) | O043 Part (i.1) – (i.4); O042 string |

### 3.3  "the M6.5 boundary appears in the executive summary, not only in the appendices"
PASS.  Funding package §1 contains §1.2 ("The M6.5 boundary (per
O042 element (e))"), which names M6.5 by milestone ID, by corpus
(Lamb), by verdict (`honest FAIL / boundary`, verbatim from
`MILESTONES.md`), and by its role as the **primary motivation** for
the continuation work.  M6.5 is also named in §1.1 claim 4
("Has a clear failure boundary (M6.5)", verbatim from O042 element
(c)) and in §1.4 ("the ask", as the reason for the ask).  It is
not only in the appendices.

### 3.4  "the continuation-work plan maps every named scope item to the O042 string element (d) and to O043 Part (i)"
PASS.  Funding package §5 contains four sub-sections (§5.1 – §5.4),
one per element-(d) item, in element-(d) order.  Each sub-section
quotes the element-(d) wording verbatim and names its O043 Part (i)
row by ID.  §5.5 contains a 4 × 3 cross-reference table making the
mapping mechanical.  Coverage = 4 of 4 element-(d) items.

| §5 row | element-(d) wording (verbatim) | O043 Part (i) row |
|---|---|---|
| §5.1 | "Voice-friendly / polyphonic-capable extractor" | (i.1) |
| §5.2 | "Extension beyond canonical 6-case dataset" | (i.2) |
| §5.3 | "Cross-corpus generalisation" | (i.3) |
| §5.4 | "Perceptual validation layer" | (i.4) |

### 3.5  "the package contains no claim outside the O042-permitted set"
PASS.  The O042-permitted set is the five locked claims in element
(c) of the O042 string.  Funding package §1.1 quotes those five
claims verbatim as the only claim envelope.  Funding package §6
("Non-claim register") restates this and lists the four explicit
non-claims that the package does not make.

Mechanical scan against the funder-facing prose for
strong-claim verbs (`proves`, `demonstrates`, `achieves`,
`succeeds`, `generalises`, `generalizes`, `outperforms`,
`state-of-the-art`, `breakthrough`, `novel`): **0 hits**.

Mechanical scan against the funder-facing prose for the
prohibited M6.5-softening lexical forms (`fix`, `resolve`,
`solve`, `easily-fixable`, `easily fixable`) per the
architect's forward note from the O043 erratum:
**0 hits**.  (Two non-softening occurrences of `easy` /
`non-trivial` exist: one as a verbatim technical term from
`MILESTONES.md` ("non-trivial intervals"), one inside the
non-claim register §6.2 in a *negation* ("the M6.5 boundary
does not have a known remediation path or is characterised
as easy to overcome").  Neither asserts the boundary is
easy to overcome; both are documented for traceability.)

### 3.6  "Steve has explicitly written 'Funding package final draft approved' in nmb3_decisions.log before any external use"
**NOT YET SATISFIED.**  This is the Steve-only portion of the
success criterion and is by design **not** an autonomous action.
Mechanical check on `nmb3/nmb3_decisions.log` at HEAD this loop:

```
$ grep -in "Funding package final draft approved" nmb3/nmb3_decisions.log
(no match)
```

Therefore:
- The package file `nmb3/nmb3_packaging/funding_package.md` is held
  inside the repository as DRAFT.
- No external use is authorised.
- Funding package §0 and §6.5 both restate this prohibition.
- Funding package §7 ("Provenance and versioning") makes the
  Steve-approval status explicit on the document itself.
- O044 is recorded in the objective map as **DRAFT AWAITING STEVE
  APPROVAL**, not `SUCCEEDED`, until that string exists.

## 4.  O044 forbidden-actions check

| Forbidden action (per O044 spec) | Status this loop |
|---|---|
| External distribution before the Steve approval string exists | NOT done.  Package is committed inside the repository as DRAFT; no external delivery channel was used; package §0, §6.5, and §7 all explicitly forbid external use until the Steve string exists. |
| Making any claim outside the O042-permitted set | NOT done.  Package §1.1 quotes the O042 element-(c) set verbatim and uses it as the only claim envelope.  §3.5 above documents the 0-hit strong-claim-verb scan. |
| Presenting continuation-work scope as already-proven | NOT done.  Each §5 sub-section labels the item `unstarted candidate` per O043 Part (i) and includes a "no specific outcome is promised" clause; §6.1 restates this as a non-claim. |
| Omitting the M6.5 boundary from the executive summary | NOT done.  §1.2 names M6.5 explicitly; §1.1 claim 4 names it; §1.4 names it as the reason for the ask. |
| Editing any policy file | NOT done.  No edit to `nmb3/nmb3_decision_policy.md` or `nmb3/nmb3_autonomous_loop_policy.md` this loop. |
| Editing `MILESTONES.md` | NOT done.  `MILESTONES.md` unchanged this loop; quoted only. |

**PASS.**  No forbidden action performed.

## 5.  Discipline check (loop bookkeeping)

- **Files added/edited this loop:**
  1. `nmb3/nmb3_packaging/funding_package.md` (NEW, ~348 lines).
  2. `nmb3/nmb3_reports/o044_funding_package.md` (NEW, this file).
  3. `nmb3/nmb3_objective_map.md` (status update only:
     `PROPOSED` → `DRAFT AWAITING STEVE APPROVAL`).
- **CI dispatches this loop:** 0.
- **Workflow yml edits this loop:** 0.  Workflow yml-edit budget
  consumed this loop: 0 of 2.
- **Script / pipeline / policy / `MILESTONES.md` / `nmb3_README.md`
  edits this loop:** 0.
- **External references introduced this loop:** 0.  All §4
  appendix pointers are repository-internal.

## 6.  Provenance

- This output is the Interpreter's verification of O044 against the
  O044 success criteria and forbidden-actions clauses in
  `nmb3/nmb3_objective_map.md`.
- The package file in §1 was committed in the same loop as this
  output; the SHA will be recorded in `nmb3_decisions.log` once
  the package + this output are committed together.
- Architect review will be requested immediately after commit, per
  loop policy.  On architect APPROVED CLEAN, the loop closes with
  status **DRAFT AWAITING STEVE APPROVAL** (not `SUCCEEDED`); the
  loop does not auto-promote to `SUCCEEDED` without the Steve
  verbatim string.
