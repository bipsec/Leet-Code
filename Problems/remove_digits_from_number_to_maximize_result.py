class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        max_number = float("-inf")
        for idx, val in enumerate(number):
            if number[idx] == digit:
                ans = int(number[:idx] + number[(idx+1):])
            if ans > max_number:
                max_number = ans
        return str(max_number)

#
# class Solution:
#     def removeDigit(self, number: str, digit: str) -> str:
#         ans = 0
#         max_number = float("-inf")
#         for idx, val in enumerate(number):
#             if number[idx] == digit:
#                 max_number = max(max_number, int(number[:idx] + number[(idx+1):]))
#
#         return str(max_number)


s = Solution()
print(s.removeDigit("123", "3"))
print(s.removeDigit("1231", "1"))
print(s.removeDigit("551", "5"))
