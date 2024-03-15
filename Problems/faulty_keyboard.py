class Solution:
    def finalString(self, s: str) -> str:

        while "i" in s:
            i = s.index("i")
            res = s[:i][::-1]
            res2 = s[i + 1:]

            s = "".join([res, res2])
        return s


s = Solution()
print(s.finalString(s="string"))
print(s.finalString(s="poiinter"))
