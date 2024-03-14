def check_od_or_even():
    t = int(input())

    evenNums = []
    oddNums = []

    nums = list(map(int , input().split()[:t]))

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evenNums.append(nums[i])
            
        elif nums[i] % 2 != 0:
            oddNums.append(nums[i])



    if len(evenNums) == 1:
        return nums.index(evenNums[0]) + 1
    else:
        return nums.index(oddNums[0]) + 1





print(check_od_or_even())