class Solution:
    def leftRightDifference(self, nums):
        totalSum = sum(nums)
        left = 0
        ans = []
        for i in range(len(nums)):
            left += nums[i]
            ans.append(abs(left - totalSum))
            totalSum -= nums[i]
        return ans


s = Solution()
print(s.leftRightDifference([10, 4, 8, 3]))
