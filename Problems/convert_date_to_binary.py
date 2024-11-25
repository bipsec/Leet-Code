class Solution:
    def decimal_to_binary(self, n):
        if n == 0:
            return '0'
        binary = []
        while n > 0:
            binary.insert(0, str(n % 2))
            n = n // 2
        return ''.join(binary)

    def convertDateToBinary(self, date: str) -> str:

        year, month, day = date.split("-")

        year = self.decimal_to_binary(int(year))
        month = self.decimal_to_binary(int(month))
        day = self.decimal_to_binary(int(day))

        # print(year, "--", month, "--", day)

        return year + "-" + month + "-" + day


s = Solution()
print(s.convertDateToBinary(date="2080-02-29"))
print(s.convertDateToBinary(date="1900-01-01"))
