class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # res = 1

        # for i in range(0, len(nums)):
        #     res *= nums[i]

        # result = 0
        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[0] + nums[1], nums[1])
        
        # case1 = nums[0]
        # case2 = max(nums[0], nums[0] + nums[1], nums[1])

        # for i in range(0, len(nums)-1):
        #     result = max(case1, case2, )
        #     result = max(result, )

        # return result

        """Kadane's Algorithm"""

        local_max = 1
        max_mul = float("-inf")

        for i in range(0, len(nums)):
            local_max = max(nums[i], nums[i] * local_max)
            max_mul = max(local_max, max_mul)

        return max_mul



s = Solution()

print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([3, -2, 4]))
print(s.maxProduct([-3, -3]))
print(s.maxProduct([4, 3]))
print(s.maxProduct([-4, -3]))
print(s.maxProduct([-2, 3, -4]))
print(s.maxProduct([2, -5, -2, -4, 3]))
