class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        letters = {chr(i + 64): i for i in range(1, 27)}
        value = 0
        n = len(columnTitle) - 1
        for i in range(len(columnTitle)):
            if columnTitle[i]:
                value += letters[columnTitle[i]] * pow(26, n)
                n -= 1
        return value


s = Solution()
print(s.titleToNumber(columnTitle="A"))
print(s.titleToNumber(columnTitle="AB"))
print(s.titleToNumber(columnTitle="ZY"))
print(s.titleToNumber(columnTitle="ABY"))
