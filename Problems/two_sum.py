class Solution:
    def twoSum(self, nums, target):
        dupes = {}

        for i in range(0, len(nums)):
            if nums[i] in dupes.keys():
                return [dupes[nums[i]], i]
            dupes[target-nums[i]] = i


s = Solution()
print(s.twoSum([3, 2, 4, 3], 6))
print(s.twoSum([2, 7, 10, 14], 17))
