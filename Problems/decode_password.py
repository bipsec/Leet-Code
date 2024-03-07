import string


class Solution:
    def decode_pass(self, key: str, msg: str) -> str:
        letters = list(string.ascii_lowercase)
        print(letters)


s = Solution()
print(s.decode_pass("the quick brown fox jumps over the jungle", "vbts is a jungle"))
