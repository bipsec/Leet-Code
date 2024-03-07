def orbitax():
  n = int(input())
  for i in range(n):
    a = int(input())
    nums = list(map(int, input().strip().split()))[:a]
    res = 0
    for j in range(1, len(nums)):
      val = nums[i - 1] | nums[i]
      if val > res:
        res = max(res, val)
    print(res)


orbitax()
