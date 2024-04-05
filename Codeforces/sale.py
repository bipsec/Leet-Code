def dekhi_bob_lav_korte_pare_kina():
    a, b = map(int, input().split()[:2])

    nums = list(map(int, input().split()[:a]))

    nums.sort()
    count = 0
    for item in range(0, b):
        if nums[item] < 1:
            count += abs(nums[item])

    print(count)


dekhi_bob_lav_korte_pare_kina()
