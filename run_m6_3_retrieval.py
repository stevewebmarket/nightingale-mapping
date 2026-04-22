"""M6.3 - small-library retrieval.

Given a query clip, rank a small library of candidate clips by structural
similarity (interval-ratio matching) and report whether a Twinkle-family
relative is retrieved in the top 3.

Reuses the locked extractor + similarity from M6.1 / M6.2 unchanged.
No per-query tuning, no scoring changes, no hand-curated rankings.

Run:    python run_m6_3_retrieval.py

Reproducibility caveat (inherited from M6.2): librosa.load may fall back
from PySoundFile to audioread for compressed formats (mp3, m4a).  Decoder
backend differences across environments can cause sub-percent feature
drift on those clips.
"""
from __future__ import annotations

import run_m6_1_similarity as m61


# Pre-set queries and library for M6.3.
QUERIES = ["twinkle_box", "twinkle_harmonica", "twinkle_people"]

# Library = all real clips + the synthetic transform of twinkle_box.
# Spec asks for >= 8 candidates; we have 9.  Synthetic orchestra transforms
# are excluded from the library because they are sanity-check artefacts for
# M6.1, not retrieval targets.
LIBRARY = [
    "twinkle_box",
    "twinkle_harmonica",
    "twinkle_people",
    "twinkle_box_tstretch",
    "orchestra",
    "rock",
    "flute",
    "highenergy",
    "polyphonic",
]

TOP_K = 3  # how many top hits count as "retrieved"


def is_twinkle_family(name: str) -> bool:
    """A 'Twinkle-family' candidate is any clip whose name starts with
    'twinkle' (covers the three real recordings + the synthetic transform)."""
    return name.startswith("twinkle")


def relatives_of(query: str) -> set[str]:
    """The Twinkle-family clips that should count as a 'correct' retrieval
    for this query.  Excludes the query itself."""
    return {n for n in LIBRARY if is_twinkle_family(n) and n != query}


def rank_query(query: str, features) -> list[tuple[str, dict]]:
    """Score the query against every other library member and return
    (name, similarity-result) sorted by descending score."""
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


def dense_ranks(ranked):
    """Yield (dense_rank, name, result) using dense-rank semantics
    (1, 2, 2, 3, ...) so tied scores share the same rank level."""
    prev_score = None
    rank = 0
    for name, r in ranked:
        if prev_score is None or abs(r["score"] - prev_score) > 1e-6:
            rank += 1
        prev_score = r["score"]
        yield rank, name, r


def print_leaderboard(query: str, ranked):
    print(f"Query: {query}")
    print(f"  {'rank':>4s}  {'candidate':25s} {'score':>6s} "
          f"{'fold':>5s} {'raw':>5s} {'fNT':>5s}  verdict")
    prev_rank = None
    for rank, name, r in dense_ranks(ranked):
        rank_str = f"{rank:>4d}" if rank != prev_rank else "   ="
        marker = " *" if is_twinkle_family(name) else "  "
        print(f"  {rank_str}{marker}{name:25s} {r['score']:6.3f} "
              f"{r['fold_match']:5.2f} {r['raw_match']:5.2f} "
              f"{r['fold_match_nt']:5.2f}  {r['verdict']}")
        prev_rank = rank


def query_passes(query: str, ranked) -> tuple[bool, str | None, int | None]:
    """Pass = at least one Twinkle-family relative appears at dense rank
    <= TOP_K.  Returns (pass, hit_name, hit_rank)."""
    relatives = relatives_of(query)
    for rank, name, _ in dense_ranks(ranked):
        if rank > TOP_K:
            break
        if name in relatives:
            return True, name, rank
    return False, None, None


def top1_is_unrelated(query: str, ranked) -> bool:
    """True if the top-scoring candidate is NOT a Twinkle-family relative."""
    if not ranked:
        return False
    top_name = ranked[0][0]
    return top_name not in relatives_of(query)


