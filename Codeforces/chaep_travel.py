import math


def cheap_travel():
    n, m, a, b = map(int, input().split())

    if m * a <= b:
        answer = n * a
    else:
        answer = math.floor(n / m) * b + min((n % m) * a, b)

    print(answer)


cheap_travel()
