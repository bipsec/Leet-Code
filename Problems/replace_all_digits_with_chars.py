class Solution:

    def get_char(self, char, index):
        return chr(ord(char) + int(index))

    def replaceDigits(self, s: str) -> str:
        res = ""

        for index in range(len(s)):
            res += self.get_char(s[index - 1], s[index]) if index % 2 else s[index]

        return res


s = Solution()
print(s.replaceDigits(s="a1c1e1"))
print(s.replaceDigits(s="a1b2c3d4e"))
