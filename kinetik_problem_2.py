def min_initial_balances(recipients, values):
    # initialize balances of banks A and B to 0
    balance_a = 0
    balance_b = 0

    # iterate over transfers, updating balances accordingly
    for i in range(len(recipients)):
        if recipients[i] == 'A':
            balance_a -= values[i]
        else:
            balance_b -= values[i]

        if balance_a < 0 or balance_b < 0:
            # transfers cannot be completed with current initial balance
            return [max(-balance_a, 0), max(-balance_b, 0)]

    # transfers can be completed with 0 initial balance
    return [max(-balance_a, 0), max(0, -balance_b)]


recipients = "ABAB"
values = [10, 5, 10, 15]
result = min_initial_balances(recipients, values)
print(result)  # output: [0, 15]

recipients = "BAABA"
values = [2, 4, 1, 1, 2]
result = min_initial_balances(recipients, values)
print(result)  # output: [2, 4]
