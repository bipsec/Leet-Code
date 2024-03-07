class Solution:
    def canJump(self, nums: list[int]) -> bool:

        current_idx = 0

        for i in range(len(nums)-1):
            if nums[i] == 0 and current_idx <= i:
                return False
            current_idx = max(current_idx, nums[i] + i)
            # print(current_idx)
        return True


s = Solution()
# print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([2, 1, 2, 0, 4]))
print(s.canJump([0, 1, 3]))
# print(s.canJump([1, 8, 7,  5, 3]))
# print(s.canJump([4, 4,  2, 5, 3]))
# print(s.canJump([1, 3, 2, 4, 1, 5, 3]))
# print(s.canJump([0, 1]))
