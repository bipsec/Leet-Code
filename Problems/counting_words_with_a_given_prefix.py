class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for i in range(len(words)):
            if words[i][:len(pref)] == pref:
                count += 1

        return count


s = Solution()
print(s.prefixCount(words=["pay", "attention", "practice", "attend"], pref="at"))
print(s.prefixCount(words=["leetcode", "win", "loops", "success"], pref="code"))
print(s.prefixCount(words=["aleetcode", "wain", "aaaaaaloops", "asuccess"], pref="aa"))
