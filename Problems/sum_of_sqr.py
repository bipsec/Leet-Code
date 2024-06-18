class Solution:
    def sumOfSquares(self, nums) -> int:

        res = 0
        for i in range(1, len(nums)+1):
            if len(nums) % i == 0:
                val = nums[i-1] ** 2
                if val == int(val):
                    # print(val)
                    res += val
        return res


s = Solution()
print(s.sumOfSquares(nums=[1, 2, 3, 4]))
print(s.sumOfSquares(nums=[2, 7, 1, 19, 18, 3]))
