class Solution:
    def maxSubArray(self, nums: list[int]):

        max_sum = cur_sum = float("-inf")

        for i in range(0, len(nums)):
            cur_sum = max(nums[i], nums[i] + cur_sum)
            max_sum = max(cur_sum, max_sum)
        return max_sum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([1]))






        # """Kadane's Algorithm"""
        #
        # local_max = 0
        # max_sum = nums[0]
        #
        # for i in range(0, len(nums)):
        #     local_max = max(nums[i], nums[i] + local_max)
        #     max_sum = max(local_max, max_sum)
        #     # print(local_max)
        #
        # return max_sum


