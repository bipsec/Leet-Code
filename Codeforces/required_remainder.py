def required_remainder():
    t = int(input())

    while t > 0:

        x, y, n = map(int, input().split())
        ans = n - (n % x) + y

        if ans <= n:
            print(ans)
        else:
            print(n - (n % x) - (x - y))

        t -= 1


required_remainder()

