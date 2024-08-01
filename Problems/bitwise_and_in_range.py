class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right - 1)
        return right


s = Solution()
print(s.rangeBitwiseAnd(left=5, right=7))
print(s.rangeBitwiseAnd(left=0, right=0))
print(s.rangeBitwiseAnd(left=1, right=2147483647))
