def lets_hire_police():
    t = int(input())

    nums = list(map(int, input().split()[:t]))

    count = 0
    pos = 0
    for item in nums:
        if item == -1 and pos == 0:
            count += 1
        elif item != -1:
            pos += item
        elif item == -1 and pos != 0:
            pos += item

    print(count)


lets_hire_police()
