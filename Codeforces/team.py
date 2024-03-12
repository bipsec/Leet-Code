def team():
    n = int(input())
    problemSet = []
    ans = 0
    while n > 0:
        nums= list(map(int, input().split()))
        problemSet.append(nums)
        n -= 1
    
    for item in problemSet:
        count = 0
        for i in item:
            if i == 1:
                count += 1
        if count >= 2:
            ans += 1
            count = 0
    
    print(ans)


team()