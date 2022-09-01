def taxi():
    n = int(input())
    nums = list(map(int, input().strip().split()))[:n]

    # nums.sort()
    car = 0
    cnt = 0
    for i in range(1, len(nums)+1):
        cnt += nums[i-1]
        if nums[i-1] == 1 or cnt == 3:
            car += 1
        elif cnt >= 4:
            car += 2
        # else:
        #     car -= 1
    print(car // 4 + car % 4)



taxi()