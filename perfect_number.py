import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        dupes = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                dupes.extend([i, num // i])
        return sum(dupes) == num
# not mine


s = Solution()
print(s.checkPerfectNumber(4))
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(7))
print(s.checkPerfectNumber(6))
print(s.checkPerfectNumber(1))
# print(s.checkPerfectNumber(100000000))
