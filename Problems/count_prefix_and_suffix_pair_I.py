class Solution:

    def check(self, str1, str2):
        n = len(str1)
        if str1[:] == str2[:n] and str1[:] == str2[-n:]:
            return True
        return False

    def countPrefixSuffixPairs(self, words) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                checker = self.check(words[i], words[j])
                if checker:
                    count += 1

        return count


s = Solution()
print(s.countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"]))
print(s.countPrefixSuffixPairs(words=["pa", "papa", "ma", "mama"]))
print(s.countPrefixSuffixPairs(words = ["abab","ab"]))
