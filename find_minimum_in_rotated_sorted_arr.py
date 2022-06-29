class Solution:
    def findMin(self, nums: list[int]) -> int:
        nums.sort()
        return nums[0]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
