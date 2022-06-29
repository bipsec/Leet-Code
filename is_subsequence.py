class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        dupes = []
        letters = s
        letters += "1" * (len(t) - len(s))
        start = end = 0
        for i in range(0, len(letters)):
            if letters[start] == t[end]:
                dupes.append(letters[start])
                start += 1
            end += 1
        new_s = "".join([i for i in dupes])
        # print(s, new_s)
        if s == new_s:
            return True
        return False

    # start = 0
    # item = 0
    #
    # while start < len(s) and item < len(t):
    #     if s[start] == t[item]:
    #         start += 1
    #     item += 1
    # if start == len(s):
    #     return True
    # return False



s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("abck", "ahabgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
print(s.isSubsequence("l", "r"))
print(s.isSubsequence("acb", "ahbdc"))
print(s.isSubsequence("", ""))
print(s.isSubsequence("aaaaaa", "bbaaaa"))

