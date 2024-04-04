def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        count = 0

        while n > 1:
            if n % 6 == 0:
                n //= 6
                count += 1
            else:
                n *= 2
                count += 1
            if n == 1:
                print(count)
                break
            else:
                print(-1)
                break



# need to solve
solve()

