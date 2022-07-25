def remove():
    n = int(input())

    while n:
        a = int(input())
        dupes = list(map(int, input().strip().split()))
        seen = []
        for j in range(1, len(dupes)):
            if dupes[j] - dupes[j-1] <= 1:
                seen.append(dupes[j-1])

        seen.append(dupes[-1])
        print(seen)

        n -= 1



remove()