class Solution:

    def unique_dict(self, arr):
        dict = {}

        for item in arr:
            if item not in dict:
                dict[item] = 1
            elif item in dict:
                dict[item] -= 1
        return dict

    def uncommonFromSentences(self, s1: str, s2: str):

        s1 = s1.split()
        s2 = s2.split()

        first_dict = self.unique_dict(s1)
        second_dict = self.unique_dict(s2)

        res = []
        for key, val in first_dict.items():
            if key not in second_dict and val > 0:
                res.append(key)

        for key, val in second_dict.items():
            if key not in first_dict and val > 0:
                res.append(key)

        return res


s = Solution()
print(s.uncommonFromSentences("this apple is sweet", s2="this apple is sour"))
print(s.uncommonFromSentences(s1="apple apple", s2="banana"))
