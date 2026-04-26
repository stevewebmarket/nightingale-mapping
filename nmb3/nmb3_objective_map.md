# NMB3 Objective Map — M3.1 Closure → M4 → M5 → M6 → Funding Package

**Document status: DRAFT, refinement r1 applied.**  Not yet
Steve-approved for execution.  Refinement r1 (this commit) reflects
Steve's roadmap-review reply:

- preferred execution path defined (see "Preferred execution path"
  section below; subset of the 44 objectives, not all of them);
- skipped objectives remain *available* and may be activated if an
  evidence gap appears during execution;
- the no-cache fresh-clone reproductions O012 / O023 / O039 share
  one parameterised workflow file (created by O012, dispatched by
  the others);
- O042 funding scope is now framed as **continuation work funded by
  validated existing evidence**, not packaging-only.  O043 and O044
  updated accordingly.

No objective in this file is authorised for execution until Steve
approves the roadmap (or individual objectives) explicitly.

**Document scope.**  This roadmap defines granular objectives for the
autonomous NMB3 loop to *re-validate the already-locked M3.1–M6.5
milestone chain under the binding Decision Policy and Autonomous Loop
Policy*, and to *assemble a funding-grade package* on top of that
evidence.  Per `MILESTONES.md`, the underlying algorithms are locked
("locked for evaluation / packaging"); this roadmap therefore covers
*re-validation, packaging, and funding artefacts*, not new
extraction / similarity / retrieval work.

**Related binding documents** (do not duplicate or override):
- `nmb3/nmb3_decision_policy.md`
- `nmb3/nmb3_autonomous_loop_policy.md`
- `nmb3/nmb3_manifesto.md`
- `MILESTONES.md`
- `nmb3/nmb3_blocks/block_template.md`
- `nmb3/nmb3_report_template.md`

**Honesty floor.**  Every objective must preserve the M6.5 boundary as
an honest FAIL.  Any objective whose success criterion would require
hiding, re-labelling, or softening that result is forbidden by
construction and is not in this roadmap.

---

## Schema (legend for every entry below)

Each objective uses these eleven fields:

- **Objective ID** — `O###` stable identifier.  Never reused.
- **Name** — short human-readable title.
- **Purpose** — one paragraph stating the question the objective
  answers and why that answer matters for the funding package.
- **Dependencies** — list of `O###` IDs that must be in `Status:
  CLOSED (Steve-approved)` before this objective may begin.
- **Success criteria** — pre-set, measurable, declared *before*
  execution per Decision Policy "pass condition declared before run".
- **Evidence required** — the concrete artefact(s) that must be
  produced and committed to canonical before the objective may close.
- **Allowed autonomous actions** — the bounded set of actions the
  Autonomous Loop may take inside this objective.
- **Forbidden actions** — explicit no-go list, in addition to the
  global Decision Policy "Forbidden Without Steve Approval" set.
- **Status** — one of: `PROPOSED`, `STEVE-APPROVED (NOT STARTED)`,
  `IN PROGRESS`, `BLOCKED`, `CLOSED (Steve-approved)`, `CLOSED
  (autonomously, validation block)`, `DEFERRED`, `OBSOLETE`.
- **Auto-execute permission** — `NO`, `YES (validation/stability
  only)`, or `YES (full)`.  Default `NO`.  Anything other than `NO`
  must cite which Decision Policy autonomous-approval criterion
  applies.
- **Rewrite permission** — who may edit the objective definition
  after Steve approves the roadmap.  Default: `Steve only`.  The
  autonomous loop may always update the `Status` field to reflect
  observed reality and may append evidence pointers; it may not edit
  any other field without Steve approval.

---

## Phase index

| Phase | Range          | Objectives  | Headline question |
|-------|----------------|-------------|-------------------|
| P0    | M3.1 closure   | O001–O004   | Close M3.1 cleanly under autonomous-loop discipline. |
| P1    | M3.2–M3.4      | O005–O009   | Re-validate the M3 sweep / sensitivity / focused-search results. |
| P2    | M4.1           | O010–O014   | Re-validate the 6-clip benchmark and lock the M4 baseline. |
| P3    | M5.1–M5.3      | O015–O019   | Re-validate per-onset diagnostics, onset-detector ablation, cqt_flux lock. |
| P4    | M5.4–M5.6      | O020–O024   | Re-validate pitch-window / adaptive-routing work and the M5.6 lock (107/144 = 0.7431). |
| P5    | M5.7–M5.9      | O025–O028   | Re-document the NEGATIVE pyin / HPSS results and the abandoned CREPE attempt. |
| P6    | M6.1–M6.4      | O029–O033   | Re-validate similarity, search, retrieval, family-retrieval (Twinkle PASS). |
| P7    | M6.5           | O034–O036   | Re-validate the multi-family Lamb FAIL **as an honest FAIL**.  Preserve the boundary. |
| P8    | Packaging      | O037–O041   | Reproducibility, methodology, and independent-reproduction artefacts. |
| P9    | Funding pkg    | O042–O044   | Funder-facing narrative, risk + out-of-scope registers, final ask. |

Total: 44 objectives.

---

## Preferred execution path (refinement r1)

Steve's preferred execution path covers a subset of the 44 objectives,
chosen so that the autonomous loop validates the *load-bearing*
evidence for the funding package without re-validating intermediate
milestones whose role is fully captured in `MILESTONES.md` and
already-closed canonical commits.

**On the preferred path (28 objectives):**

| Range       | Phase | Why it is on the path                                             |
|-------------|-------|-------------------------------------------------------------------|
| O001–O004   | P0    | Close M3.1 cleanly; archive the M3.1 evidence base.               |
| O020–O024   | P4    | Re-validate the locked **M5.6 = 107/144 = 0.7431** baseline (the headline number that anchors every later claim) and the M5.4 / M5.5 work that produced it. |
| O029–O036   | P6+P7 | Re-validate the M6.1 → M6.4 PASS chain *and* the M6.5 Lamb FAIL **as a FAIL** — the boundary is a load-bearing part of the result. |
| O037–O041   | P8    | Reproducibility, methodology, independent-reproduction protocol, open-issues register, risk register. |
| O042–O044   | P9    | Funding scope (continuation work, see refinement below), out-of-scope register, final funder-facing draft. |

**Off the preferred path but available (16 objectives):**

| Range       | Phase | Why it is off the preferred path                                  |
|-------------|-------|-------------------------------------------------------------------|
| O005–O009   | P1    | M3.2 / M3.3 / M3.4 are intermediate steps already locked; their evidence is fully captured in `MILESTONES.md` and the canonical commit chain. |
| O010–O014   | P2    | M4.1 baseline (93/135) is superseded by the locked M5.6 baseline (107/144) for funding-package purposes; re-validate only if O020–O024 surface a discrepancy that points back at M4.1. |
| O015–O019   | P3    | M5.1 / M5.2 / M5.3 are intermediate steps to the cqt_flux lock, which is itself a prerequisite of M5.6; re-validating M5.6 directly is sufficient unless an M5.6 reproduction discrepancy points back at one of them. |
| O025–O028   | P5    | M5.7 / M5.8 NEGATIVE results and M5.9 abandonment are honestly preserved in `MILESTONES.md`; the funding package can cite them by reference rather than re-running them. |

**Activation rule for off-path objectives.**  An off-path objective
moves onto the preferred path *only if* an on-path objective
produces evidence that points back at the off-path milestone — for
example, if O022 (M5.6 lock re-validation) fails to reproduce
107/144 to the note-flip, then O017 (M5.2 cqt_flux ablation) and
O018 (M5.3 lock) become on-path so the regression can be
localised.  Activation is recorded as a Steve-approved one-line
update to this section.  No off-path objective is deleted; all
remain available.

**On-path dependency rewiring.**  Where an on-path objective's
`Dependencies` field originally pointed at an off-path predecessor,
the dependency is rewired to the most recent on-path predecessor
with status `CLOSED (Steve-approved)`.  Concretely:

- O020's effective dependency is O004 (P0 archive), not O019 (P3
  closure).
- O029's effective dependency is O024 (P4 closure), not O028 (P5
  closure).

The original `Dependencies` text in those entries is preserved as
written; this section is the binding override for the preferred
path.

---

## P0 — M3.1 closure

### O001
- **Objective ID**: O001
- **Name**: M3.1 closure decision (Steve gate)
- **Purpose**: Convert the autonomous-loop's standing closure
  recommendation into an explicit Steve decision so every downstream
  objective has a defined entry condition.
- **Dependencies**: none
- **Success criteria**: Steve writes a single-line decision to
  `nmb3/nmb3_decisions.log` (or replies in chat which the manager then
  records there) selecting one of the four options listed in
  `nmb3/nmb3_reports/m3_1_closure_recommendation.md`.
- **Evidence required**: timestamped entry in
  `nmb3/nmb3_decisions.log` quoting Steve's exact wording.
- **Allowed autonomous actions**: append to `nmb3_decisions.log` in
  Steve's name only when Steve has supplied the wording; restate the
  four options if asked.
- **Forbidden actions**: choosing on Steve's behalf; closing M3.1
  without an explicit Steve string; editing the recommendation file.
