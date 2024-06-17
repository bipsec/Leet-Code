class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(int(c ** 0.5) + 1):
            val = pow((c - i * i), 0.5)
            if val == int(val):
                return True
        return False


s = Solution()
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(4))
