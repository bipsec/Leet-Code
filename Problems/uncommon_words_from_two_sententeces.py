class Solution:

    def uncommonFromSentences(self, s1: str, s2: str):

        s1 = s1.split() + s2.split()

        dupes = {}

        for item in s1:
            if item not in dupes:
                dupes[item] = 1
            elif item in dupes:
                dupes[item] -= 1
            else:
                dupes[item] += 1

        res = []

        for key, val in dupes.items():
            if val == 1:
                res.append(key)

        return res


s = Solution()
print(s.uncommonFromSentences("this apple is sweet", s2="this apple is sour"))
print(s.uncommonFromSentences(s1="apple apple", s2="banana"))
