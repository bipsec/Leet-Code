class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        for i in s:
            if i.upper() in s and i.lower() in s:
                res += i.upper()
        res = sorted(res)
        if not res:
            return ""
        else:
            return res[-1].upper()


s = Solution()
print(s.greatestLetter("lEeTcOdE"))
print(s.greatestLetter("arRAzFif"))
print(s.greatestLetter("AbCdEfGhIjK"))
print(s.greatestLetter("AaohuiabnaiaoopzcnuawgfiuZ"))
print(s.greatestLetter("aaaabbbbbbb111"))
