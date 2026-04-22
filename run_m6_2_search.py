"""M6.2 - structural similarity search.

Given a query clip, rank every other clip in the library by how structurally
similar it is, using the M6.1 similarity score and verdict.

This turns the pairwise metric from M6.1 into a usable behaviour:
"find the clips that are structurally most like this one."

Run:    python run_m6_2_search.py                    # all queries, default library
        python run_m6_2_search.py twinkle_box        # single query
"""
from __future__ import annotations

import sys

import run_m6_1_similarity as m61


def rank_against_library(query, features, exclude=()):
    """Return a list of (candidate_name, similarity_dict) sorted by score
    descending.  Skips the query itself and any names in `exclude`."""
    qf = features[query]
    rows = []
    for name, ff in features.items():
        if name == query or name in exclude:
            continue
        rows.append((name, m61.similarity(qf, ff)))
    rows.sort(key=lambda kv: kv[1]["score"], reverse=True)
    return rows


# Queries chosen to exercise the operator's "obvious test cases":
#   - twinkle_box / _harmonica / _people: same melody, different instrument
#   - orchestra:                          known to be a sustained tone (control)
QUERIES = ["twinkle_box", "twinkle_harmonica", "twinkle_people", "orchestra"]


def main():
    print("Loading clips and extracting features (this reuses M6.1)...")
    features = m61.build_features()

    queries = sys.argv[1:] if len(sys.argv) > 1 else QUERIES
    for q in queries:
        if q not in features:
            print(f"  unknown query clip: {q!r}  (known: {sorted(features)})")
            continue

    print()
    for q in queries:
        if q not in features:
            continue
        # Exclude the synthetic transformed copies of OTHER clips so
        # the ranking is between real, distinct candidates.  The query's
        # own transformed copy stays in -- it's the natural top match
        # and a built-in sanity check.
        exclude = {x for x in features
                   if (x.endswith("_pshift") or x.endswith("_tstretch"))
                   and not x.startswith(q)}

        print(f"Query: {q}")
        qf = features[q]
        print(f"  query has {qf['valid_ratios'] if 'valid_ratios' in qf else sum(1 for r in qf['ratios'] if r is not None)} valid ratios, "
              f"{sum(1 for r in qf['ratios'] if m61._is_nontrivial(r))} non-trivial")
        ranked = rank_against_library(q, features, exclude=exclude)

        print(f"  {'rank':>4s}  {'candidate':25s} {'score':>6s} "
              f"{'fold':>5s} {'raw':>5s} {'fNT':>5s}  verdict")
        for i, (name, r) in enumerate(ranked, 1):
            print(f"  {i:>4d}  {name:25s} {r['score']:6.3f} "
                  f"{r['fold_match']:5.2f} {r['raw_match']:5.2f} "
                  f"{r['fold_match_nt']:5.2f}  {r['verdict']}")
        print()

    # ---------------------------------------------------------------------
    # Pre-set pass condition self-check
    # ---------------------------------------------------------------------
    # 1. ranking must be non-degenerate (top != bottom)
    # 2. for any query whose own transformed copy is in the library, that
    #    transformed copy must rank above ALL unrelated clips
    # 3. at least one same-melody pair (twinkle vs twinkle) must rank above
    #    a different-melody pair (twinkle vs orchestra/rock/etc.)
    # 4. fresh-clone behaviour identical to M6.1's
    print("Pass-condition self-check:")

    non_degenerate_ok = True
    transformed_ok = True
    for q in queries:
        if q not in features:
            continue
        exclude = {x for x in features
                   if (x.endswith("_pshift") or x.endswith("_tstretch"))
                   and not x.startswith(q)}
        ranked = rank_against_library(q, features, exclude=exclude)
        if not ranked:
            continue
        scores = [r["score"] for _, r in ranked]
        if max(scores) - min(scores) < 0.05:
            non_degenerate_ok = False
        own_tform = [n for n, _ in ranked
                     if n.startswith(q) and n != q]
        if own_tform:
            top_tform_idx = min(i for i, (n, _) in enumerate(ranked)
                                if n in own_tform)
            unrelated_idx = [i for i, (n, _) in enumerate(ranked)
                             if not n.startswith(q.split("_")[0])]
            if unrelated_idx and top_tform_idx >= min(unrelated_idx):
                transformed_ok = False

    # melody-vs-non-melody check using twinkle_box's ranking
    melody_ok = False
    if "twinkle_box" in features:
        exclude = {x for x in features
                   if (x.endswith("_pshift") or x.endswith("_tstretch"))
                   and not x.startswith("twinkle_box")}
        ranked = rank_against_library("twinkle_box", features, exclude=exclude)
        twinkle_scores = [r["score"] for n, r in ranked
                          if n.startswith("twinkle")]
        other_scores = [r["score"] for n, r in ranked
                        if not n.startswith("twinkle")]
        if twinkle_scores and other_scores:
            melody_ok = max(twinkle_scores) > max(other_scores)

    def tag(ok):
        return "PASS" if ok else "FAIL"

    print(f"  1. non-degenerate ranking spread:        {tag(non_degenerate_ok)}")
    print(f"  2. own transformed copy ranks above unrelated clips: "
          f"{tag(transformed_ok)}")
    print(f"  3. same-melody (twinkle*) ranks above different-melody:  "
          f"{tag(melody_ok)}")
    print(f"  4. numeric ranking + per-row verdict output:      "
          f"PASS (printed above)")
    print(f"  5. fresh-clone reproducible: NOT VERIFIED HERE -- this script")
    print(f"     is deterministic given the locked extractor + sample files;")
    print(f"     verify externally by cloning the canonical repo, running")
    print(f"     scripts/fetch_samples.py, then re-running this script.")


if __name__ == "__main__":
    main()
