#manangatra
import itertools
from collections import defaultdict

# ✅ Décomposition en runs croissants
def decompose_runs(seq):
    runs = []
    current_run = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] > seq[i - 1]:
            current_run.append(seq[i])
        else:
            runs.append(current_run)
            current_run = [seq[i]]
    runs.append(current_run)
    return runs

# ✅ Sous-suite croissante de longueur ≥ r contenant 1
def has_increasing_subsequence_of_length_at_least_with_1(seq, r):
    n = len(seq)
    for indices in itertools.combinations(range(n), r):
        subseq = [seq[i] for i in indices]
        if 1 in subseq and all(subseq[i] < subseq[i + 1] for i in range(r - 1)):
            return True
    return False

# ❌ Pas de sous-suite croissante de longueur > r contenant 1
def no_increasing_subsequence_longer_than_r_with_1(seq, r):
    n = len(seq)
    for length in range(r + 1, n + 1):
        for indices in itertools.combinations(range(n), length):
            subseq = [seq[i] for i in indices]
            if 1 in subseq and all(subseq[i] < subseq[i + 1] for i in range(length - 1)):
                return False
    return True

# ✅ Têtes croissantes
def run_heads_increasing(seq):
    runs = decompose_runs(seq)
    heads = [run[0] for run in runs]
    return all(heads[i] < heads[i+1] for i in range(len(heads) - 1))

# ✅ Pieds décroissants
def run_feet_decreasing(seq):
    runs = decompose_runs(seq)
    feet = [run[-1] for run in runs]
    return all(feet[i] > feet[i+1] for i in range(len(feet) - 1))

# ✅ Filtrage des permutations
def filter_permutations(elements, prefix=(), filter_functions=[]):
    results = []
    for perm in itertools.permutations(elements):
        candidate = prefix + perm
        if all(f(candidate) for f in filter_functions):
            results.append(candidate)
    return results

# ✅ Générateur principal
def generate_filtered_permutations(n, r):
    filters = [
        lambda seq: seq[0] == 1,
        lambda seq: has_increasing_subsequence_of_length_at_least_with_1(seq, r),
        lambda seq: no_increasing_subsequence_longer_than_r_with_1(seq, r),
        run_heads_increasing,
        run_feet_decreasing
    ]
    return filter_permutations(list(range(2, n + 1)), prefix=(1,), filter_functions=filters)

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
