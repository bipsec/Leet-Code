import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = ""
        dupes = {}
        cnt = 0
        letters = list(string.ascii_lowercase)
        # print(letters)
        key = key.split()
        new_key = "".join(key)

        for i in range(len(new_key)):
            # print(new_key[i], letters[i])
            if new_key[i] not in dupes.keys():
                dupes[new_key[i]] = letters[i]



        print(dupes)









s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))