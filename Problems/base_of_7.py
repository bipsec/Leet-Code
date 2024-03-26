class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = False
        if num < 0:
            negative = True
            num = abs(num)

        result = ""
        while num:
            num, remainder = divmod(num, 7)
            result = str(remainder) + result

        if negative:
            result = "-" + result

        return result
