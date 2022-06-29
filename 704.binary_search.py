class Solution:
    def search(self, nums: list[int], target: int) -> int:

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1,0,3,5,9,12], 2))
print(s.search([5], 5))
