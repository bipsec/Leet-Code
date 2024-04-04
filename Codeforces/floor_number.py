import math


def floor():
    for i in range(int(input())):
        n, x = map(int, input().split())
        if n <= 2:
            print(1)
        else:
            final = n - 2
            print(math.ceil(final / x) + 1)


floor()