- **Status**: CLOSED (Steve-approved) at 2026-04-25T16:34:20Z.
  Closure is on the "narrow reading" defined in
  `nmb3/nmb3_reports/m3_1_closure_recommendation.md`; explicitly
  does NOT authorise M4 work, any funding claim, the perceptual-
  validity claim, generalisation beyond the canonical 6-case
  sample set, generalisation to parameters other than onset_delta,
  or any policy-file edit.
- **Evidence to date**:
  - `nmb3/nmb3_reports/o001_report.md` — autonomous-portion
    execution and restated options (canonical commit 42a113b).
  - `nmb3/nmb3_decisions.log` — Steve's verbatim closure string
    (2026-04-25T16:34:20Z entry).
  - `nmb3/nmb3_reports/o001_closure_report.md` — session summary
    for the O001 closure step.
- **Auto-execute permission**: NO (Steve-only milestone decision per
  Decision Policy "Forbidden Without Steve Approval: change milestone").
- **Rewrite permission**: Steve only.

### O002
- **Objective ID**: O002
- **Name**: M3.1 per-case mid-range decomposition (optional)
- **Purpose**: Resolve the non-monotonic plateau in the
  onset_delta = 0.10 / 0.15 / 0.20 region by reporting per-case
  contributions, so Steve can decide whether the plateau is a real
  metric property or a sample-specific artefact.
- **Dependencies**: O001
- **Success criteria**: per-case (6 cases × 3 onset_delta values)
  within/total counts produced; deterministic across two runs;
  any case whose folded score moves by ≥ 1 note flip flagged.
- **Evidence required**: `nmb3/nmb3_reports/block_005_*` artefacts
  if Steve authorises the block.
- **Allowed autonomous actions**: write a Block 005 plan that varies
  only onset_delta in {0.10, 0.15, 0.20}; smoke-test; dispatch via the
  CI workflow rewire pattern already proven in Blocks 003 and 004.
- **Forbidden actions**: starting without Steve authorisation in
  O001's reply; varying any other parameter; declaring perceptual
  interpretation.
- **Status**: SUCCEEDED at 2026-04-25T16:52:53Z.  All three
  success criteria met (per-case 6×3 within/total counts produced;
  18/18 per-case bit-identical pairs across the two passes per
  delta; 4 of 6 cases flagged with within-span ≥ 1; 2 pitch_shift
  cases flat).  Aggregate scores at 0.10/0.15/0.20 reproduce the
  published Block 002/004 values exactly (no pipeline drift).
  Narrow factual conclusion (counts only, NOT perceptual): the
  mid-range plateau is driven by 4 of 6 cases shifting by exactly
  1 note across the region, with Orchestra and Rock cases moving
  in opposite directions; consistent with H1 (real metric
  property) and not H2 (sample-specific artefact).  Evidence:
  `nmb3/nmb3_blocks/block_005_plan.md`,
  `run_nmb3_block_005.py`,
  `nmb3/nmb3_logs/current_block_output.txt`,
  `nmb3/nmb3_reports/current_block_report.md`,
  `nmb3/nmb3_reports/block_005_interpreter_output.md`,
  CI run id 24935788699 (head d47b8b2, conclusion=success),
  bot commit cec5acd.  M3.1 closure is NOT re-opened.
- **Auto-execute permission**: NO (must be authorised inside Steve's
  O001 reply).
- **Rewrite permission**: Steve only.

### O003
- **Objective ID**: O003
- **Name**: M3.1 cross-corpus probe (optional)
- **Purpose**: Provide a one-block sanity check that the M3.1 metric
  behaves on at least one sample outside the canonical 6-case set,
  so the closure recommendation's "narrow reading" can be either
  ratified or constrained.
- **Dependencies**: O001
- **Success criteria**: at least one new clip evaluated end-to-end
  without runner exception; resulting score in [0, 1]; explicit honest
  label of any weak-evidence outcome (< 4 non-trivial intervals).
- **Evidence required**: Block 006 plan + interpreter output if Steve
  authorises.
- **Allowed autonomous actions**: locate one operator-supplied clip
  attached to an existing release; run with DEFAULT_CONFIG only.
- **Forbidden actions**: tuning to make the new clip pass; introducing
  new tuning parameters; altering the canonical 6-case set.
- **Status**: PROPOSED
- **Auto-execute permission**: NO.
- **Rewrite permission**: Steve only.

### O004
- **Objective ID**: O004
- **Name**: Lock M3.1 into the autonomous-loop archive
- **Purpose**: Once Steve closes M3.1 in O001, freeze the M3.1
  artefacts under a stable directory and update the manifesto's
  status table so all later phases reference a fixed M3.1 snapshot.
- **Dependencies**: O001 (and O002 / O003 if Steve authorised them)
- **Success criteria**: `nmb3/nmb3_archive/m3_1/` exists and
  contains copies of: blocks 001–004 plans, current_block_output.txt
  for each block, all interpreter outputs, the closure recommendation,
  and the Steve decision string from O001.
- **Evidence required**: directory commit; pointer added to
  `nmb3/nmb3_README.md`.
- **Allowed autonomous actions**: copy files; create the archive
  directory; append a single pointer paragraph to
  `nmb3/nmb3_README.md`; commit and push.
- **Forbidden actions**: editing any archived file post-copy;
  modifying any policy file; renaming the canonical M3.1 milestone.
- **Status**: SUCCEEDED at 2026-04-25T17:01:00Z.  Archive directory
  `nmb3/nmb3_archive/m3_1/` exists on canonical and contains:
  blocks 001–005 plans (block 005 included by the dependency-hint
  extension since O002 was Steve-authorised and SUCCEEDED);
  per-block runner outputs extracted from the bot commits that
  originally landed them (b056e9b/7929524, 5fb41bb, 488a889,
  c0a1b8c, cec5acd); per-block interpreter outputs (block_001
  static report + blocks 002–005 interpreter outputs); closure
  artefacts (closure recommendation, M3.1 session report, O001
  closure session report, Steve's verbatim O001 decision string
  extracted from the 2026-04-25T16:34:20Z entry of
  `nmb3/nmb3_decisions.log`); and `nmb3/nmb3_archive/m3_1/README.md`
  documenting source-of-truth pointers and the immutability rule.
  Pointer paragraph appended to `nmb3/nmb3_README.md`.  No
  archived file was edited post-copy.  No policy file was
  modified.  M3.1 milestone name was not renamed.
- **Auto-execute permission**: YES (validation/measurement-integrity
  block under Decision Policy autonomous-approval criterion 7;
  archival is a side effect with no scientific risk).
- **Rewrite permission**: Steve only.

---

## P1 — M3.2 / M3.3 / M3.4 re-validation

### O005
- **Objective ID**: O005
- **Name**: P1 entry approval (Steve gate)
- **Purpose**: Confirm Steve wants the autonomous loop to re-validate
  the M3.2–M3.4 work, or wants to skip ahead to M4 packaging.
- **Dependencies**: O001
- **Success criteria**: Steve string in `nmb3_decisions.log` of the
  form "Re-validate P1" / "Skip P1, proceed to P2" / "Skip all
  re-validation, proceed to packaging".
- **Evidence required**: log entry.
- **Allowed autonomous actions**: present the three options.
- **Forbidden actions**: choosing on Steve's behalf.
- **Status**: PROPOSED
- **Auto-execute permission**: NO.
- **Rewrite permission**: Steve only.

### O006
- **Objective ID**: O006
- **Name**: M3.2 re-validate hyperparameter sweep
- **Purpose**: Reproduce the M3.2 grid result (best config carried
  forward) on a clean CI runner and confirm the chosen DEFAULT_CONFIG
  is bit-identical to the locked one.
- **Dependencies**: O005 (= "Re-validate P1")
- **Success criteria**: every grid point reproduces to the note-flip;
  the chosen config matches `run_milestones.DEFAULT_CONFIG`;
  no parameter is silently different.
- **Evidence required**: Block 007 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch the M3.2 grid as a single
  block under the existing yml-rewire pattern.
- **Forbidden actions**: extending the grid; changing the metric;
  hiding any reproduction discrepancy.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O007
- **Objective ID**: O007
- **Name**: M3.3 re-validate sensitivity check
- **Purpose**: Re-run the M3.3 noise / clip-length perturbation set
  and confirm the score is not on a knife-edge.
- **Dependencies**: O006
- **Success criteria**: every perturbation reproduces; spread across
  perturbations matches the locked M3.3 spread to ≤ 1 note flip per
  perturbation.
- **Evidence required**: Block 008 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch the perturbation set;
  compute and report the spread.
- **Forbidden actions**: introducing new perturbations; changing the
  knife-edge threshold.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O008
- **Objective ID**: O008
- **Name**: M3.4 re-validate focused search
- **Purpose**: Reproduce the narrower search around the M3.2 winner
  and confirm M3.2 default is still the optimum at this scale.
- **Dependencies**: O007
- **Success criteria**: focused-search winner equals M3.2 winner;
  no improvement larger than 1 note flip discovered.
- **Evidence required**: Block 009 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch the focused search as
  defined in the locked M3.4 spec.
- **Forbidden actions**: re-tuning; relaxing the "no improvement
  larger than 1 note flip" condition.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O009
