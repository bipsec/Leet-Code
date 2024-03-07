import collections
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen = defaultdict(int)
        dupes = defaultdict(int)

        for i in range(len(s)):
            seen[s[i]] += 1
            dupes[t[i]] += 1

        for key in seen:
            if seen[key] != dupes[key]:
                return False
        return True




s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("nameless", "salesman"))
print(s.isAnagram("aacc", "ccac"))
print(s.isAnagram("rat", "car"))
