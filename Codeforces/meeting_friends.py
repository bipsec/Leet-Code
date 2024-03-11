def sorting_distance():
    nums = list(map(int, input().split()))
    nums.sort()

    val = abs(nums[1] - nums[0])
    val_2 = abs(nums[2] - nums[1])

    if val == val_2:
        return val * 2
    else:
        return val + val_2

print(sorting_distance())
