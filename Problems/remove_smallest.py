def game():
    n = int(input())

    for i in range(n):
        a = int(input())

        nums = list(map(int, input().strip().split()))[:a]
        nums.sort()
        j = 0
        res = "Yes"
        while j < len(nums)-1:
            val = int(nums[j]) - int(nums[j+1])

            if val < -1:
                res = "No"
                break
            j += 1
        print(res)

game()