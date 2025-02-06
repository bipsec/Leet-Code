class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        res = []
        if s1 == s2:
            return True
        else:
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    res.append([s1[i], s2[i]])

        if len(res) == 2:
            if res[0][0] == res[1][1] and res[0][1] == res[1][0]:
                return True
        return False



s = Solution()
# print(s.areAlmostEqual(s1="bank", s2="kanb"))
# print(s.areAlmostEqual(s1="attack", s2="defend"))
# print(s.areAlmostEqual(s1="kelb", s2="kelb"))
# print(s.areAlmostEqual(s1="aa", s2="ac"))
# print(s.areAlmostEqual(s1="caa", s2="aaz"))
# print(s.areAlmostEqual(s1="caba", s2="abaz"))
print(s.areAlmostEqual(s1="npv", s2="zpn"))
print(s.areAlmostEqual(s1="nav", s2="zpn"))
