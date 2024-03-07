class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""
        if len(word1) < len(word2):
            for i in range(len(word1)):
                res += word1[i]
                res += word2[i]
            return res + word2[len(word1):]
        else:
            for i in range(len(word2)):
                res += word1[i]
                res += word2[i]
            return res + word1[len(word2):]


s = Solution()
print(s.mergeAlternately(word1="abc", word2="pqr"))
print(s.mergeAlternately(word1="ab", word2="pqrs"))
print(s.mergeAlternately(word1="abcd", word2="pq"))
