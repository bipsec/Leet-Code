class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:


        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            i -= 1
        return nums

        


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([1, 1, 2]))
