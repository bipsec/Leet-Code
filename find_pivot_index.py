class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for idx, curr_sum in enumerate(nums):
            right_sum -= curr_sum
            if left_sum == right_sum:
                return idx
            left_sum += curr_sum
        return -1



s = Solution()
print(s.pivotIndex([1,2,3]))
print(s.pivotIndex([2,1,-1]))
print(s.pivotIndex([1,7,3,6,5,6]))


