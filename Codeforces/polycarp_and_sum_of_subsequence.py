def find():
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        unique = nums[-1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1, 1):
                for k in range(j + 1, len(nums) - 1, 1):
                    if nums[i] + nums[j] + nums[k] == unique:
                        print(nums[i], nums[j], nums[k])
                        return


find()
