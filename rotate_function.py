class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:

        n = len(nums)
        val = sum(nums)

        res = sum(idx * val for idx, val in enumerate(nums))
        total = res

        for i in range(n):
            total += n * nums[i] - val

            res = max(res, total)

        return res












s = Solution()
print(s.maxRotateFunction([4, 3, 2, 6]))
print(s.maxRotateFunction([100]))
