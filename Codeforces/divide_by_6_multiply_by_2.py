import math


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        cnt3 = 0
        cnt2 = 0
        k = n

        while k % 3 == 0 and k > 1:
            k //= 3
            cnt3 += 1

        while k % 2 == 0 and k > 1:
            k //= 2
            cnt2 += 1

        if k != 1 or cnt3 < cnt2:
            print(-1)
            continue

        cnt6 = cnt3 - cnt2
        n *= pow(2, cnt6)

        while n > 1:
            n //= 6
            cnt6 += 1

        print(cnt6)


solve()
