def lets_restore_three_numbers():
    nums = list(map(int, input().split()))
    nums.sort()
    a = nums[3] - nums[0]
    b = nums[3] - nums[1]
    c = nums[3] - nums[2]
    print(str(a) + " " + str(b) + " " + str(c))


lets_restore_three_numbers()
