class Solution:
    def findMaxK(self, nums) -> int:
        nums.sort()
        for item in range(len(nums)):
            if nums[item] < 1:
                pos = nums[item] * -1
                if pos in nums[item+1:]:
                    maxVal = pos
                    return maxVal
        return -1


s = Solution()
print(s.findMaxK(nums=[-1, 2, -3, 3]))
print(s.findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
print(s.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
