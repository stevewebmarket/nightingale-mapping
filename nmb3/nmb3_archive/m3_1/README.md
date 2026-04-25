# NMB3 Archive — M3.1 Frozen Snapshot

Created:   2026-04-25T16:59:31Z (NMB3 objective O004 execution).
Audience:  Steve; future agents.
Status:    **Frozen snapshot.**  Contents must not be edited
           post-copy.  See "Immutability Rule" below.

---

## Why this directory exists

NMB3 objective O004 ("Lock M3.1 into the autonomous-loop archive")
freezes the M3.1 invariance metric work into a stable directory so
all later phases (P1 onward) reference a fixed M3.1 snapshot, even
if the live `nmb3/` tree is later reorganised, refactored, or
re-numbered.

M3.1 is **CLOSED (Steve-approved)** at 2026-04-25T16:34:20Z on
the narrow reading defined in
`closure/m3_1_closure_recommendation.md`.  The per-case follow-on
work commissioned by Steve in the same closure reply (NMB3
objective O002) **SUCCEEDED** at 2026-04-25T16:52:53Z; its
results are included in this archive so the snapshot captures the
M3.1 closure *and* its named follow-on in one place rather than
two.

## Immutability Rule

Per the O004 forbidden-actions clause in
`nmb3/nmb3_objective_map.md`:

> "editing any archived file post-copy"

Every file under `nmb3/nmb3_archive/m3_1/` is a frozen copy of
its source-of-truth at the moment of archival.  Subsequent agents
must **not** edit these files.  If a corresponding live file in
`nmb3/` is later changed, the live file diverges from the archived
copy and the archived copy remains the canonical M3.1 record.
Re-archival under a new directory (e.g. `m3_1_v2/`) is the only
permitted way to refresh the snapshot, and requires Steve
authorisation.

## Source-of-truth pointers (at the moment of archival)

Each file in this directory was copied or extracted from the
following canonical source at canonical commit b42ee30 (HEAD when
the archive was built; later commits do not affect the archived
copies):

### `blocks/`

Block plans — copied from `nmb3/nmb3_blocks/`:

  - block_001_plan.md
  - block_002_plan.md
  - block_003_plan.md
  - block_004_plan.md
  - block_005_plan.md  (O002 follow-on, included by dependency
    hint in O004's spec since Steve authorised O002)

### `runner_outputs/`

Per-block raw runner outputs.  Because the live workflow
overwrites `nmb3/nmb3_logs/current_block_output.txt` on each
block, the historical outputs are extracted from the bot commits
that originally landed them:

  - block_001_raw_output.txt — copied from
    `nmb3/nmb3_logs/block_001_raw_output.txt` (commit 7929524,
    pre-bot manual landing).
  - block_002_output.txt — extracted from commit 5fb41bb's
    `nmb3/nmb3_logs/current_block_output.txt`.  (Two block_002
    bot commits exist: 830b63a and 5fb41bb; the more recent of
    the two — 5fb41bb — is archived.  Block 003's interpreter
    output documents that block 002 was deterministic, so the
    two outputs are functionally equivalent.)
  - block_003_output.txt — extracted from commit 488a889.
  - block_004_output.txt — extracted from commit c0a1b8c.
  - block_005_output.txt — extracted from commit cec5acd.

### `interpreter_outputs/`

Per-block Interpreter Agent outputs — copied from
`nmb3/nmb3_reports/`:

  - block_001_report.md  (block_001 used a static report file;
    the per-block "interpreter output" pattern began at block_002)
  - block_002_interpreter_output.md
  - block_003_interpreter_output.md
  - block_004_interpreter_output.md
  - block_005_interpreter_output.md

### `closure/`

The Steve-decision and recommendation artefacts that closed M3.1:

  - m3_1_closure_recommendation.md — copied from
    `nmb3/nmb3_reports/m3_1_closure_recommendation.md`.  The
    canonical recommendation Steve replied to.  Defines the
    "narrow reading" that became the binding closure.
  - m3_1_autonomous_session_report.md — copied from
    `nmb3/nmb3_reports/m3_1_autonomous_session_report.md`.  The
    session summary covering the autonomous run that produced
    Blocks 003 + 004 and the closure recommendation.
  - o001_closure_report.md — copied from
    `nmb3/nmb3_reports/o001_closure_report.md`.  The session
    summary for the O001 closure step itself (the moment the
    Steve gate flipped from PROPOSED to CLOSED).
  - steve_o001_closure_decision.txt — extracted verbatim from
    `nmb3/nmb3_decisions.log`, the 2026-04-25T16:34:20Z entry.
    The single load-bearing Steve decision string that closed
    M3.1 on the narrow reading and authorised O002.  This is the
    file the O004 success criteria identifies as "the Steve
    decision string from O001".

## What the archive does and does NOT authorise

This archive is a **record**, not a claim.  It does not, by its
existence, authorise any of the following (each of which would
require a separate Steve gate):

  - Re-opening M3.1 closure on a wider reading.
  - Recommending or beginning M4 work.
  - Generalising the M3.1 metric beyond the canonical 6-case
    sample set.
  - Generalising the Block 005 Orchestra-down / Rock-up genre
    asymmetry beyond the canonical 6-case set or beyond the
    0.10–0.20 onset_delta range.
  - Claiming perceptual validity of the M3.1 metric.
  - Making any funding claim on the strength of these artefacts.
  - Editing any policy file (`nmb3_decision_policy.md`,
    `nmb3_autonomous_loop_policy.md`) or `MILESTONES.md`.

## Provenance summary

| What | Source | Frozen at |
|---|---|---|
| Block plans | `nmb3/nmb3_blocks/block_NNN_plan.md` | b42ee30 |
| block_001 runner output | `nmb3/nmb3_logs/block_001_raw_output.txt` | b42ee30 |
| block_002 runner output | bot commit 5fb41bb | b42ee30 |
| block_003 runner output | bot commit 488a889 | b42ee30 |
| block_004 runner output | bot commit c0a1b8c | b42ee30 |
| block_005 runner output | bot commit cec5acd | b42ee30 |
| Interpreter outputs | `nmb3/nmb3_reports/block_NNN_*` | b42ee30 |
| Closure recommendation | `nmb3/nmb3_reports/m3_1_closure_recommendation.md` | b42ee30 |
| M3.1 session report | `nmb3/nmb3_reports/m3_1_autonomous_session_report.md` | b42ee30 |
| O001 closure session report | `nmb3/nmb3_reports/o001_closure_report.md` | b42ee30 |
| Steve O001 decision string | `nmb3/nmb3_decisions.log` 2026-04-25T16:34:20Z entry | b42ee30 |

## NMB3 objective record

This directory satisfies the success criteria of NMB3 objective
**O004** ("Lock M3.1 into the autonomous-loop archive") in
`nmb3/nmb3_objective_map.md`.  O004 status moves from PROPOSED to
SUCCEEDED in the commit that creates this directory.
