class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        newString = ""
        count = 0

        for i in range(1, len(s)):
            if s[i - 1] not in newString and s[i - 1] != s[i]:
                newString += s[i - 1]
        # print(newString)
        res = ""
        for i in range(len(s)):
            start, end = 0, len(s) - 1
            c = len(newString)
            while start <= end:
                if newString[:] == s[start:c]:
                    res += s[start: c]
                start += len(newString)
            c += start


s = Solution()
print(s.repeatedSubstringPattern(s="abab"))
print(s.repeatedSubstringPattern(s="aba"))
print(s.repeatedSubstringPattern(s="abcabcabcabcabc"))
print(s.repeatedSubstringPattern(s="aaaaaaaaaaaaabaaaaaaaaaaaaaa"))
