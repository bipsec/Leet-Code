def okakusama():
    t = int(input())

    while t > 0:

        nums = list(map(int, input().split()[:3]))

        nums.sort()

        if sum(nums[:2]) == nums[2]:
            print("YES")
        else:
            print("NO")

        t -= 1


okakusama()
