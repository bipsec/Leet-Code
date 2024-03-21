def count_and_go():
    t = int(input())

    nums = list(map(int, input().split()[:t]))

    min_val = nums[0]
    max_val = nums[0]
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
            count += 1
        if nums[i] > max_val:
            max_val = nums[i]
            count += 1

    print(count)


count_and_go()
