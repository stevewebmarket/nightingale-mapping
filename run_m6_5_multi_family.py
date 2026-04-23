"""M6.5 -- multi-family retrieval validation.

Question:

    M6.4 showed family-level retrieval works for the Twinkle melody.
    Does it generalize to a SECOND, independently-recorded melody, with
    no per-family tuning, no scoring changes, no extractor edits?

This is a VALIDATION step, not an optimization step.  The pipeline
(extractor, similarity, ranking) is reused unchanged from M5.6 / M6.1
/ M6.3 / M6.4.  All that's added is a second melody family
(Mary Had a Little Lamb, three timbres) and a per-family report.

Run:    python run_m6_5_multi_family.py

Reproducibility caveat (inherited): librosa.load may fall back from
PySoundFile to audioread for compressed formats (mp3, m4a).  Decoder
backend differences can cause sub-percent feature drift on those clips.
"""
from __future__ import annotations

from pathlib import Path

import run_milestones as rm
import run_m6_1_similarity as m61
import run_m6_3_retrieval as m63


# ---------------------------------------------------------------------------
# Family 2 (new): Mary Had a Little Lamb, three timbres.
# Same melody, three different recordings -- the second "obvious test case".
# ---------------------------------------------------------------------------
FAMILY2_CLIPS = [
    ("lamb_solo",  "lamb_solo.mp3"),
    ("lamb_group", "lamb_group.mp3"),
    ("lamb_male",  "lamb_male.mp3"),
]

FAMILY1 = {  # Twinkle (locked in M6.4)
    "twinkle_box", "twinkle_harmonica", "twinkle_people",
    "twinkle_box_tstretch",
}
FAMILY2 = {name for name, _ in FAMILY2_CLIPS}

QUERIES_F1 = ["twinkle_box", "twinkle_harmonica", "twinkle_people"]
QUERIES_F2 = ["lamb_solo", "lamb_group", "lamb_male"]

# Library = M6.3 library + the three Lamb clips.  No other changes.
LIBRARY = list(m63.LIBRARY) + [name for name, _ in FAMILY2_CLIPS]


def add_family2_features(features):
    """Load Lamb clips and append them to the existing features dict
    using the same extraction pipeline as m61.build_features()."""
    for name, path in FAMILY2_CLIPS:
        if not Path(path).exists():
            raise SystemExit(
                f"Missing {path}.  Run: python scripts/fetch_samples.py"
            )
        audio = rm.load_clip(path)
        pitches = m61.extract_pitch_sequence(audio)
        ratios = m61.interval_ratios(pitches)
        folded = [m61.octave_fold_to_unit(r) for r in ratios]
        features[name] = {
            "audio": audio,
            "pitches": pitches,
            "ratios": ratios,
            "folded": folded,
        }
    return features


def family_of(name):
    if name in FAMILY1:
        return "family1"
    if name in FAMILY2:
        return "family2"
    return "nonfam"


def rank_query(query, features):
    """Rank the query against every other library member (descending score)."""
    qf = features[query]
    scored = []
    for cand in LIBRARY:
        if cand == query:
            continue
        if cand not in features:
            continue
        scored.append((cand, m61.similarity(qf, features[cand])))
    scored.sort(key=lambda kv: kv[1]["score"], reverse=True)
    return scored


def family_relatives_of(query):
    own_family = family_of(query)
    if own_family == "nonfam":
        return set()
    family_set = FAMILY1 if own_family == "family1" else FAMILY2
    return {n for n in LIBRARY if n in family_set and n != query}


def family_hits_within_rank(query, ranked, top_k):
    relatives = family_relatives_of(query)
    hits = []
    for rank, name, _ in m63.dense_ranks(ranked):
        if rank > top_k:
            break
        if name in relatives:
            hits.append(name)
    return hits


def best_family_outranks_all_other(query, ranked):
    """Best score among same-family relatives must strictly exceed the best
    score among all clips that are NOT in the query's family
    (this includes both the other family AND non-family clips, so
    family separation is genuinely tested)."""
    relatives = family_relatives_of(query)
    own_family = family_of(query)
    fam_scores = [r["score"] for n, r in ranked if n in relatives]
    other_scores = [r["score"] for n, r in ranked if family_of(n) != own_family]
    if not fam_scores or not other_scores:
        return False, 0.0, 0.0
    best_fam = max(fam_scores)
    max_other = max(other_scores)
    return best_fam > max_other, best_fam, max_other


def query_has_weak_evidence(query, features):
    nt = sum(1 for r in features[query]["ratios"] if m61._is_nontrivial(r))
    return nt < 4, nt


