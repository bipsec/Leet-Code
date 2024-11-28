class Solution:
    def arraySign(self, nums) -> int:

        val = 1

        for item in nums:
            val *= item

        if val >= 1:
            return 1
        elif val < 0:
            return -1
        else:
            return 0


s = Solution()
print(s.arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))
print(s.arraySign(nums=[1, 5, 0, 2, -3]))
print(s.arraySign(nums=[-1, 1, -1, 1, -1]))
