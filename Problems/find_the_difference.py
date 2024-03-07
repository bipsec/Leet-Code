class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        s.append("")

        for i in range(len(t)):
            if s[i] != t[i]:
                return t[i]


s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "e"))
print(s.findTheDifference("akbf", "fbkag"))
print(s.findTheDifference("aaaa", "aaaea"))
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference("ae", "aea"))

