def calculate_drinks():
    t = int(input())

    nums = list(map(int, input().split()[:t]))
    ans = 0
    for item in nums:
        ans += item / 100
    ans = ans / len(nums) * 100
    return ans


print(calculate_drinks())
