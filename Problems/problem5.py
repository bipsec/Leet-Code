class Solution:
  def zeroFilledSubarray(self, nums) -> int:
    count, ans = 0, 0
    for i in range(len(nums)):
      if nums[i] == 0:
        count += 1
      else:
        count = 0
      ans += count
    return ans


s = Solution()
print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
print(s.zeroFilledSubarray([2, 10, 2019]))
