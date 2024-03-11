class Solution:

    def minimumLength(self, s: str) -> int:
        res = ""
        start, end = 0, len(s) -1

        while start < end:
            if s[start] == s[start+1] and s[start] == s[end]:
                s.removeprefix(s[start:start+1])
                s.removesuffix(s[end])
                print("Checking S 1", s)
            elif s[start] == s[end] and s[start] == s[end-1]:
                s.removeprefix(s[start])
                s.removesuffix(s[end-1])
                print("Checking S 2", s)
            elif s[start] == s[end]:
                s.removeprefix(s[start])
                s.removesuffix(s[end])
                print("Checking S 3", s)
            elif s[start] != s[start+1]:
                print("Checking S 4", s)
                res += s[start]
                # start, end = 0, len(res)
            start += 1
        return res




s = Solution()
# print(s.minimumLength(s = "cabaabac"))
# print(s.minimumLength(s = "caba"))
print(s.minimumLength(s = "aabccabba"))