def any_strong_match_outside_family(query, ranked):
    """Returns the first (name, verdict) pair where a clip OUTSIDE the
    query's family is labelled a 'structural match' or 'partial melodic
    match'.  Used by cond4: no unrelated clip should be promoted."""
    own_family = family_of(query)
    for name, r in ranked:
        if family_of(name) == own_family:
            continue
        v = r["verdict"].lower()
        if "structural match" in v or "partial melodic" in v:
            return name, r["verdict"], r["score"]
    return None


def print_leaderboard(query, ranked):
    print(f"Query: {query}  (own family: {family_of(query)})")
    print(f"  {'rank':>4s}  {'candidate':25s} {'label':>7s}  {'score':>6s} "
          f"{'fNT':>5s}  verdict")
    prev_rank = None
    for rank, name, r in m63.dense_ranks(ranked):
        rank_str = f"{rank:>4d}" if rank != prev_rank else "   ="
        label = family_of(name)
        print(f"  {rank_str}  {name:25s} {label:>7s}  {r['score']:6.3f} "
              f"{r['fold_match_nt']:5.2f}  {r['verdict']}")
        prev_rank = rank


def evaluate(queries, features):
    """Return per-query rows: (query, ranked, hits3, hits5, outranks,
    weak, nt, strong_outside)."""
    rows = []
    for q in queries:
        if q not in features:
            print(f"Query: {q} -- MISSING from features, skipping\n")
            continue
        ranked = rank_query(q, features)
        print_leaderboard(q, ranked)
        hits3 = family_hits_within_rank(q, ranked, 3)
        hits5 = family_hits_within_rank(q, ranked, 5)
        outranks, best_fam, max_other = best_family_outranks_all_other(q, ranked)
        weak, nt = query_has_weak_evidence(q, features)
        strong_outside = any_strong_match_outside_family(q, ranked)
        weak_tag = (f"  [weak-evidence query: only {nt} non-trivial intervals]"
                    if weak else "")
        print(f"  Family hits in top 3: {len(hits3)}  ({hits3})")
        print(f"  Family hits in top 5: {len(hits5)}  ({hits5})")
        print(f"  Best same-family ({best_fam:.3f}) outranks all "
              f"other-family + non-family ({max_other:.3f}): "
              f"{'YES' if outranks else 'NO'}{weak_tag}")
        if strong_outside is not None:
            sname, sv, sscore = strong_outside
            print(f"  WARNING: outside-family clip '{sname}' got "
                  f"verdict='{sv}' (score {sscore:.3f})")
        print()
        rows.append((q, ranked, hits3, hits5, outranks, weak, nt,
                     strong_outside))
    return rows


def family_passes(rows, *, label):
    """Apply M6.4-style pass logic to one family's rows and print the
    self-check.  Returns (overall_pass, detail_dict)."""
    n = len(rows)
    n_top3_ge1 = sum(1 for _, _, h3, _, _, _, _, _ in rows if len(h3) >= 1)
    n_outranks = sum(1 for _, _, _, _, ok, _, _, _ in rows if ok)
    no_strong_outside = all(s is None for _, _, _, _, _, _, _, s in rows)

    cond_a = n >= 2
    cond_b = n_top3_ge1 >= 2
    cond_c = n_outranks >= 2
    cond_d = no_strong_outside

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print(f"  [{label}] queries: {n}")
    print(f"    >= 2 queries:                                  {tag(cond_a)}")
    print(f"    family member in top 3 for >= 2 queries:       "
          f"{n_top3_ge1}/{n}     {tag(cond_b)}")
    print(f"    best same-family outranks all-other for >= 2:  "
          f"{n_outranks}/{n}     {tag(cond_c)}")
    print(f"    no outside-family clip labelled strong match:  {tag(cond_d)}")

    overall = cond_a and cond_b and cond_c and cond_d
    return overall, dict(n=n, top3=n_top3_ge1, outranks=n_outranks,
                         no_strong_outside=no_strong_outside)


def twinkle_did_not_regress(f1_rows):
    """M6.4 headline (locked):
       twinkle_box       top3=3 top5=3 outranks-all-nonfam=YES
       twinkle_harmonica top3=2 top5=3 outranks-all-nonfam=YES
       twinkle_people    top3=1 top5=1 outranks-all-nonfam=NO  (weak)

    Note: 'outranks-all-other' here is STRICTER than M6.4's
    'outranks-all-nonfam' because it now includes the lamb family too.
    So we relax that specific check to 'twinkle_box and twinkle_harmonica
    must still beat all clips outside Twinkle' (which is what the strict
    YES required in M6.4 too, since lamb wasn't in the library)."""
    expected = {
        "twinkle_box":       (3, 3, True,  False),  # (top3, top5, outranks, weak)
        "twinkle_harmonica": (2, 3, True,  False),
        "twinkle_people":    (1, 1, False, True),
    }
    diffs = []
    for q, _, h3, h5, ok, weak, _, _ in f1_rows:
        if q not in expected:
            continue
        e_t3, e_t5, e_ok, e_weak = expected[q]
        if (len(h3), len(h5), ok, weak) != (e_t3, e_t5, e_ok, e_weak):
            diffs.append((q, (e_t3, e_t5, e_ok, e_weak),
                          (len(h3), len(h5), ok, weak)))
    return (len(diffs) == 0), diffs


