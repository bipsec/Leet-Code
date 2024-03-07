def practice():
    a = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(len(a)):
        if a[i] >= 10:
            cnt += 1
    print(cnt)

practice()