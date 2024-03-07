class Solution:
    def isTarget(self, nums: list, target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return False


s = Solution()
print(s.isTarget([1], 1))
print(s.isTarget([1, 2, 3, 5, 5, 8, 10], 12))
print(s.isTarget([1, 1, 1, 1, 1, 1], 1))
print(s.isTarget([0, 0, 1, 3, 5], 5))
print(s.isTarget([0, 0, 1, 3, 5], 0))
print(s.isTarget([0, 0, 3, 3, 5], 3))