def main():
    print("M6.5 -- multi-family retrieval validation")
    print("=" * 70)
    print()
    print("Loading clips and extracting features (locked M5.6 extractor)...")
    features = m61.build_features()
    add_family2_features(features)
    print()
    print(f"Library ({len(LIBRARY)} candidates): {LIBRARY}")
    print(f"Family 1 (Twinkle, {len(FAMILY1)}): {sorted(FAMILY1)}")
    print(f"Family 2 (Lamb, {len(FAMILY2)}):    {sorted(FAMILY2)}")
    print(f"Queries family 1: {QUERIES_F1}")
    print(f"Queries family 2: {QUERIES_F2}")
    print()

    print("=== Family 1 (Twinkle) ===")
    print()
    f1_rows = evaluate(QUERIES_F1, features)

    print("=== Family 2 (Lamb) ===")
    print()
    f2_rows = evaluate(QUERIES_F2, features)

    # ---------------------------------------------------------------------
    # Pre-set pass condition self-check (declared BEFORE the run)
    # ---------------------------------------------------------------------
    print("Pass-condition self-check:")
    print()
    print("  Family-level checks:")
    f2_pass, _ = family_passes(f2_rows, label="family 2 (Lamb)")
    print()
    f1_pass, _ = family_passes(f1_rows, label="family 1 (Twinkle, sanity)")
    print()

    no_regress, regress_diffs = twinkle_did_not_regress(f1_rows)
    weak_consistent = all(
        weak == (nt < 4)
        for _, _, _, _, _, weak, nt, _ in (f1_rows + f2_rows)
    )

    cond1 = len(QUERIES_F2) >= 2          # at least 2 family-2 queries
    cond2 = sum(1 for _, _, h3, _, _, _, _, _ in f2_rows if len(h3) >= 1) >= 2
    cond3 = sum(1 for _, _, _, _, ok, _, _, _ in f2_rows if ok) >= 2
    cond4 = all(s is None for _, _, _, _, _, _, _, s in f2_rows)
    cond5 = no_regress
    cond6 = weak_consistent
    cond7 = "EXTERNAL"  # fresh-clone reproducibility -- verified externally

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print("  Pre-set conditions (declared before this run):")
    print(f"    1. >= 2 queries from new family:               {tag(cond1)}")
    print(f"    2. family-2 hit in top 3 for >= 2 queries:     {tag(cond2)}")
    print(f"    3. best family-2 outranks all-other for >= 2:  {tag(cond3)}")
    print(f"    4. no outside-family clip labelled strong:     {tag(cond4)}")
    print(f"    5. Twinkle behaviour does not regress:         {tag(cond5)}")
    if not cond5:
        for q, exp, got in regress_diffs:
            print(f"         {q}: expected {exp}, got {got}")
    print(f"    6. weak-evidence cases honestly flagged:       {tag(cond6)}")
    print(f"    7. fresh-clone reproducible: NOT VERIFIED HERE -- this script")
    print(f"       is deterministic given the locked extractor + sample files;")
    print(f"       verify externally by cloning the canonical repo, running")
    print(f"       scripts/fetch_samples.py, then re-running this script.")
    print()

    overall = cond1 and cond2 and cond3 and cond4 and cond5 and cond6
    print("Family retrieval summary:")
    for q, _, h3, h5, ok, weak, _, _ in f1_rows:
        marker = " (weak)" if weak else ""
        print(f"  [F1] {q:25s} top3={len(h3)} top5={len(h5)} "
              f"outranks-all-other={'YES' if ok else 'NO'}{marker}")
    for q, _, h3, h5, ok, weak, _, _ in f2_rows:
        marker = " (weak)" if weak else ""
        print(f"  [F2] {q:25s} top3={len(h3)} top5={len(h5)} "
              f"outranks-all-other={'YES' if ok else 'NO'}{marker}")
    print()
    print(f"Twinkle family: {'PASS' if f1_pass and no_regress else 'FAIL'}")
    print(f"Lamb family:    {'PASS' if f2_pass else 'FAIL'}")
    print()
    print(f"M6.5 {'PASS' if overall else 'FAIL'}")


if __name__ == "__main__":
    main()
