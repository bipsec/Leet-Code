def is_possible(initial_balance_a, R, V):
    balance_a = initial_balance_a
    balance_b = sum(V) - initial_balance_a
    for i in range(len(R)):
        if R[i] == 'A':
            if balance_a < V[i]:
                return False
            balance_a -= V[i]
        else:
            if balance_b < V[i]:
                return False
            balance_b -= V[i]
    return True


def minimum_initial_balance(R, V):
    max_transfer_to_a = max([V[i] for i in range(len(R)) if R[i] == 'A'])
    min_balance_a = max_transfer_to_a
    max_balance_a = sum(V) - max_transfer_to_a

    while min_balance_a <= max_balance_a:
        mid = (min_balance_a + max_balance_a) // 2
        if is_possible(mid, R, V):
            max_balance_a = mid - 1
        else:
            min_balance_a = mid + 1
    return [min_balance_a, sum(V) - min_balance_a]


print(minimum_initial_balance("BAABA", [2, 4, 1, 1, 2]))
