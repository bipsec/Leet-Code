import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        ##### Approach 3 ###########

        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for i in range(0, len(s)):
            if seen[s[i]] == 1:
                return i
        return -1

        ##### Approach 1 ###########
        # counter = collections.Counter(s)
        # print(s)
        # print(counter)

        # for i in range(len(s)):
        #     if counter[s[i]] == 3:
        #         return i
        # return -1

        # for i, ch in enumerate(s):
        #     if counter[ch] == 3:
        #         return i
        # return -1
        ##### Approach 2--> Mine ###########

        # seen = {}
        # dupes = []
        #
        # for i in range(0, len(s)):
        #     if s[i] in seen:
        #         dupes.append(s[i])
        #     else:
        #         seen[s[i]] = i
        #
        # for key, value in seen.items():
        #     if key not in dupes:
        #         return value
        # return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
print(s.firstUniqChar("ajkaaaawqnnnhnjpowrqug"))
print(s.firstUniqChar("fffffffff"))

