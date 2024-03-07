class Solution:
    def joinStr(self, st):
        ans = "".join(i for i in st)
        # for i in range(len(st)):
        #     ans += st[i]
        return ans

    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return self.joinStr(word1) == self.joinStr(word2)


s = Solution()
print(s.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(s.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(s.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))