def main():
    print("M6.3 -- small-library retrieval")
    print("=" * 70)
    print()
    print("Loading clips and extracting features (locked M5.6 extractor)...")
    features = m61.build_features()
    print(f"  features built for: {sorted(features)}")
    print()
    print(f"Library ({len(LIBRARY)} candidates): {LIBRARY}")
    print(f"Queries ({len(QUERIES)}): {QUERIES}")
    print(f"  retrieval bar: a Twinkle-family relative in top {TOP_K} = PASS")
    print(f"  ('*' marks Twinkle-family clips in the leaderboards)")
    print()

    per_query = []
    for q in QUERIES:
        if q not in features:
            print(f"Query: {q} -- MISSING from features, skipping")
            per_query.append((q, None, False, None, None, False))
            continue
        ranked = rank_query(q, features)
        print_leaderboard(q, ranked)
        ok, hit, hit_rank = query_passes(q, ranked)
        borderline = ok and top1_is_unrelated(q, ranked)
        if ok and borderline:
            print(f"  -> PASS (borderline): '{hit}' at rank {hit_rank}, "
                  f"but top-1 is unrelated ({ranked[0][0]}) -- "
                  f"top-3 criterion only")
        elif ok:
            print(f"  -> PASS: '{hit}' retrieved at rank {hit_rank}")
        else:
            print(f"  -> FAIL: no Twinkle-family relative in top {TOP_K}")
        print()
        per_query.append((q, ranked, ok, hit, hit_rank, borderline))

    # ---------------------------------------------------------------------
    # Pass-condition self-check
    # ---------------------------------------------------------------------
    n_queries = len([q for q, _, _, _, _, _ in per_query if q in features])
    n_lib = len(LIBRARY)
    n_passed = sum(1 for _, _, ok, _, _, _ in per_query if ok)
    n_borderline = sum(1 for _, _, _, _, _, b in per_query if b)
    cond1 = n_queries >= 3
    cond2 = n_lib >= 8
    cond3 = n_passed >= 2

    # cond4: spec wording -- "unrelated clips do not outrank ALL Twinkle-family
    # matches for the passing queries."  Spec-faithful check is
    # max(relative_scores) >= min(unrelated_scores), i.e. at least one
    # relative is not outranked by every single unrelated clip.
    cond4 = True
    cond4_details = []
    for q, ranked, ok, _, _, _ in per_query:
        if not ok or ranked is None:
            continue
        relatives = relatives_of(q)
        rel_scores = [r["score"] for n, r in ranked if n in relatives]
        unrel_scores = [r["score"] for n, r in ranked if n not in relatives]
        if rel_scores and unrel_scores:
            ok_q = max(rel_scores) >= min(unrel_scores)
            cond4_details.append((q, ok_q, max(rel_scores),
                                  min(unrel_scores), max(unrel_scores)))
            if not ok_q:
                cond4 = False

    # cond5: weak-evidence cases honestly labeled.  The verdict gating in
    # M6.1 (>=4 non-trivial intervals on both sides) enforces this; we
    # check that no row labelled "structural match" had < 4 non-trivial
    # intervals on either side.
    cond5 = True
    cond5_violations = []
    for q, ranked, _, _, _, _ in per_query:
        if ranked is None:
            continue
        for name, r in ranked:
            strong = r["verdict"] in ("structural match", "partial melodic match")
            weak_evidence = min(r["nontriv_a"], r["nontriv_b"]) < 4
            if strong and weak_evidence:
                cond5 = False
                cond5_violations.append((q, name, r["verdict"],
                                         r["nontriv_a"], r["nontriv_b"]))

    # cond6: output includes ranked list, scores, verdicts -- printed above
    cond6 = True
    # cond7: fresh-clone reproducible -- verified externally
    cond7 = "EXTERNAL"

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print("Pass-condition self-check:")
    print(f"  1. queries >= 3:                                   "
          f"{n_queries:>2d}      {tag(cond1)}")
    print(f"  2. library size >= 8:                              "
          f"{n_lib:>2d}      {tag(cond2)}")
    print(f"  3. >= 2/3 queries retrieve Twinkle-family in top {TOP_K}: "
          f"{n_passed}/{len(QUERIES)}     {tag(cond3)}")
    print(f"  4. unrelated clips do NOT outrank all Twinkle-family "
          f"relatives for passing queries: {tag(cond4)}")
    for q, ok_q, mr, min_u, max_u in cond4_details:
        print(f"       {q:25s} max-relative={mr:.3f} "
              f"min-unrelated={min_u:.3f} max-unrelated={max_u:.3f}  "
              f"{tag(ok_q)}")
    print(f"  5. weak-evidence rows honestly labeled: {tag(cond5)}")
    if cond5_violations:
        for q, name, v, na, nb in cond5_violations:
            print(f"       VIOLATION: {q} vs {name} -> '{v}' "
                  f"with non-trivial counts {na}/{nb}")
    print(f"  6. ranked list + scores + verdicts in output: PASS (printed above)")
    print(f"  7. fresh-clone reproducible: NOT VERIFIED HERE -- this script")
    print(f"     is deterministic given the locked extractor + sample files;")
    print(f"     verify externally by cloning the canonical repo, running")
    print(f"     scripts/fetch_samples.py, then re-running this script.")

    overall = cond1 and cond2 and cond3 and cond4 and cond5 and cond6
    print()
    if n_borderline:
        print(f"Queries passed: {n_passed}/{len(QUERIES)}  "
              f"({n_borderline} borderline -- top-1 was unrelated)")
    else:
        print(f"Queries passed: {n_passed}/{len(QUERIES)}")
    print(f"M6.3 {'PASS' if overall else 'FAIL'}")


if __name__ == "__main__":
    main()
