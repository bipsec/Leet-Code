from collections import Counter


class Solution:
    def similarPairs(self, words) -> int:
        for i in range(len(words)):
            words[i] = set(words[i])
        count = 0
        words.sort()
        # print(set(words))
        for i in range(1, len(words)):
            if words[i-1] == words[i]:
                count += 1
        print(count)

        # return len(words) % getLength
#  need to solve this on my next attempt
# this is an easy problem --- '__' >__<


s = Solution()
print(s.similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"]))
print(s.similarPairs(words=["aabb", "ab", "ba"]))
