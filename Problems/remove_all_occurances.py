class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while True:
            index = s.find(part)

            if index == -1:
                break
            s = s[:index] + s[index + len(part):]

        return s


s = Solution()
print(s.removeOccurrences(s="daabcbaabcbc", part="abc"))
print(s.removeOccurrences(s="axxxxyyyyb", part="xy"))
