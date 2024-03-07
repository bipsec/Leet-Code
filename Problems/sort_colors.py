class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # INSERTION Sorting Technique

        for val in range(1, len(nums)):
            key = nums[val]
            j = val - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j = j - 1

            nums[j + 1] = key

        return nums


s = Solution()
print(s.sortColors([1, 1, 1, 2, 2, 3]))
print(s.sortColors([0, 0, 1, 1, 1, 1, 2, 2, 3, 3]))
print(s.sortColors([0, 1, 1, 1, 1, 2, 2, 3, 3]))

