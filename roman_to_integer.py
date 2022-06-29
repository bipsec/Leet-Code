class Solution:
    def romanToInt(self, s: str) -> int:

        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0

        for i in s[::-1]:
            if d[i] >= prev:
                result += d[i]
            else:
                result -= d[i]
            prev = d[i]

        return result


s = Solution()
print(s.romanToInt("MCMXCIV"))
