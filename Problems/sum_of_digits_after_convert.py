class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        for item in s:
            ans += str(ord(item)-96)

        while k > 0:
            res = 0
            for item in str(ans):
                res += int(item)
            ans = res
            k -= 1

        return ans


s = Solution()
print(s.getLucky(s="iiii", k=1))
print(s.getLucky(s="leetcode", k=2))