- **Objective ID**: O009
- **Name**: M3 phase closure recommendation
- **Purpose**: Aggregate O004 + O006 + O007 + O008 evidence into a
  single closure recommendation file for Steve.
- **Dependencies**: O008
- **Success criteria**: `nmb3/nmb3_reports/m3_phase_closure_recommendation.md`
  exists, lists evidence pointers, states a recommendation and limits.
- **Evidence required**: the recommendation file.
- **Allowed autonomous actions**: write the file; commit; push.
- **Forbidden actions**: declaring closure; changing milestone;
  editing MILESTONES.md.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P2 — M4.1 re-validation

### O010
- **Objective ID**: O010
- **Name**: M4 entry approval (Steve gate)
- **Purpose**: Explicit Steve approval to begin M4 re-validation
  work.  This satisfies the Decision Policy "M3.1 → M4 transition is
  Forbidden Without Steve Approval" clause for the *re-validation*
  sense (not a new-algorithm sense, which is out of scope for the
  locked repo).
- **Dependencies**: O009
- **Success criteria**: Steve string authorising M4 re-validation.
- **Evidence required**: `nmb3_decisions.log` entry.
- **Allowed autonomous actions**: present the request.
- **Forbidden actions**: starting M4 re-validation without the string.
- **Status**: PROPOSED
- **Auto-execute permission**: NO (Steve-only milestone gate).
- **Rewrite permission**: Steve only.

### O011
- **Objective ID**: O011
- **Name**: M4.1 re-validate the 6-clip benchmark
- **Purpose**: Reproduce the 93/135 baseline using the M3-default
  extractor on the canonical 6 clips × 3 transforms set, on a clean
  CI runner.
- **Dependencies**: O010
- **Success criteria**: total reproduces to 93/135 (= 0.6889) exactly;
  per-clip / per-transform breakdown reproduces to the note-flip.
- **Evidence required**: Block 010 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch the 6-clip benchmark with
  the M3 default extractor.
- **Forbidden actions**: substituting any later extractor (M5.3,
  M5.6) for the M3 default; modifying the clip set.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O012
- **Objective ID**: O012
- **Name**: Fresh-clone reproducibility check for M4.1 (off preferred path)
- **Purpose**: Independently confirm M4.1 reproducibility from a
  fresh clone of canonical (no caches, no prior CI artefacts).
- **Dependencies**: O011
- **Success criteria**: a fresh ubuntu-latest runner, given only
  `git clone` + the documented setup steps, produces bit-identical
  numbers to O011.
- **Evidence required**: a CI run launched from the shared no-cache
  reproducibility workflow with output pinned by SHA in the
  interpreter output.
- **Allowed autonomous actions**: as the first user of the shared
  no-cache workflow under refinement r1, *create* the parameterised
  reusable workflow file at
  `.github/workflows/nmb3_no_cache_repro.yml` (workflow_dispatch
  with `target` and `script` inputs; checkout with no caches; setup
  python; run the parameterised script; print the headline number;
  do NOT auto-commit any artefact); dispatch with `target=m4_1` and
  the M4.1 reproduction command; record the run id and SHA.  The
  same workflow file is reused without modification by O023 and
  O039.
- **Forbidden actions**: re-using cached samples; cherry-picking
  runs; baking M4.1-specific logic into the shared workflow (the
  M4.1-specific bits live in the `script` input, not in the yml).
- **Status**: PROPOSED (off preferred path; activate only if O022
  surfaces a regression that points back at M4.1).
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O013
- **Objective ID**: O013
- **Name**: M4.1 baseline lock confirmation
- **Purpose**: Record an explicit "baseline locked" entry stating
  93/135 = 0.6889 is the M4 baseline against which all M5 work is
  measured, with a pointer to the O011 + O012 evidence.
- **Dependencies**: O012
- **Success criteria**: `nmb3/nmb3_reports/m4_baseline_lock.md`
  exists with the headline, pointers, and explicit "no extractor
  changes proposed" note.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write the file; commit; push.
- **Forbidden actions**: claiming improvement; modifying
  `MILESTONES.md`.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O014
- **Objective ID**: O014
- **Name**: M4 phase closure recommendation
- **Purpose**: Aggregate P2 evidence into a single Steve-facing
  recommendation.
- **Dependencies**: O013
- **Success criteria**: `nmb3/nmb3_reports/m4_phase_closure_recommendation.md`
  exists.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: declaring closure; editing
  `MILESTONES.md`; making funding claims.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P3 — M5.1 / M5.2 / M5.3 re-validation

### O015
- **Objective ID**: O015
- **Name**: P3 entry approval (Steve gate)
- **Purpose**: Confirm Steve wants the M5 re-validation chain run.
- **Dependencies**: O014
- **Success criteria**: Steve string authorising P3.
- **Evidence required**: `nmb3_decisions.log` entry.
- **Allowed autonomous actions**: present the request.
- **Forbidden actions**: starting without the string.
- **Status**: PROPOSED
- **Auto-execute permission**: NO.
- **Rewrite permission**: Steve only.

### O016
- **Objective ID**: O016
- **Name**: M5.1 re-validate per-onset diagnostics
- **Purpose**: Reproduce the M5.1 per-onset classification (matches /
  octave_errors / other_errors / missing) on the canonical 6-clip
  set; confirm polyphonic still loses 3/8 onsets and highenergy still
  sits in the other_errors bottleneck under M3 defaults.
- **Dependencies**: O015
- **Success criteria**: per-clip per-onset classification reproduces
  bit-identically to the locked M5.1 numbers.
- **Evidence required**: Block 011 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch with the M3 default
  extractor and the M5.1 diagnostic hook.
- **Forbidden actions**: changing the diagnostic taxonomy; using a
  later extractor.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O017
- **Objective ID**: O017
- **Name**: M5.2 re-validate cqt_flux onset-detector ablation
- **Purpose**: Reproduce the 7-detector ablation result and confirm
  cqt_flux wins on polyphonic 5/8 → 8/8, flute 16/24 → 22/24, and
  total 93/135 → 100/144.
- **Dependencies**: O016
- **Success criteria**: full table reproduces; cqt_flux remains the
  winner; no other detector ties or beats it.
- **Evidence required**: Block 012 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch all 7 detectors.
- **Forbidden actions**: dropping detectors to make cqt_flux look
  cleaner; introducing new detectors.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O018
- **Objective ID**: O018
- **Name**: M5.3 re-validate cqt_flux lock and tracked regression
- **Purpose**: Confirm cqt_flux-as-default produces 100/144
  bit-identically and the rock_time_stretch 7/8 → 4/8 regression is
  still present and still tracked as an open issue.
- **Dependencies**: O017
- **Success criteria**: 100/144 reproduces; rock_tstretch = 4/8;
  open-issues file lists the regression.
- **Evidence required**: Block 013 plan + CI bot output + interpreter
  output; updated `nmb3/nmb3_reports/open_issues.md`.
- **Allowed autonomous actions**: dispatch the locked M5.3 config;
  append the open issue line if not already present.
- **Forbidden actions**: silently fixing the regression; removing it
  from the tracked-issues list.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O019
- **Objective ID**: O019
- **Name**: P3 closure recommendation
- **Purpose**: Aggregate O016–O018 into a single Steve-facing
  recommendation.
- **Dependencies**: O018
- **Success criteria**: `nmb3/nmb3_reports/m5_phase_p3_closure_recommendation.md`
  exists.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: declaring closure.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P4 — M5.4 / M5.5 / M5.6 re-validation

### O020
- **Objective ID**: O020
- **Name**: M5.4 re-document the pitch-window NEGATIVE result
- **Purpose**: Reproduce the M5.4 6-variant pitch-window ablation and
  confirm no variant passes all pre-set conditions, preserving the
  NEGATIVE label.
- **Dependencies**: O019
- **Success criteria**: 6-variant table reproduces; NEGATIVE
  classification preserved.
- **Evidence required**: Block 014 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch all 6 variants.
- **Forbidden actions**: relaxing the pre-set conditions to upgrade
  the result; dropping a variant.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O021
- **Objective ID**: O021
- **Name**: M5.5 re-validate adaptive-routing ablation
- **Purpose**: Reproduce the 4-signal routing ablation and confirm
  `adaptive_rms_attack` (threshold 1.5) passes all 7 pre-set
  conditions and produces the 107/144 number.
- **Dependencies**: O020
- **Success criteria**: full table reproduces; 7/7 conditions PASS;
  routing distribution ≈ 234 baseline / 54 short_med (within ±2
  routing decisions).
- **Evidence required**: Block 015 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch all 4 routing signals;
  report routing distribution explicitly.
- **Forbidden actions**: tuning the threshold off 1.5; dropping a
  signal.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O022
- **Objective ID**: O022
- **Name**: M5.6 re-validate adaptive-routing lock — **headline
  number 107/144 = 0.7431**
- **Purpose**: Reproduce the locked M5.6 baseline on a fresh runner
  and confirm `pitch_at()` dispatches on `pitch_mode` correctly.
- **Dependencies**: O021
- **Success criteria**: 107/144 reproduces bit-identically; both
  `baseline` and `short_med` modes remain selectable for comparisons.
- **Evidence required**: Block 016 plan + CI bot output + interpreter
  output; explicit "headline = 107/144 = 0.7431" line in the report.
