import sys

def fractional_knapsack(n,w, values, weights):
    total_value = 0
    frac_val = []

    for i in range(0, n):
        frac_val.append(values[i] / weights[i])

    indexed_list = enumerate(frac_val)

    sorted_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)

    sorted_indices = [index for index, value in sorted_list]
    for i in sorted_indices:
        if w == 0:
            break
        a = min(w, weights[i])
        total_value += a * frac_val[i]
        w -= a
    return format(round(total_value, 4), '.4f')

data = list(map(int, sys.stdin.read().split()))
n, w = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2*n+2):2]
values = list(map(int,values))
weights = list(map(int,weights))

print(fractional_knapsack(int(n),int(w), values, weights))
