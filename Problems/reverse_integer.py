class Solution:
    def reverse(self, x: int) -> int:

        res = 0

        if x < 0:
            char = -1
            x = -x
        else:
            char = 1

        while x:
            res = res * 10 + x % 10
            x //= 10

        return 0 if res > pow(2, 31) else res * char


s = Solution()
print((s.reverse(123)))
print((s.reverse(-123)))
print((s.reverse(120)))
print((s.reverse(1225789198590217596126528949051387575357239578598138236)))
