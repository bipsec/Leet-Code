class Solution:
    def maxAdjacentDistance(self, nums) -> int:

        maxDiff = 0

        for i in range(len(nums) - 1, -1, -1):
            diff = abs(nums[i] - nums[i - 1])

            if diff > maxDiff:
                maxDiff = diff

        return maxDiff


s = Solution()
print(s.maxAdjacentDistance(nums=[1, 2, 4]))
print(s.maxAdjacentDistance(nums=[-5, -10, -5]))
print(s.maxAdjacentDistance(nums=[1, 2, 3, 4, 5]))
print(s.maxAdjacentDistance(nums=[-1, -2, -3, -4, -5]))
print(s.maxAdjacentDistance(nums=[-1, -2]))
print(s.maxAdjacentDistance(nums=[-1, -1]))
