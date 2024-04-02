

def sereja_and_dima():
    n = int(input())
    nums = list(map(int, input().split()[:n]))

    sereja_got = dima_got = 0
    left, right = 0, n - 1
    sereja_turn = True

    for _ in range(n):
        if sereja_turn:
            sereja_got += max(nums[left], nums[right])
            left, right = (left + 1, right) if nums[left] > nums[right] else (left, right - 1)
        else:
            dima_got += max(nums[left], nums[right])
            left, right = (left + 1, right) if nums[left] > nums[right] else (left, right - 1)

        sereja_turn = not sereja_turn

    print(sereja_got, dima_got)


sereja_and_dima()

