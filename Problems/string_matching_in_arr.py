class Solution:
    def stringMatching(self, words):
        ans = set()
        for x in words:
            for y in words:
                if x != y and x in y:
                    ans.add(x)
        return list(ans)


s = Solution()
print(s.stringMatching(words=["mass", "as", "hero", "superhero"]))
print(s.stringMatching(words=["leetcode", "et", "code"]))
print(s.stringMatching(words=["blue", "green", "bu"]))
