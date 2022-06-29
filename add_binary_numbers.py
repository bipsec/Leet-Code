class Solution:
    def addBinary(self, a: str, b: str) -> str:

        binary_sum = bin(int(a, 2) + int(b, 2))

        return binary_sum[2:]




s = Solution()
print(s.addBinary("101", "11"))
print(s.addBinary("11111", "11"))