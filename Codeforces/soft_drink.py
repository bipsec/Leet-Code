def lets_make_soft_drink():
    n, k, l, c, d, p, nl, np = map(int, input().split())

    return min(min(k * l // nl, c * d), p // np) // n


print(lets_make_soft_drink())
