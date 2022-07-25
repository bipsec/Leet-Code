def fun():
    n = int(input())

    for i in range(n):
        a = int(input())
        dupes = list(map(int, input().strip().split()))[:a]
        cnt = 0
        for j in dupes:
            if j >= 1000:
                cnt += 1
        print(cnt)


fun()