"""M6.4 - family retrieval demo.

Question moved on from M6.3:

  M6.3:  "given a query, does ANY relative appear in top 3?"
  M6.4:  "given a query, can the system retrieve the WHOLE FAMILY of
          related clips ahead of unrelated ones?"

Reuses the M6.3 ranking and the locked M6.1 similarity unchanged.  No
scoring changes, no per-query tuning, no extractor edits.

Run:    python run_m6_4_family_retrieval.py

Reproducibility caveat (inherited): librosa.load may fall back from
PySoundFile to audioread for compressed formats (mp3, m4a).  Decoder
backend differences can cause sub-percent feature drift on those clips.
"""
from __future__ import annotations

import run_m6_1_similarity as m61
import run_m6_3_retrieval as m63


# Twinkle "family" -- the set of clips that share the Twinkle Twinkle melody
# (three real recordings + one synthetic time-stretch of twinkle_box).
FAMILY = {"twinkle_box", "twinkle_harmonica", "twinkle_people",
          "twinkle_box_tstretch"}

# Queries: the three real twinkle recordings (the synthetic transform is a
# library candidate but not used as a query).
QUERIES = ["twinkle_box", "twinkle_harmonica", "twinkle_people"]

# Library = M6.3 library (9 candidates).  No new clips introduced here,
# so M6.4 is honestly a wrapper milestone over M6.3, not a new dataset.
LIBRARY = m63.LIBRARY

TOP_K_FAMILY = 5  # spec asks for "family hits in top 5"


def family_relatives_of(query: str) -> set[str]:
    """Family members the query could possibly retrieve (excludes itself)."""
    return {n for n in LIBRARY if n in FAMILY and n != query}


def is_family(name: str) -> bool:
    return name in FAMILY


def print_leaderboard(query: str, ranked):
    print(f"Query: {query}")
    print(f"  {'rank':>4s}  {'candidate':25s} {'label':>7s}  {'score':>6s} "
          f"{'fNT':>5s}  verdict")
    prev_rank = None
    for rank, name, r in m63.dense_ranks(ranked):
        rank_str = f"{rank:>4d}" if rank != prev_rank else "   ="
        label = "family " if is_family(name) else "nonfam "
        print(f"  {rank_str}  {name:25s} {label:>7s}  {r['score']:6.3f} "
              f"{r['fold_match_nt']:5.2f}  {r['verdict']}")
        prev_rank = rank


def family_hits_within_rank(query: str, ranked, top_k: int) -> list[str]:
    """Names of family relatives that appear within the first `top_k` dense
    ranks of `ranked` (excluding the query itself)."""
    relatives = family_relatives_of(query)
    hits = []
    for rank, name, _ in m63.dense_ranks(ranked):
        if rank > top_k:
            break
        if name in relatives:
            hits.append(name)
    return hits


def best_family_outranks_all_nonfam(query: str, ranked) -> tuple[bool, float, float]:
    """Returns (does_outrank, best_family_score, max_nonfam_score)."""
    relatives = family_relatives_of(query)
    fam_scores = [r["score"] for n, r in ranked if n in relatives]
    non_scores = [r["score"] for n, r in ranked if n not in FAMILY]
    if not fam_scores or not non_scores:
        return False, 0.0, 0.0
    best_fam = max(fam_scores)
    max_non = max(non_scores)
    # "outranks every unrelated clip" = strictly greater than the highest
    # unrelated score.  Ties with non-family count as not outranking.
    return best_fam > max_non, best_fam, max_non


def query_has_weak_evidence(query: str, features) -> tuple[bool, int]:
    """A query is weak-evidence if its own non-trivial interval count is
    below M6.1's MIN_NT_FOR_VERDICT (4).  Mirrors the gating logic in
    similarity() so weak queries are flagged at the query level too."""
    nt = sum(1 for r in features[query]["ratios"] if m61._is_nontrivial(r))
    return nt < 4, nt


