class Solution:
    def reverseBits(self, n) -> int:
        decimal = 0
        for i in range(32):
            decimal = (decimal << 1) + (n & 1)
            n >>= 1
        return decimal


s = Solution()
print(s.reverseBits(10100101000001111010011100))
print(s.reverseBits(11111111111111111111111111111101))
print(s.reverseBits(11011111111111111111111111111101))
