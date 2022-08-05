class Solution:
  def minimumOperations(self, nums) -> int:
    count = 0

    while sum(nums) > 0:
      small = min(n for n in nums if n != 0)
      for i in range(len(nums)):
        if nums[i] != 0:
          nums[i] -= small
      count += 1
    return count


s = Solution()
print(s.minimumOperations(nums=[1, 5, 0, 3, 5]))
print(s.minimumOperations(nums=[0, 1]))
print(s.minimumOperations(nums=[5]))
print(s.minimumOperations(nums=[50]))
print(s.minimumOperations(nums=[0, 1, 2, 3]))
