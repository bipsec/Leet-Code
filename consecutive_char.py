class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        ans = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                res += 1
            else:
                res = 1
            ans = max(res, ans)

        return ans


s = Solution()
print(s.maxPower("leetcode"))
print(s.maxPower("abbcccddddeeeeedcba"))
print(s.maxPower("abbccccccc"))
print(s.maxPower("counttheconsecutive"))
