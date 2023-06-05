class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return int(dividend/divisor)


s = Solution()
print(s.divide(dividend=10, divisor=3))
print(s.divide(dividend=7, divisor=-3))
print(s.divide(dividend=-1, divisor=-1))
print(s.divide(dividend=-2147483648, divisor=-1))
