class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                return num
            elif num[i] == "0":
                num = num[:i]
        return num


s = Solution()
print(s.removeTrailingZeros("51230100"))
print(s.removeTrailingZeros("123"))
print(s.removeTrailingZeros("1235632023640326003260000000000000000000000000000"))
