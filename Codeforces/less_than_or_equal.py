def less_than_or_equal():
    l, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    if k == 0:
        ans = arr[0] - 1
    else:
        ans = arr[k - 1]
    res = 0
    for i in arr:
        if i <= ans:
            res += 1

    if ans < 1 or res != k:
        print(-1)
    else:
        print(ans)


less_than_or_equal()
