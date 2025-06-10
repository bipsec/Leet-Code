class Solution:

    def check(self, item, words2):
        ans = []
        for i in range(len(words2)):
            # print(words2[i])
            if len(words2[i]) > 1:
                for j in range(len(words2[i])):
                    if words2[i][j] not in item:
                        ans.append(False)

            else:
                if words2[i] not in item:
                    ans.append(False)
            ans.append(True)

        if False in ans:
            return False
        else:
            return True

    def wordSubsets(self, words1, words2):
        res = []
        for i in range(len(words1)):
            val = self.check(words1[i], words2)
            if val:
                res.append(words1[i])
        return res


s = Solution()
print(s.wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"]))
print(s.wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["lc", "eo"]))
print(s.wordSubsets(words1=["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], words2=["c", "cc", "b"]))
print(s.wordSubsets(["aaaba", "aabcb", "cbcca", "abcca", "ccaca"], ["ac", "b", "b"]))  # ["aabcb","cbcca","abcca"]
