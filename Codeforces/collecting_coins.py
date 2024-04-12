
def collect_coins():

    t = int(input())

    for _ in range(t):
        a, b, c, n = map(int, input().split())

        maxi = max(a, b, c)
        n -= 3 * maxi - (a + b + c)

        if n < 0 or n % 3 != 0:
            print("NO")
        else:
            print("YES")


collect_coins()
