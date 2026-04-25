Block ID:
block_022

Current Milestone:
M6.4 — family-retrieval demo (`run_m6_4_family_retrieval.py`).
PASS as recorded in MILESTONES.md, locked at the M5.6 extractor
SHA d332f54 and unchanged on canonical since.  This block does
NOT introduce a new milestone or modify the locked metric; it
re-validates the existing PASS on a fresh clone with no caches.

Approval Status:
STEVE-APPROVED via two chat strings recorded in
`nmb3/nmb3_decisions.log`:

  - "Execute O033" at 2026-04-25T17:59:01Z (loop-time successor
    to the O024 approval string), which authorised the objective
    in principle but ran into the declared dependency chain
    O033 ← O032 ← O031 ← O030 ← O029 (P6 entry Steve-gate, all
    PROPOSED on canonical at the time).  The loop stopped before
    dispatch and surfaced the dependency-chain issue along with
    the loop's own self-recorded errata that the prior session
    had recommended O033 without tracing the dependency chain.

  - "Override deps for O033 (single-objective waiver)" at
    approximately 2026-04-25T18:00Z, which is the explicit policy
    waiver authorising O033 to execute alone, against the current
    canonical M5.6 extractor, without first re-validating
    M6.1 / M6.2 / M6.3.  The waiver string is logged verbatim in
    decisions.log so the audit trail records the override.

The waiver does NOT alter the M6.4 spec.  In particular the
forbidden actions clause of O033 ("removing the weak-evidence
flag; relaxing cond4") still binds.

One Question to Answer:
Does the locked M6.4 family-retrieval PASS reproduce on a fresh
clone with no caches, including all five pre-set conditions, the
weak-evidence flag for `twinkle_people`, and the cond4 honesty
assertion (every nt<4 query marked weak AND `twinkle_people`
still weak)?

Why This Matters:
M6.4 is the load-bearing PASS for the family-retrieval claim in
the funding package.  It says: given a query Twinkle clip, the
system retrieves Twinkle relatives ahead of unrelated clips, in
two of three cases convincingly (top-3 + outranks), and in the
weak-evidence case (`twinkle_people` voice, only 2 non-trivial
intervals) honestly flags itself as weak rather than overclaiming.
The "honestly flags itself" half of the claim is what the cond4
self-check enforces in the script.

Re-validation matters because the M6.4 result depends on:

  - the locked M5.6 extractor (which O023 has already re-validated
    bit-identically; M6.4 imports from `run_milestones` and uses
    the same locked extractor with no per-query tuning);
  - the locked M6.1 similarity weights (0.45 / 0.25 / 0.30) and
    the >= 4 non-trivial intervals honesty gate;
  - the locked M6.3 ranking semantics (dense-rank, ties visible);
  - the canonical sample set (twinkle_box.mp3,
    twinkle_harmonica.wav, twinkle_people.m4a, twinkle_box_tstretch
    [synthetic], orchestra.wav, rock.wav, flute.mp3,
    polyphonic.mp3, highenergy.wav).

This block does NOT re-validate M6.1 / M6.2 / M6.3 in their own
right (those are separate objectives O030 / O031 / O032, all
PROPOSED on canonical and explicitly NOT executed under this
waiver).  It validates that the M6.4 result built on top of those
upstream components reproduces from a fresh clone with no caches.
A failure here could be due to a regression at any layer, and
would trigger the activation rule for the upstream off-path
objectives (O030 / O031 / O032 would become on-path so the
regression could be localised).

Allowed Actions:
- Dispatch `run_m6_4_family_retrieval.py` exactly as written on
  canonical (no edits to the script; no per-query tuning; no
  scoring changes; no extractor changes).
- Use the shared no-cache reproducibility workflow at
  `.github/workflows/nmb3_no_cache_repro.yml` with target=`m6_4`.
- Capture the run id and head SHA for pinning in the interpreter
  output.
- Compare the captured stdout line-by-line against the M6.4
  baseline narrative in `MILESTONES.md` for: the per-query
  family-hits-in-top-3 / family-hits-in-top-5 / outranks values;
  the weak-evidence flag on `twinkle_people` and only on
  `twinkle_people`; each of the 5 pre-set conditions PASSing
  (with cond4 explicitly fired); and the final `M6.4 PASS` line.

Forbidden Actions:
- Editing `run_m6_4_family_retrieval.py`, `run_m6_3_retrieval.py`,
  `run_m6_1_similarity.py`, `run_milestones.py`, or any other
  pipeline file -- the dispatch must run the canonical scripts
  unmodified.
- Removing the weak-evidence flag for `twinkle_people` from the
  reproduction or relaxing the cond4 honesty check (forbidden by
  O033's spec).
- Caching any sample, library output, or pip dependency.
- Cherry-picking the run -- the first dispatch's result is the
  reproduction unless dispatch failed for infrastructure reasons
  (in which case the failure must be logged honestly and the
  retry's reasoning made explicit in decisions.log).
- Introducing M6.4-specific logic into the shared workflow yml
  (target-specific logic lives in the `script` input, not the
  yml file; this rule comes from O012 / O023 / O039 and binds
  every consumer).
- Auto-committing the reproduction artefact (the workflow does
  not commit; artefacts are pinned by run id + SHA only).

Pass Criteria (per O033 success criteria, mapped concretely):
- Full table reproduces — for each of the 3 queries:
    * twinkle_box        : top3=3, top5=3, outranks=YES
    * twinkle_harmonica  : top3=2, top5=3, outranks=YES
    * twinkle_people     : top3=1, top5=1, outranks=NO
- Weak-evidence flag for `twinkle_people` reproduces (the script
  prints the weak-evidence tag with the non-trivial interval
  count, and twinkle_people's flag is on while the other two
  queries' flags are off).
- The cond4 honesty assertion fires and prints PASS in the
  pre-set condition self-check section.
- The final line prints `M6.4 PASS`.
- All 5 pre-set conditions print PASS (cond6 is EXTERNAL by design).

Out of Scope (explicit non-claims):
- This block does NOT re-validate M6.1, M6.2, or M6.3 (deferred
  under Steve's single-objective waiver).
- This block does NOT relax M6.4's claim or extend it to clips
  outside the canonical Twinkle / non-family library.
- This block does NOT advance any other objective.
- This block does NOT touch policy files, MILESTONES.md, the
  M3.1 archive, the M3.1 closure recommendation, or the P4
  closure recommendation.
- This block does NOT make any funding, commercial, or
  perceptual-validity claim.
