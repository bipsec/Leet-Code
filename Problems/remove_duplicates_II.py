class Solution:
    def removeDuplicates(self, nums) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            pass


s = Solution()
print(s.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