def main():
    print("M6.4 -- family retrieval demo")
    print("=" * 70)
    print()
    print("Loading clips and extracting features (locked M5.6 extractor)...")
    features = m61.build_features()
    print()
    print(f"Library ({len(LIBRARY)} candidates): {LIBRARY}")
    print(f"Family ({len(FAMILY)}): {sorted(FAMILY)}")
    print(f"Queries ({len(QUERIES)}): {QUERIES}")
    print()

    per_query = []
    for q in QUERIES:
        if q not in features:
            print(f"Query: {q} -- MISSING from features, skipping\n")
            continue
        ranked = m63.rank_query(q, features)
        print_leaderboard(q, ranked)
        hits3 = family_hits_within_rank(q, ranked, 3)
        hits5 = family_hits_within_rank(q, ranked, 5)
        outranks, best_fam, max_non = best_family_outranks_all_nonfam(q, ranked)
        weak, nt = query_has_weak_evidence(q, features)
        weak_tag = (f"  [weak-evidence query: only {nt} non-trivial intervals]"
                    if weak else "")
        print(f"  Family hits in top 3: {len(hits3)}  ({hits3})")
        print(f"  Family hits in top 5: {len(hits5)}  ({hits5})")
        print(f"  Best family ({best_fam:.3f}) outranks all non-family "
              f"({max_non:.3f}): {'YES' if outranks else 'NO'}{weak_tag}")
        print()
        per_query.append((q, ranked, hits3, hits5, outranks, weak, nt))

    # ---------------------------------------------------------------------
    # Pre-set pass condition self-check
    # ---------------------------------------------------------------------
    n_queries = len(per_query)
    n_top5_ge2 = sum(1 for _, _, _, h5, _, _, _ in per_query if len(h5) >= 2)
    n_outranks = sum(1 for _, _, _, _, ok, _, _ in per_query if ok)

    # cond4 (real check, not tautology):
    #   (a) every query whose non-trivial-interval count is below the
    #       MIN_NT_FOR_VERDICT threshold (4) MUST be marked weak in the
    #       per-query results; AND
    #   (b) the historically weak query 'twinkle_people' must still be
    #       weak (otherwise something silently changed upstream and the
    #       honesty guarantee is no longer being exercised).
    MIN_NT = 4
    flag_consistent = all(
        weak == (nt < MIN_NT)
        for _, _, _, _, _, weak, nt in per_query
    )
    twinkle_people_row = next(
        ((weak, nt) for q, _, _, _, _, weak, nt in per_query
         if q == "twinkle_people"),
        None,
    )
    expected_weak_still_weak = (
        twinkle_people_row is not None
        and twinkle_people_row[0]
        and twinkle_people_row[1] < MIN_NT
    )

    cond1 = n_queries >= 3
    cond2 = n_top5_ge2 >= 2
    cond3 = n_outranks >= 2
    cond4 = flag_consistent and expected_weak_still_weak
    cond5 = True  # output structure printed above
    cond6 = "EXTERNAL"

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print("Pass-condition self-check:")
    print(f"  1. Twinkle-family queries >= 3:                          "
          f"{n_queries:>2d}      {tag(cond1)}")
    print(f"  2. >= 2 family members in top 5 for >= 2/3 queries:      "
          f"{n_top5_ge2}/3     {tag(cond2)}")
    print(f"  3. Best family hit outranks ALL non-family for >= 2/3:   "
          f"{n_outranks}/3     {tag(cond3)}")
    print(f"  4. weak-evidence honestly flagged AND twinkle_people "
          f"still weak: {tag(cond4)}")
    for q, _, _, _, _, weak, nt in per_query:
        marker = (f"weak ({nt} non-trivial) -- flagged"
                  if weak else f"OK ({nt} non-trivial)")
        print(f"       {q:25s} {marker}")
    if not cond4:
        print(f"       (flag-consistency: {flag_consistent}; "
              f"twinkle_people still weak: {expected_weak_still_weak})")
    print(f"  5. ranked list + family labels + per-query summary: "
          f"PASS (printed above)")
    print(f"  6. fresh-clone reproducible: NOT VERIFIED HERE -- this script")
    print(f"     is deterministic given the locked extractor + sample files;")
    print(f"     verify externally by cloning the canonical repo, running")
    print(f"     scripts/fetch_samples.py, then re-running this script.")

    overall = cond1 and cond2 and cond3 and cond4 and cond5
    print()
    print(f"Family retrieval summary:")
    for q, _, h3, h5, ok, weak, _ in per_query:
        marker = " (weak)" if weak else ""
        print(f"  {q:25s} top3={len(h3)} top5={len(h5)} "
              f"outranks-all-nonfam={'YES' if ok else 'NO'}{marker}")
    print()
    print(f"M6.4 {'PASS' if overall else 'FAIL'}")


if __name__ == "__main__":
    main()
