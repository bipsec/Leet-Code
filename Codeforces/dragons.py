def dragon_dhorte_chai():
    s, n = map(int, input().split())

    nums = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        nums.append((x, y))

    nums.sort()

    flag = True
    for item in nums:
        if s <= item[0]:
            flag = False
            break
        s += item[1]

    if flag:
        print("YES")
    else:
        print("NO")


dragon_dhorte_chai()
