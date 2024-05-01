def divisibility_problem():
    t = int(input())

    while t > 0:
        n, m = map(int, input().split())

        if n % m == 0:
            print(0)
            continue
        else:
            div = n // m
            pls = (div + 1) * m
            print(pls-n)

        t -= 1


divisibility_problem()
