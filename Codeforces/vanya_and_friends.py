def bent_down():
    t, w = list(map(int, input().split()[:2]))
    count = 0

    nums = list(map(int, input().split()[:t]))

    for item in nums:
        if item > w:
            count += 2
        else:
            count += 1
    print(count)


bent_down()
