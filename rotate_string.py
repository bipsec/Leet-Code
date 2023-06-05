class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        newString = ""

        for i in range(len(s)-1, -1, -1):
            if s[i] == goal[0]:
                newString += s[i:] + s[:i]
                break
        return newString


s = Solution()
# print(s.rotateString(s="abcde", goal="cdeab"))
# print(s.rotateString(s="abcde", goal="abced"))
# print(s.rotateString(s="abkde", goal="abccmaioweed"))
# print(s.rotateString(s="ferawgcde", goal="abcedfhj"))
# print(s.rotateString(s="aaab", goal="abaa"))
print(s.rotateString("clrwmpkwru", "wmpkwruclr"))
