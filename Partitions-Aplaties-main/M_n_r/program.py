#manangatra
import sys
import os
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Functions.utils import decompose_runs, generate_filtered_permutations

# ▶️ Exécution principale
if __name__ == "__main__":
    n = 7      # Taille de la permutation
    r = 5      # Longueur exacte de la sous-suite croissante contenant 1

    results = generate_filtered_permutations(n, r)
    results.sort()

    by_run_count = defaultdict(list)
    for perm in results:
        runs = decompose_runs(perm)
        by_run_count[len(runs)].append((perm, runs))

    total = 0
    for run_count in sorted(by_run_count):
        group = by_run_count[run_count]
        print(f"\n🔹 Permutations avec {run_count} run(s) (sous-total : {len(group)})")
        for perm, runs in group:
            print(f"{perm} => runs: {runs}")
        total += len(group)

    print(f"\n✅ Total général : {total}")
