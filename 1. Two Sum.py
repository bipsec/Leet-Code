class Solution:
    def twoSum(self, nums, target):

        dict = {}

        for i in range(0,len(nums)):
            if target - nums[i] in dict:
                return [i+1, dict[target-nums[i]] +1]
            dict[nums[i]] = i


s = Solution()
print(s.twoSum([3, 2, 4], 6))