class Solution(object):
    def convertToTitle(self, columnNumber):

        output = ""
        while columnNumber > 0:
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26

        return output



s = Solution()
print(s.convertToTitle(columnNumber=1))
print(s.convertToTitle(columnNumber=1212))
print(s.convertToTitle(columnNumber=701))
