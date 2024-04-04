class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


s = Solution()
print(s.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