- **Allowed autonomous actions**: dispatch the locked M5.6 config;
  exercise both pitch_modes.
- **Forbidden actions**: editing the dispatcher; renaming
  `pitch_mode` values; making any "we beat baseline" claim outside
  the locked 107/144 number.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O023
- **Objective ID**: O023
- **Name**: M5.6 fresh-clone reproducibility check (on preferred path)
- **Purpose**: Independent fresh-clone reproduction of **107/144 =
  0.7431**, the locked M5.6 baseline.  This is the headline-
  reproducibility evidence that anchors every later claim in the
  funding package.
- **Dependencies**: O022
- **Success criteria**: clean ubuntu-latest runner reproduces 107/144
  bit-identically with no caches; per-clip / per-transform breakdown
  reproduces to the note-flip; routing distribution reproduces to ±2
  routing decisions.
- **Evidence required**: dispatch of the shared no-cache workflow
  (created in O012 if O012 has been activated; otherwise created
  here, at the same path `.github/workflows/nmb3_no_cache_repro.yml`,
  with the same parameterised shape so O039 can reuse it) with
  `target=m5_6`; resulting CI run id pinned by SHA in the
  interpreter output.
- **Allowed autonomous actions**: dispatch the shared no-cache
  workflow with the M5.6 reproduction command; if the shared
  workflow file does not yet exist on canonical, create it per the
  spec in O012 (this objective and O012 are interchangeable as the
  workflow's creator; whichever runs first creates it, the other
  reuses it without modification); record run id and SHA.
- **Forbidden actions**: caching; cherry-picking runs; introducing
  M5.6-specific logic into the shared workflow yml.
- **Status**: SUCCEEDED at 2026-04-25T17:38:00Z.  All three success
  criteria met with zero drift.  Headline 107/144 = 0.7431
  reproduces bit-identically; per-clip / per-transform breakdown
  reproduces at all 18 of 18 (clip, test) cells (canonical
  `m4_1_results.json` from d332f54 vs Run A); routing distribution
  reproduces exactly at 234 baseline / 54 short_med (delta = 0,
  comfortably within ±2).  Two CI runs dispatched against
  `.github/workflows/nmb3_no_cache_repro.yml` (created in this
  same objective execution per the O023 / O012 interchangeability
  clause), both pinned to head SHA
  `1368524699287cc28ae416c7edda7f6c04b4c0e0`:
  Run A (24936558636, target=m5_6, headline reproduction) and
  Run B (24936650442, target=m5_6_routing, routing instrumentation
  via inline Python wrapper passed in the `script` input — no
  pipeline file modified, no M5.6-specific logic in the yml).
  Evidence: `nmb3/nmb3_reports/o023_m5_6_fresh_clone_reproduction.md`.
  Activation-rule check: no P2 / P3 activation triggered (no
  regression points back at M4.1 / M5.1 / M5.2 / M5.3); MILESTONES.md
  remains accurate; no errata commit required.
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O024
- **Objective ID**: O024
- **Name**: P4 closure recommendation
- **Purpose**: Aggregate O020–O023 into a single Steve-facing
  recommendation that the locked M5.6 baseline is reproduced.
- **Dependencies**: O023
- **Success criteria**: `nmb3/nmb3_reports/m5_phase_p4_closure_recommendation.md`
  exists, includes the headline 107/144 = 0.7431.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: claiming improvement on the M5.6 baseline.
- **Status**: SUCCEEDED at 2026-04-25T17:41:53Z, in the **partial-
  scope** variant explicitly authorised by Steve's
  "Execute O024 (partial-scope closure)" string (see
  `nmb3/nmb3_decisions.log`, 2026-04-25T17:41:53Z entry).  File
  `nmb3/nmb3_reports/m5_phase_p4_closure_recommendation.md` exists
  on canonical and contains the headline 107/144 = 0.7431
  (success criterion), the full O023 evidence base (run ids
  24936558636 / 24936650442, head SHA
  `1368524699287cc28ae416c7edda7f6c04b4c0e0`, per-cell breakdown,
  routing distribution), the activation-rule justification for
  partial scope (O020 / O021 / O022 deferred — not failed —
  because O023 succeeded with zero drift and no regression points
  back at M5.4 / M5.5 / M5.6-in-repo), and an explicit "what this
  does NOT recommend" section enumerating every forbidden and
  out-of-scope claim.  Recommendation was a draft on canonical
  until Steve issued his explicit approval string.  No improvement
  claim was made (forbidden actions clause respected).  Full-
  scope expansion to a v2 recommendation aggregating all four
  P4 objectives remains available if Steve later authorises and
  succeeds O020 / O021 / O022.

  **APPROVED by Steve at 2026-04-25T17:59:01Z** via chat string
  "Approve P4 partial-scope closure" (see `nmb3/nmb3_decisions.log`
  entry of the same timestamp, and § 8 of the recommendation
  file).  The five binding items in § 5 of the recommendation
  are now in force for funding-package purposes on the partial-
  scope basis defined in § 2 (107/144 = 0.7431 treated as
  independently reproducible; 234/54 routing treated as part of
  the locked baseline; future citations use run ids 24936558636 /
  24936650442 + head SHA `1368524699287cc28ae416c7edda7f6c04b4c0e0`;
  O020 / O021 / O022 deferred under the activation rule, not
  skipped or failed; shared no-cache workflow remains the
  target-agnostic canonical reproduction surface).
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P5 — M5.7 / M5.8 / M5.9 re-documentation

### O025
- **Objective ID**: O025
- **Name**: M5.7 re-document the pyin NEGATIVE result
- **Purpose**: Reproduce the YIN-vs-pyin ablation; confirm pyin's
  isolated polyphonic win and its rock/flute/highenergy regressions;
  re-state the NEGATIVE classification (3 of 7 pre-set conditions
  fail) without re-running CREPE (still not importable here).
- **Dependencies**: O024
- **Success criteria**: full pyin / yin table reproduces; NEGATIVE
  preserved.
- **Evidence required**: Block 017 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch yin and pyin only;
  document CREPE skip with the same wording as MILESTONES.md.
