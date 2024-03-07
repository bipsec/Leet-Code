class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        return nums


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))
