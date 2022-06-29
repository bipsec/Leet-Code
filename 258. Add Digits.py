class Solution:
    def addDigits(self, num: int) -> int:

        if num <= 0:
            return 0

        while num >= 10:
            num = num % 10 + num // 10
        return num

        # if num == 0:
        #     return 0
        # elif num % 9 == 0:
        #     return 9
        # else:
        #     return num % 9


s = Solution()
print(s.addDigits(300))
