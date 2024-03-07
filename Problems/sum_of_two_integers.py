class Solution:
    def getSum(self, a: int, b: int) -> int:

        while b != 0:
            res = a & b

            a = a ^ b
            b = res << 1

        return a

        # if a > b > 0:
        #     while b > 0:
        #         a += 1
        #         b -= 1
        #     return a
        #
        # elif a < b < 0:
        #     a = -1 * a
        #     b = -1 * b
        #     while b > 0:
        #         a += 1
        #         b -= 1
        #     return -a
        #
        # else:
        #     if a == 0:
        #         return b
        #     elif b == 0:
        #         return a
        #     else:
        #         while b > 0:
        #             a += 1
        #             b -= 1
        #         return a


s = Solution()
print(s.getSum(1, 2))
print(s.getSum(2, 3))
print(s.getSum(-1000, 1000))
print(s.getSum(-12, -8))
print(s.getSum(-12, 0))
print(s.getSum(0, 12))
print(s.getSum(0, -1))
print(s.getSum(0, 0))
print(s.getSum(5, 0))
