class Solution:
    def maxSubArray(self, nums: list[int]):
        cur_sum = 0
        max_sum = float("-inf")
        end = 0
        k = len(nums)

        for i in range(0, len(nums)):
            cur_sum += nums[i]
            # print("Adding values,", cur_sum)
            if i >= (k-1):
                max_sum = max(cur_sum, max_sum)
                # print("Max_sum:", max_sum)
                cur_sum -= nums[i - (k-1)]
                # print("Current_sum:", cur_sum)

        return max_sum


s = Solution()
print(s.maxSubArray([5, 4, -1, 7, 8]))
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(s.maxSubArray([-1, 2, 3, 1, -3, 2], 2))

