def move():
    n = int(input())
    for i in range(n):
        target = int(input())
        ans = 0
        if target < 2:
            ans = target % 3 + target // 2 + 1
        elif target >= 3:
            ans = target % 3 + target // 3
        elif target == 2:
            ans = target % 2 + target // 2
        print(ans)


move()

# not done!! codeforces contest