- **Forbidden actions**: claiming pyin "almost passes"; re-weighting
  conditions; re-attempting CREPE install in this objective (that's
  O027's scope).
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O026
- **Objective ID**: O026
- **Name**: M5.8 re-document the HPSS NEGATIVE result
- **Purpose**: Reproduce HPSS+yin and confirm zero measurable change
  on every clip relative to yin control; re-state NEGATIVE.
- **Dependencies**: O025
- **Success criteria**: per-clip table reproduces with HPSS=YIN to
  the note-flip on every clip; NEGATIVE preserved.
- **Evidence required**: Block 018 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch HPSS+yin and yin control.
- **Forbidden actions**: claiming HPSS "would help with more tuning";
  introducing new HPSS parameters.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O027
- **Objective ID**: O027
- **Name**: M5.9 document the abandoned CREPE attempt
- **Purpose**: Produce a stable record of why CREPE was abandoned
  mid-install (heavy `tensorflow-cpu` dependency, unclear upside
  given M5.7) and confirm the leftover `tensorflow-cpu` install is
  documented as "harmless leftover".
- **Dependencies**: O026
- **Success criteria**: `nmb3/nmb3_reports/m5_9_abandonment.md` exists
  and matches MILESTONES.md wording.
- **Evidence required**: that file; checksum match against
  MILESTONES.md M5.9 section.
- **Allowed autonomous actions**: write the file; quote MILESTONES.md
  verbatim.
- **Forbidden actions**: re-attempting CREPE install; arguing for or
  against future CREPE work in this file.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.

### O028
- **Objective ID**: O028
- **Name**: P5 closure recommendation
- **Purpose**: Aggregate O025–O027 evidence into a single Steve-
  facing recommendation that the M5.7 / M5.8 NEGATIVE results and
  the M5.9 abandonment are honestly preserved.
- **Dependencies**: O027
- **Success criteria**: `nmb3/nmb3_reports/m5_phase_p5_closure_recommendation.md`
  exists.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: softening any NEGATIVE label.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P6 — M6.1 / M6.2 / M6.3 / M6.4 re-validation

### O029
- **Objective ID**: O029
- **Name**: P6 entry approval (Steve gate)
- **Purpose**: Explicit approval to begin M6 re-validation.
- **Dependencies**: O028
- **Success criteria**: Steve string authorising P6.
- **Evidence required**: `nmb3_decisions.log` entry.
- **Allowed autonomous actions**: present the request.
- **Forbidden actions**: starting without the string.
- **Status**: PROPOSED
- **Auto-execute permission**: NO.
- **Rewrite permission**: Steve only.

### O030
- **Objective ID**: O030
- **Name**: M6.1 re-validate pairwise structural similarity
- **Purpose**: Reproduce the three locked pair scores (orchestra vs
  orchestra_pshift = 0.700, orchestra vs orchestra_tstretch = 0.700,
  orchestra vs rock = 0.164 with "insufficient melodic content"
  verdict); confirm the >= 4 non-trivial intervals honesty gate
  fires correctly on the rock comparison.
- **Dependencies**: O029
- **Success criteria**: all three scores reproduce to 3 decimal
  places; honesty-gate verdict reproduces verbatim.
- **Evidence required**: Block 019 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch `run_m6_1_similarity.py`
  on the locked M5.6 extractor.
- **Forbidden actions**: editing the similarity weights
  (0.45 / 0.25 / 0.30); editing the >= 4 non-trivial gate.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O031
- **Objective ID**: O031
- **Name**: M6.2 re-validate query-vs-library search
- **Purpose**: Reproduce the `twinkle_box` headline ranking
  (twinkle_box_tstretch 0.479 → twinkle_harmonica 0.284 →
  unrelated tied at 0.164) and confirm the per-query PASS/FAIL/N/A
  self-check fires correctly.
- **Dependencies**: O030
- **Success criteria**: full ranking reproduces to 3 decimal places;
  tied ranks visible; self-check matches locked output.
- **Evidence required**: Block 020 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch
  `run_m6_2_search.py` on the locked library.
- **Forbidden actions**: editing the verdict gate; reordering ties;
  removing operator-supplied clips.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O032
- **Objective ID**: O032
- **Name**: M6.3 re-validate small-library retrieval
- **Purpose**: Reproduce the 3/3-queries-PASS retrieval result on
  the 9-candidate library; confirm `twinkle_people`'s explicit
  `borderline` label is preserved (top-1 unrelated, but
  twinkle_box_tstretch reaches rank 3).
- **Dependencies**: O031
- **Success criteria**: 3/3 PASS reproduces; all 7 pre-set conditions
  reproduce; `twinkle_people` borderline label intact.
- **Evidence required**: Block 021 plan + CI bot output + interpreter
  output.
- **Allowed autonomous actions**: dispatch `run_m6_3_retrieval.py`.
- **Forbidden actions**: removing the borderline label; relaxing the
  dense-rank semantics.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O033
- **Objective ID**: O033
- **Name**: M6.4 re-validate Twinkle family-retrieval (PASS)
- **Purpose**: Reproduce the family-retrieval PASS for Twinkle:
  twinkle_box (3 in top 3, outranks YES), twinkle_harmonica (2 in
  top 3, outranks YES), twinkle_people (1 in top 3, outranks NO and
  flagged weak-evidence).
- **Dependencies**: O032 — **WAIVED** by Steve's
  "Override deps for O033 (single-objective waiver)" string at
  2026-04-25T18:00Z (recorded in `nmb3/nmb3_decisions.log`).
  The waiver authorises O033 to execute alone against the current
  canonical M5.6 extractor without first re-validating M6.1 / M6.2
  / M6.3 (O030 / O031 / O032).  The waiver does not weaken any
  forbidden-action clause; "removing the weak-evidence flag" and
  "relaxing cond4" remain binding (and were respected in the
  reproduction — see the SUCCEEDED entry below).
- **Success criteria**: full table reproduces; weak-evidence flag for
  `twinkle_people` reproduces; the cond4 honesty assertion fires.
- **Evidence required**: Block 022 plan + CI bot output + interpreter
  output; explicit pointer to the 5/5 pre-set conditions PASS.
- **Allowed autonomous actions**: dispatch
  `run_m6_4_family_retrieval.py`.
- **Forbidden actions**: removing the weak-evidence flag; relaxing
  cond4.
- **Status**: SUCCEEDED at 2026-04-25T18:21:00Z.  All success
  criteria met.  Full table reproduces line-by-line vs MILESTONES.md
  M6.4 baseline (twinkle_box top3=3 / top5=3 / outranks=YES;
  twinkle_harmonica top3=2 / top5=3 / outranks=YES; twinkle_people
  top3=1 / top5=1 / outranks=NO).  Weak-evidence flag fires on
  `twinkle_people` only (2 non-trivial intervals < MIN_NT=4) and
  not on `twinkle_box` / `twinkle_harmonica` (both nt=5).  Cond4
  honesty assertion (every nt<4 query marked weak AND twinkle_people
  still weak) fires PASS.  All 5 of the script's pre-set conditions
  PASS (with cond6 EXTERNAL satisfied by this CI evidence).  Final
  script line `M6.4 PASS` printed.  CI run id 24937477484 pinned to
  head SHA `3929fbcda21e79045075dcc9ca3802f7bb9d7bc0` (which
  contains the Block 022 plan and the target-agnostic ffmpeg
  install in the shared workflow yml; no pipeline file modified).
  First-attempt run 24937425251 at SHA 59fad71 failed for an
  infrastructure reason (missing ffmpeg → audioread NoBackendError
  on `twinkle_people.m4a`); failure recorded honestly in the
  interpreter output § 5 and in decisions.log per the Block 022
  no-cherry-picking clause.  Forbidden actions respected: weak-
  evidence flag preserved; cond4 not relaxed; no M6.4-specific
  logic in workflow yml.  Evidence:
  `nmb3/nmb3_reports/o033_m6_4_family_retrieval_revalidation.md`
  and `nmb3/nmb3_blocks/block_022_plan.md`.
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P7 — M6.5 multi-family validation (the boundary)

### O034
- **Objective ID**: O034
- **Name**: M6.5 re-validate the Lamb FAIL **as an honest FAIL**
- **Purpose**: Reproduce the M6.5 result on the 12-candidate library
  with the three Lamb clips, with **no per-family tuning, no scoring
  changes, no extractor edits**.  Preserve the FAIL label and the
  per-condition breakdown (4 of 7 conditions FAIL).
- **Dependencies**: O033 — SATISFIED at 2026-04-25T18:21:00Z
  (canonical SHA 9eaabac).  Clean dependency; no waiver required.
- **Success criteria**: 6-query headline table reproduces verbatim;
  per-condition results reproduce; FAIL label preserved; no
  condition silently re-weighted.
- **Evidence required**: Block 023 plan + CI bot output + interpreter
  output; explicit assertion in the interpreter output that no
  tuning, scoring change, or extractor edit was applied.
- **Allowed autonomous actions**: dispatch
  `run_m6_5_multi_family.py` on the locked library + Lamb clips.
- **Forbidden actions**: per-family tuning; scoring changes; extractor
  edits; downgrading the comparator from "outranks-all-other" to a
  weaker comparator; restating cond5 to look better.
- **Status**: SUCCEEDED at 2026-04-25T18:45:00Z.  All success
  criteria met.  18-cell headline table reproduces verbatim vs
  MILESTONES.md M6.5 baseline (twinkle_box F1 top3=2/top5=3/YES;
  twinkle_harmonica F1 top3=1/top5=2/NO; twinkle_people F1
  top3=1/top5=1/NO+weak; lamb_solo F2 top3=0/top5=1/NO+weak;
  lamb_group F2 top3=1/top5=2/NO; lamb_male F2 top3=0/top5=1/NO+weak).
  All 7 pre-set conditions reproduce with bit-identical PASS/FAIL
  labels (cond1 PASS; cond2 FAIL 1/3; cond3 FAIL 0/3; cond4 FAIL
  on `polyphonic` partial-melodic-match WARNING firing 3 times;
  cond5 FAIL with twinkle_box (3,3,True,False)→(2,3,True,False)
  and twinkle_harmonica (2,3,True,False)→(1,2,False,False); cond6
  PASS; cond7 EXTERNAL satisfied by this CI evidence).  Final
  script line `M6.5 FAIL` printed.  Honesty floor explicitly NOT
  triggered (verdict is FAIL not PASS, only 3 of 7 conditions
  PASS, both family-level booleans report FAIL).  Forbidden
  actions respected: no pipeline file modified; no per-family
  tuning; no scoring change; no extractor edit; comparator
  remained the strict "outranks-all-other"; cond5 not restated.
  CI run id 24937928571 pinned to head SHA 9eaabac.  First-
  attempt success — no infrastructure failure (ffmpeg already in
  shared workflow from O033's commit 3929fbc).  Evidence:
  `nmb3/nmb3_reports/o034_m6_5_lamb_fail_revalidation.md` and
  `nmb3/nmb3_blocks/block_023_plan.md`.
- **Auto-execute permission**: YES (validation/measurement-integrity)
  — *with explicit honesty floor*: the autonomous loop may execute
  this objective only because the FAIL is the locked, declared
  result; any reproduction that *passes* M6.5 must trigger the
  Decision Policy "suspected metric gaming" early-stop and be
  reported to Steve before any further action.
- **Rewrite permission**: Steve only.

### O035
- **Objective ID**: O035
- **Name**: Boundary documentation file
- **Purpose**: Produce a single boundary document that quotes
  MILESTONES.md "Current boundary" verbatim, points at O034
  evidence, and lists what is and is not within the locked
  pipeline's good case.
- **Dependencies**: O034 — SATISFIED at 2026-04-25T18:45:00Z
  (canonical SHA cf165f4 / 5190b05).  Clean dependency; no
  waiver required.
- **Success criteria**: `nmb3/nmb3_reports/boundary.md` exists;
  quoted MILESTONES.md section is checksum-equal to the canonical
  source.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: softening boundary language; suggesting
  out-of-scope fixes (CREPE, voice-friendly extractor) anywhere
  except the explicit "out of scope" register (O043).
- **Status**: SUCCEEDED at 2026-04-25T18:58:00Z.  All success
  criteria met.  `nmb3/nmb3_reports/boundary.md` created with
  the verbatim MILESTONES.md "Current boundary" passage (lines
  40-53 at canonical SHA cf165f4) embedded as a fenced quote
  with explicit SHA256 pinning
  (`a6fc0d62b760733e96eb40a798fd5c67374bb2689273fcdf42c68d92d21e0cfc`)
  and a verifier reproduction command
  (`sed -n '40,53p' MILESTONES.md | sha256sum`).  Document points
  at O033 (M6.4 PASS, run 24937477484 at SHA 3929fbc) for the
  good-case side and O034 (M6.5 FAIL, run 24937928571 at SHA
  9eaabac) for the boundary side, with interpreter output paths
  and artefact filenames inline.  No softening language
  introduced (M6.5 FAIL preserved as FAIL; not relabelled
  "partial pass" / "open issue" / "scheduled improvement").
  No new fix-recommendation language added outside the verbatim
  quote (the CREPE mention in § 1 appears only inside the byte-
  equal quote, as the success criterion requires; § 5 explicitly
  records that this is not a recommendation made by the
  document).  Non-claim register in § 5 explicitly points
  out-of-scope fix discussion to O043.  Pointer summary in
  § 6 cross-references all five evidence locations (canonical
  passage; M6.4 PASS interpreter + CI; M6.5 FAIL interpreter +
  CI).  Evidence: `nmb3/nmb3_reports/boundary.md` and
  `nmb3/nmb3_blocks/block_024_plan.md`.
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.

### O036
- **Objective ID**: O036
- **Name**: M6 phase closure recommendation (including the boundary)
- **Purpose**: Aggregate O030–O035 into a Steve-facing recommendation
  that explicitly includes the M6.5 boundary as part of the closed
  result, not as an open issue to be solved.
- **Dependencies**: O035 — SATISFIED at 2026-04-25T18:58:00Z
  (canonical SHA dd1b689).  Clean dependency against the literal
  Dependencies clause; no waiver required.  Note: O030 / O031 /
  O032 (M6.1 / M6.2 / M6.3 fresh CI re-validation) remain PROPOSED
  on canonical and are NOT formal dependencies of O036; the
  closure recommendation aggregates them on a partial-scope basis
  matching the O024 P4 partial-scope closure pattern, with their
  PROPOSED status explicitly recorded in the recommendation's
  scope section.
- **Success criteria**: `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`
  exists; explicitly states "M6.5 FAIL is part of the result, not a
  blocker for closure".
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: presenting M6.4 PASS without the M6.5
  boundary in the same paragraph.
- **Status**: **APPROVED by Steve at 2026-04-25T19:18:00Z** via
  chat string "Approve M6 partial-scope closure" (see
  `nmb3/nmb3_decisions.log` 2026-04-25T19:18:00Z entry and
  § 9 of `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`).
  Binding for funding-package purposes on the partial-scope
  basis defined in § 2 of the recommendation.  Initial
  SUCCEEDED at 2026-04-25T19:14:00Z; approval applied via
  post-approval errata at 2026-04-25T19:18:00Z (no change to
  the recommendation's substantive content -- the approval
  errata only updates the Status: header from "Awaiting Steve"
  to APPROVED, fills in § 9's previously-placeholder fields
  with the verbatim approval string + timestamp + binding
  effect, and updates this Status entry).  All success
  criteria met.  `nmb3/nmb3_reports/m6_phase_closure_recommendation.md`
  created.  The verbatim required phrase "M6.5 FAIL is part of
  the result, not a blocker for closure" appears load-bearing
  in § 1 (the Headline section, first sentence in bold) and
  again in § 5 recommendation item 2.  Boundary co-location
  discipline holds throughout: every paragraph mentioning M6.4
  PASS also references M6.5 FAIL or the boundary, verified
  programmatically at commit time (a paragraph-scan finds 14
  paragraphs containing "M6.4 PASS" and zero violations after
  errata).  The errata patch (single bullet in § 3.4) added
  the explicit M6.5 boundary cross-reference to the bullet
  describing M6.2 score reproduction inside the M6.4 PASS
  leaderboard, since that bullet had previously stood alone
  as a paragraph and would have technically violated the
  forbidden action even though it was incidental rather than
  load-bearing.  Asymmetric scope explicitly recorded in § 2:
  O033 / O034 / O035 SUCCEEDED with full CI pinning, O030 /
  O031 / O032 PROPOSED (M6.1 / M6.2 / M6.3 carry MILESTONES.md
  baseline + incidental score reproduction inside O033 / O034
  leaderboards, NOT fresh CI re-validation).  Per-objective
  evidence pinning present for each SUCCEEDED objective: O033
  (run 24937477484 at SHA 3929fbc; interpreter output
  o033_m6_4_family_retrieval_revalidation.md); O034 (run
  24937928571 at SHA 9eaabac; interpreter output
  o034_m6_5_lamb_fail_revalidation.md); O035 (canonical commit
  dd1b689; boundary.md with SHA256 a6fc0d62...d2b28 byte-equal
  to MILESTONES.md "Current boundary").  Non-claim register in
  § 7 routes all out-of-scope fix discussion to O043 and
  explicitly disclaims funding / commercial / perceptual /
  second-corpus / real-time claims.  Governance note in § 4
  records that O029 (P6 entry approval) is PROPOSED and the M6
  work proceeded on a per-objective Steve-string basis (more
  conservative than a single phase entry).  Approval status
  header is "Awaiting Steve" per the P4 closure pattern; § 9
  is the post-approval errata target awaiting an explicit
  Steve approval string in chat (suggested: "Approve M6
  partial-scope closure").  Architect-driven errata (second
  errata, after the loop's own commit-time errata) tightened
  § 5 item 2 to remove a list of negated softening terms
  ("open issue", "scheduled improvement", "next steps", "work
  in progress") that the block plan permitted only in § 7's
  non-claim register; the substantive binding meaning of § 5
  item 2 is preserved (M6.5 FAIL is what the locked pipeline
  demonstrably does on multi-family material; the closure
  approves it; M6.5 FAIL is an approved boundary result
  within closure scope and receives no reclassification).
  Two other occurrences of "open issue" remain in the
  document outside § 7 -- one in § 2 inside a verbatim
  double-quoted citation of O036's own Purpose clause from
  this objective map, one in § 6 inside a single-quoted
  risk-table label naming the risk being prevented -- both
  in legitimate citation/labeling contexts that the architect
  review did not flag and that retain accurate cross-reference
  to the objective spec and risk register.  Evidence:
  `nmb3/nmb3_reports/m6_phase_closure_recommendation.md` and
  `nmb3/nmb3_blocks/block_025_plan.md`.
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

---

## P8 — Packaging artefacts

### O037
- **Objective ID**: O037
- **Name**: Reproducibility appendix (partial-scope)
- **Purpose**: Produce a single appendix that, for the milestone
  results currently backed by SHA-pinned CI evidence on canonical
  (M5.6 from O023, M6.4 from O033, M6.5 from O034), gives a SHA, a
  CI run id, the exact command, the workflow file, the artefact
  name, and the headline number, in a form that lets a third party
  reproduce every cited claim in one read; and **explicitly lists**
  the 13 milestones that are not yet SHA-pinned (M3.1, M3.2, M3.3,
  M3.4, M4.1, M5.1, M5.2, M5.3, M5.4, M5.5, M6.1, M6.2, M6.3) as
  **gaps, not failures**, with each gap entry naming the script
  whose locked baseline lives in MILESTONES.md.
- **Dependencies**: O036 — APPROVED at 2026-04-25T19:18:00Z
  (canonical SHA ea935f4).  Clean dependency.
- **Success criteria**: `nmb3/nmb3_packaging/reproducibility_appendix.md`
  exists; section A (or equivalent) lists the three SHA-pinned
  reproductions (M5.6 / M6.4 / M6.5) with full pinning per the
  Purpose; section B (or equivalent) lists the 13 gap milestones
  with each gap labelled as "gap, not failure" and each pointing at
  the MILESTONES.md baseline; the appendix explicitly disclaims any
  full-chain reproducibility claim and any funding claim; the
  appendix does NOT introduce any un-pinned number into its
  SHA-pinned section.
- **Evidence required**: that file.
- **Allowed autonomous actions**: assemble from existing artefacts;
  write; commit; push.  No fresh CI runs.
- **Forbidden actions**: omitting any of the 13 gap milestones from
  the gap list; mis-labelling a gap as a failure or vice-versa;
  introducing any number into the SHA-pinned section that is not
  pinned to a CI run id + head SHA; running a broader CI-pinning
  campaign (specifically forbidden by Steve in the rewrite string);
  claiming full-chain reproducibility; editing any policy file;
  making any funding / commercial / perceptual claim.
- **Status**: SUCCEEDED at 2026-04-25T19:26:00Z.  All success
  criteria met under the partial-scope rewrite at
  2026-04-25T19:24:00Z.  `nmb3/nmb3_packaging/reproducibility_appendix.md`
  created; section A pins three reproductions (M5.6 Run A id
  24936558636 at SHA 1368524, M6.4 run id 24937477484 at SHA
  3929fbcda21e79045075dcc9ca3802f7bb9d7bc0, M6.5 run id 24937928571
  at SHA 9eaabacf5ae5640d329fa97ebe316486eaccd08f) with full
  pinning (head SHA, CI run id, exact command, workflow file,
  artefact name, headline number, interpreter output filename,
  closure recommendation cross-reference) and a verifier command
  per entry; section B lists all 13 gap milestones (M3.1, M3.2,
  M3.3, M3.4, M4.1, M5.1, M5.2, M5.3, M5.4, M5.5, M6.1, M6.2,
  M6.3) labelled "gap, not failure" with each pointing at
  MILESTONES.md and naming the script in repo, with explicit
  caveat for M5.3 (no separate script -- diagnostics derived
  via M5.1/M5.2 scripts) and incidental-observational-
  reproduction caveats for M6.1 / M6.2 / M6.3 (their scores
  reproduce inside the M6.4 / M6.5 leaderboards but the scripts
  themselves have not been dispatched as SHA-pinned CI runs);
  section C non-claim register disclaims full-chain
  reproducibility, funding, commercial, perceptual, second-
  corpus generalisation, real-time-deployment claims, and the
  Steve-forbidden broader CI-pinning campaign; section D
  preserves a future-expansion path if Steve later authorises
  a broader campaign.  Negative / FAIL / ABANDONED milestones
  (M5.7, M5.8, M5.9, M6.5) are explicitly distinguished from
  gaps so the gap list cannot mislead a reviewer.  No policy
  file edited; no MILESTONES.md edited; no nmb3_README.md
  edited; no other objective's status changed; no fresh CI
  runs dispatched.  Evidence:
  `nmb3/nmb3_packaging/reproducibility_appendix.md` and
  `nmb3/nmb3_blocks/block_026_plan.md`.
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.
- **Rewrite history**:
    - 2026-04-25T19:24:00Z — Rewrite by Steve.  Authorisation
      string: "Re-scope O037 to partial-scope.  Rewrite permission
      granted by Steve."  (See `nmb3/nmb3_decisions.log`,
      2026-04-25T19:24:00Z entry, for the verbatim full text and
      the loop's interpretation.)  This rewrite narrows the
      Purpose / Success criteria from the original "every M3.1
      through M6.5 milestone" scope to the partial-scope "currently
      SHA-pinned evidence (M5.6 / M6.4 / M6.5) plus an explicit
      gap list for the 13 non-SHA-pinned milestones".  Explicit
      Steve-imposed forbidden actions added: no broader CI-pinning
      campaign; no full-chain reproducibility claim; no policy
      change; no funding claim.  The original Evidence required
      field "cross-link from `nmb3/nmb3_README.md`" is superseded
      by this rewrite (Steve's rewrite did not carry it forward;
      adding a README cross-link would require a separate Steve
      authorisation since editing the README is a substantive
      change outside this rewrite's scope).

### O038
- **Objective ID**: O038
- **Name**: Methodology appendix
- **Purpose**: Produce a single appendix describing the autonomous
  loop discipline (block plan → smoke test → CI dispatch → bot
  commit → interpreter output → closure recommendation), the policy
  files that bind it, and the explicit honesty floors.
- **Dependencies**: O037 — SUCCEEDED at 2026-04-25T19:26:00Z under
  the partial-scope rewrite (canonical SHA be48a65); architect
  review PASS at 2026-04-25T19:30:00Z with no BLOCKING / HIGH
  findings; Steve's conditional permission from
  2026-04-25T19:24:00Z therefore active for O038.
- **Success criteria**: `nmb3/nmb3_packaging/methodology_appendix.md`
  exists; references the binding policy files; references the schema
  in this objective map.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: editing the policy files; restating policy
  rules in a way that conflicts with their canonical text.
- **Status**: SUCCEEDED at 2026-04-25T19:32:00Z.  All success
  criteria met.  `nmb3/nmb3_packaging/methodology_appendix.md`
  created with five sections: (§ 1) the loop discipline phases
  (block plan → smoke test → CI dispatch → bot commit →
  interpreter output → closure recommendation), each pointing at
  the binding policy file(s) and quoting `nmb3/nmb3_cycle.md`'s
  canonical 6-step cycle and supporting rules verbatim; (§ 2) the
  inventory of 13 binding policy / process files (`nmb3_manifesto`,
  `nmb3_decision_policy`, `nmb3_autonomous_loop_policy`,
  `nmb3_cycle`, `nmb3_roles`, the four agent role files, the
  Manager-on-Replit-with-OpenAI integration spec, the toolchain
  spec, the two template files, and the objective map itself);
  (§ 3) the explicit honesty floors quoting the Early Stop
  Conditions, Session Budget, and Forbidden Without Steve
  Approval lists from `nmb3/nmb3_autonomous_loop_policy.md`
  verbatim and anchoring the Measurement Integrity Rules from
  `nmb3/nmb3_decision_policy.md`, with the M6.5 metric-gaming
  floor anchored to the O034 / appendix-A.3 evidence; (§ 4) the
  canonical 11-field schema for `nmb3/nmb3_objective_map.md`
  entries (Objective ID, Name, Purpose, Dependencies, Success
  criteria, Evidence required, Allowed autonomous actions,
  Forbidden actions, Status, Auto-execute permission, Rewrite
  permission) plus the optional Rewrite history / Evidence to
  date extensions, with the O037 entry as the worked example;
  (§ 5) a non-claim register paralleling the reproducibility
  appendix's Section C (no funding / commercial / perceptual /
  generalisation / deployment claims; no policy edit; no
  closure re-litigation; no scope creep; explicit binding to
  Steve's session stop rule).  No policy file edited; no
  MILESTONES.md edited; no nmb3_README.md edited; no other
  objective's status changed; no fresh CI runs dispatched; no
  workflow yml change.  Evidence:
  `nmb3/nmb3_packaging/methodology_appendix.md` and
  `nmb3/nmb3_blocks/block_027_plan.md`.
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.

### O039
- **Objective ID**: O039
- **Name**: Independent reproduction protocol
- **Purpose**: Produce a one-page, copy-pasteable protocol that an
  external reviewer can run to independently reproduce the M5.6
  baseline (107/144) and at least one M6.4 PASS query, on a fresh
  ubuntu-latest CI runner with no caches.
- **Dependencies**: O038
- **Success criteria**: `nmb3/nmb3_packaging/independent_reproduction_protocol.md`
  exists; protocol fits on one page; an external reviewer following
  it bit-identically reproduces the headline numbers; the protocol
  explicitly references the shared no-cache workflow at
  `.github/workflows/nmb3_no_cache_repro.yml` so the reviewer can
  re-dispatch it directly.
- **Evidence required**: that file; one CI run launched against the
  protocol's exact commands using the shared no-cache workflow with
  `target=m6_4_repro_smoke` (or an equivalent input naming the
  M5.6 + one-M6.4-query scope), pinned by SHA.
- **Allowed autonomous actions**: write the protocol; dispatch the
  shared no-cache workflow once with the protocol's exact inputs to
  verify; record the run id.  Do NOT create a new workflow file —
  reuse the one created in O012 / O023.  If neither O012 nor O023
  has been activated, create the shared workflow here per the spec
  in O012.
- **Forbidden actions**: relaxing the "no caches" requirement;
  hiding any setup step in an unspoken assumption; introducing
  M6.4-specific logic into the shared workflow yml.
- **Status**: SUCCEEDED at 2026-04-26T01:50:00Z.  Protocol artefact
  at `nmb3/nmb3_packaging/independent_reproduction_protocol.md`
  (introduced at SHA `766cff6`).  Reference CI dispatch run id
  `24945531211` at head SHA `766cff6` reproduced all four headline
  lines.  See `nmb3/nmb3_reports/o039_independent_reproduction_protocol.md`.
- **Auto-execute permission**: YES (validation/measurement-integrity).
- **Rewrite permission**: Steve only.

### O040
- **Objective ID**: O040
- **Name**: Open-issues register (final)
- **Purpose**: Produce a single open-issues register listing every
  tracked-not-hidden item from MILESTONES.md "Open issues" plus any
  added during P1–P7, with a current status line for each.
- **Dependencies**: O039
- **Success criteria**: `nmb3/nmb3_packaging/open_issues_final.md`
  exists; every item from MILESTONES.md "Open issues" appears.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: dropping any tracked issue; reclassifying
  any open issue as resolved without explicit Steve approval.
- **Status**: SUCCEEDED at 2026-04-26T02:45:00Z.  Register artefact
  at `nmb3/nmb3_packaging/open_issues_final.md` (207 lines) lists
  all 4 `MILESTONES.md` "Open issues" items verbatim plus 6
  tracked-not-hidden items added during P0 – P8 (4 from M3.1
  closure, 1 reproducibility-gap, 1 ffmpeg drift); no item dropped,
  no item reclassified.  See
  `nmb3/nmb3_reports/o040_open_issues_register.md`.
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.

### O041
- **Objective ID**: O041
- **Name**: Risk register
- **Purpose**: Produce an explicit risk register covering: scientific
  risk (boundary at M6.5), reproducibility risk (CI infrastructure
  drift), perceptual-validity risk (metric responds to known
  parameters but not to perceptual judgements, untested), corpus
  risk (canonical 6-case set), and process risk (autonomous loop
  failure modes).
- **Dependencies**: O040
- **Success criteria**: `nmb3/nmb3_packaging/risk_register.md`
  exists; each risk has a likelihood, impact, and mitigation column.
- **Evidence required**: that file.
- **Allowed autonomous actions**: write; commit; push.
- **Forbidden actions**: omitting the perceptual-validity risk;
  understating the M6.5 boundary risk.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (documentation only).
- **Rewrite permission**: Steve only.

---

## P9 — Funding package

### O042
- **Objective ID**: O042
- **Name**: Funding package scope decision — **continuation work
  funded by validated existing evidence** (Steve gate)
- **Purpose**: Steve declares the funding ask, the audience, the
  permissible claims, **and the continuation-work scope** that the
  ask funds.  Per refinement r1, the package is framed as
  *continuation work funded by validated existing evidence*: the
  evidence base is the autonomously-revalidated locked chain
  (O004 + O024 + O036 outputs + the locked `MILESTONES.md` numbers
  for the off-path phases), and the ask funds work that pushes past
  the M6.5 boundary — explicitly named candidate scopes include
  CREPE pitch tracker integration, voice-friendly extractor work,
  and second-corpus generalisation.
- **Dependencies**: O041
- **Success criteria**: Steve string in `nmb3_decisions.log`
  specifying:
  (a) funder type / audience;
  (b) ask amount or range;
  (c) the locked claim set the package is allowed to assert about
      *existing* validated evidence;
  (d) the continuation-work scope the ask funds, named at the level
      of milestone candidates (e.g., "CREPE integration as the
      first continuation milestone, voice-friendly extractor as the
      second, second-corpus generalisation as the third");
  (e) explicit confirmation that the M6.5 boundary will be stated
      honestly in the funder-facing material as the *reason* for
      the continuation ask, not hidden by it.
- **Evidence required**: log entry containing all five elements
  (a)–(e).
- **Allowed autonomous actions**: present the five-element question
  to Steve; restate the Decision Policy "no funding claim without
  Steve approval" rule; quote the `MILESTONES.md` "Current
  boundary" section verbatim so the continuation-scope discussion
  is anchored in the locked record.
- **Forbidden actions**: drafting any funder-facing prose before
  the five-element string exists; suggesting an ask amount or a
  continuation scope on Steve's behalf; proposing continuation work
  whose success criteria would require softening the M6.5
  boundary; treating any new algorithmic work as *executed* under
  this objective (O042 only declares scope; new algorithmic work
  is itself out-of-scope for the locked repo and must be its own
  separately-funded follow-on programme).
- **Status**: PROPOSED
- **Auto-execute permission**: NO (Steve-only — funding decisions
  are explicitly reserved for Steve).
- **Rewrite permission**: Steve only.

### O043
- **Objective ID**: O043
- **Name**: Out-of-scope register (continuation-work framing)
- **Purpose**: Per refinement r1, O043 produces a two-part register:
  (i) what is *in continuation scope* per the O042 string (named
  candidate continuation milestones, e.g., CREPE, voice extractor,
  second-corpus generalisation), and (ii) what remains
  *out-of-scope even for the continuation work* (e.g., perceptual-
  validity studies if Steve excluded them in O042; cross-language
  vocal corpora; real-time deployment; commercial productisation).
  The funder must be able to read this file and know exactly which
  results the ask buys and which it does not.
- **Dependencies**: O042
- **Success criteria**:
  `nmb3/nmb3_packaging/scope_and_out_of_scope.md` exists; every
  continuation-scope item named in the O042 string appears in
  Part (i); every "What does not yet work" item from
  `MILESTONES.md` "Current boundary" appears in either Part (i) (if
  Steve put it in continuation scope) or Part (ii) (if not), with
  no item silently dropped.
- **Evidence required**: that file; explicit cross-reference to the
  O042 log entry's element (d).
- **Allowed autonomous actions**: write the file; commit; push;
  derive Part (i) and Part (ii) mechanically from the O042 string
  and `MILESTONES.md` "Current boundary".
- **Forbidden actions**: implying any in-continuation-scope item is
  already proven achievable; framing the M6.5 boundary as easily-
  fixable; adding a continuation-scope item that was not named in
  the O042 string; promising any specific continuation outcome.
- **Status**: PROPOSED
- **Auto-execute permission**: YES (documentation only, post-O042).
- **Rewrite permission**: Steve only.

### O044
- **Objective ID**: O044
- **Name**: Funder-facing package — final draft for Steve approval
  (continuation-work framing, per r1)
- **Purpose**: Produce the single funder-facing package
  (`nmb3/nmb3_packaging/funding_package.md`) that frames the ask as
  **continuation work funded by validated existing evidence**.  The
  package combines:
  (1) an executive summary stating the validated existing claims
      (only those permitted by the O042 string), the M6.5 boundary
      as the explicit *reason* for the continuation ask, and the
      continuation scope from O042 element (d);
  (2) a technical brief covering the locked pipeline through M5.6,
      the M6.1–M6.4 retrieval chain, and the M6.5 boundary;
  (3) headline numbers (M3.1 baseline, M5.6 = 107/144 = 0.7431,
      M6.4 PASS, M6.5 boundary FAIL);
  (4) pointers to every appendix (O037, O038, O039, O040, O041,
      O043);
  (5) a continuation-work plan referencing O043 Part (i),
      explicitly *not* claiming any continuation outcome is proven
      in advance.
- **Dependencies**: O043
- **Success criteria**: file exists; every claim in the executive
  summary maps to an appendix pointer; the M6.5 boundary appears
  in the executive summary, not only in the appendices; the
  continuation-work plan maps every named scope item to the O042
  string element (d) and to O043 Part (i); the package contains no
  claim outside the O042-permitted set; Steve has explicitly
  written "Funding package final draft approved" in
  `nmb3_decisions.log` before any external use.
- **Evidence required**: the package file, plus the Steve approval
  string.
- **Allowed autonomous actions**: assemble the file from
  Steve-approved artefacts only; submit for Steve review.
- **Forbidden actions**: external distribution before the Steve
  approval string exists; making any claim outside the
  O042-permitted set; presenting continuation-work scope as
  already-proven; omitting the M6.5 boundary from the executive
  summary; editing any policy file; editing `MILESTONES.md`.
- **Status**: PROPOSED
- **Auto-execute permission**: NO (Steve-only — funding-package
  release is explicitly reserved for Steve).
- **Rewrite permission**: Steve only.

---

## Roadmap-level forbidden actions (apply to every objective above)

- Editing `nmb3/nmb3_decision_policy.md` or
  `nmb3/nmb3_autonomous_loop_policy.md` for any reason.
- Editing `MILESTONES.md` (the locked record).
- Beginning any new algorithmic work (extractor, similarity,
  retrieval, pitch tracker) — the repo state is "locked for
  evaluation / packaging" per MILESTONES.md.
- Re-classifying any NEGATIVE / FAIL milestone as a PASS.
- Hiding or softening the M6.5 boundary in any objective, appendix,
  or funding artefact.
- Making any funder-facing claim before O042 is closed
  (Steve-approved).
- Treating the autonomous loop's own validation work as evidence
  for the underlying algorithms — the loop validates *that the
  locked numbers reproduce*, not *that the locked numbers are the
  best achievable*.

## Default open questions (for Steve's roadmap review) — RESOLVED in r1

All three questions answered by Steve's roadmap-review reply.
Resolutions retained here for the audit trail; the binding effects
are encoded in the "Preferred execution path" section, in the O012
/ O023 / O039 entries, and in the O042 / O043 / O044 entries.

1. **Are P1, P3, P5 re-validations actually wanted?**
   *Resolved:* not on the preferred execution path.  P1 (O005–O009),
   P2 (O010–O014), P3 (O015–O019), and P5 (O025–O028) are
   *available* and may be activated if an evidence gap appears
   during execution of the on-path objectives, per the activation
   rule in the "Preferred execution path" section.
2. **Should the no-cache fresh-clone reproductions (O012, O023,
   O039) all be the same workflow file or three separate
   workflows?**
   *Resolved:* one shared parameterised workflow file at
   `.github/workflows/nmb3_no_cache_repro.yml`, created by whichever
   of O012 / O023 / O039 is activated first (per the entry-level
   text added in r1) and reused without modification by the others.
3. **Does the funding ask in O042 include continuation work (CREPE,
   voice extractor) or is this strictly a packaging-of-existing-
   work funding ask?**
   *Resolved:* continuation work funded by validated existing
   evidence.  O042 success criteria now require Steve to name the
   continuation-work scope in element (d) of the funding-scope
   string; O043 produces a two-part register (in-continuation-scope
   vs. out-of-scope-even-for-continuation); O044 includes a
   continuation-work plan in the funder-facing draft.

## Maintenance

- Status field updates by the autonomous loop are the only edits
  the loop is permitted to make to this file without Steve
  approval.  Every other field requires Steve.
- Each closed objective must add a single pointer line below this
  section under a "Closed objectives" sub-heading, with a SHA and
  a one-line summary.  No closed objective is removed.
- Any new objective discovered to be necessary mid-execution is
  proposed by appending an `OPEN PROPOSAL` block at the bottom of
  this file; it is not assigned an O### ID until Steve approves
  it.

## Closed objectives (none yet — this is a draft)
