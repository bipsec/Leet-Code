class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        setVal = True
        count = 0
        val, num = dividend, divisor
        if dividend < 0:
            val *= -1
        if divisor < 0:
            num *= -1
        while setVal:
            val -= num
            if val < 0:
                setVal = False
            count += 1
        count -= 1
        result = count
        if divisor < 0 and dividend > 0:
            result *= -1
        elif divisor > 0 and dividend < 0:
            result *= -1
        return result



s = Solution()
print(s.divide(dividend=10, divisor=-3))
print(s.divide(dividend=-7, divisor=-3))
print(s.divide(dividend=0, divisor=-3))
print(s.divide(dividend=10, divisor=-2))
print(s.divide(dividend=10, divisor=10))
