class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        maxVal = 0

        current_sum = sum(nums[:k])
        for i in range(1, len(nums) - k+1):
            if nums[i] != nums[i+1] and nums[i+1] != nums[i+2]:
                current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            if current_sum > maxVal:
                maxVal = current_sum

        return maxVal


s = Solution()
print(s.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(s.maximumSubarraySum(nums=[4, 4, 4], k=3))
print(s.maximumSubarraySum(nums=[1, 4, 5], k=3))
