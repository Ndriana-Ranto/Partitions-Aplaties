import itertools

def avoids_incr_m(seq, m):
    n = len(seq)
    for indices in itertools.combinations(range(len(seq)), m):
        if all(seq[indices[i]] < seq[indices[i+1]] for i in range(m - 1)):
            return False
    return True

def decompose_runs(seq):
    runs = []
    current_run = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i-1] < seq[i]:
            current_run.append(seq[i])
        else:
            runs.append(current_run)
            current_run = [seq[i]]
    runs.append(current_run)
    return runs

def run_heads_increasing(seq):
    runs = decompose_runs(seq)
    heads = [run[0] for run in runs]
    return all(heads[i] < heads[i+1] for i in range(len(heads)-1))

def run_feet_decreasing(seq):
    runs = decompose_runs(seq)
    feet = [run[-1] for run in runs]
    return all(feet[i] > feet[i+1] for i in range(len(feet)-1))

def filter_permutations(elements, prefix=(), filter_functions=[]):
    results = []
    for perm in itertools.permutations(elements):
        candidate = prefix + perm
        if all(filter_func(candidate) for filter_func in filter_functions):
            results.append(candidate)
    return results

def generate_filtered_permutations(r, n):
    filters = [
        lambda seq: avoids_incr_m(seq, r),
        run_heads_increasing,
        run_feet_decreasing
    ]
    return filter_permutations(list(range(2, n+1)), prefix=(1,), filter_functions=filters)

# ▶️ Exécution principale
if __name__ == "__main__":
    n = 5
    r = 4
    results = generate_filtered_permutations(r, n)
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
