from collections import Counter


def football():
    n = int(input())
    data = [input() for _ in range(n)]

    counter = Counter(data)
    max_count = max(counter.values())
    max_char = [char for char, count in counter.items() if count == max_count]

    print('\n'.join(max_char))


football()
