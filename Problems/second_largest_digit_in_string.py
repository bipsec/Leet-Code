class Solution:
    def secondHighest(self, s: str) -> int:
        res = []

        for i in range(len(s)):
            if s[i].isdigit():
                res.append(int(s[i]))

        # print(res)
        res = list(sorted(set(res)))
        # print(res)

        if len(res) >= 2:
            return res[-2]
        else:
            return -1


s = Solution()
print(s.secondHighest(s="dfa12321afd"))
print(s.secondHighest(s="abc1111"))
print(s.secondHighest(s="239kjfnajwh398598q2j29837917251b"))
print(s.secondHighest(s="111121"))
print(s.secondHighest(s="hciuvahwi82734ckjna3u498275612f89247123hv"))
