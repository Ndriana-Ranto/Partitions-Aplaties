import itertools
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Functions.utils import avoids_incr_m, decompose_runs, run_heads_increasing, run_feet_decreasing, \
    generate_filtered_permutationsT

# ▶️ Exécution principale
if __name__ == "__main__":
    n = 5
    r = 4
    results = generate_filtered_permutationsT(r, n)
    results.sort()

    # Dictionnaire pour classer par nombre de runs
    by_run_count = {}

    for candidate in results:
        runs = decompose_runs(candidate)
        run_count = len(runs)
        by_run_count.setdefault(run_count, []).append((candidate, runs))

    total = 0
    for run_count in sorted(by_run_count.keys()):
        group = by_run_count[run_count]
        print(f"\n🔹 Permutations avec {run_count} run(s) (sous-total : {len(group)})")
        for perm, runs in group:
            print(f"{perm} => runs: {runs}")
        total += len(group)

    print(f"\n✅ Total général : {total}")
