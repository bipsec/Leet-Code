class Solution:

    def get_key_form_value(self, d, value):

        for k, v in d.items():
            if v == value:
                return k
        return None

    def replaceDigits(self, s: str) -> str:

        alphabets_dict = {chr(i + 96): i for i in range(1, 27)}
        res = ""

        for item in s:
            if item.islower():
                res += item
            else:
                val = alphabets_dict[res[-1]] + int(item)
                res += self.get_key_form_value(alphabets_dict, val)

        return res


s = Solution()
print(s.replaceDigits(s="a1c1e1"))
print(s.replaceDigits(s="a1b2c3d4e"))
