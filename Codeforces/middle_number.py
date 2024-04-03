def lets_find_mid_num():
    t = int(input())

    while t > 0:
        nums = list(map(int, input().split()[:3]))
        nums.sort()
        print(nums[1])

        t -= 1


lets_find_mid_num()
