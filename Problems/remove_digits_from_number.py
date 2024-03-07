class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = 0
        number = list(number)
        start, end = 0, len(number)-1
        for i in number:
            while start < end:
                if number[start] == digit:
                    number.pop(start)
                    # print(number)
                    res = "".join([elm for elm in number])
                    result = max(int(res), result)
                start += 1
        return result


s = Solution()
# print(s.removeDigit("123", 3))
# print(s.removeDigit("1231", 1))
# print(s.removeDigit("551", 5))
print(s.removeDigit("133235", "3"))

