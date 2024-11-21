class Solution:
    def isBalanced(self, num: str) -> bool:
        ans = 0
        for i in range(len(num) - 1, -1, -1):
            if i % 2 != 0:
                ans += int(num[i])
            else:
                ans -= int(num[i])

        return ans == 0


s = Solution()
print(s.isBalanced(num="1234"))
print(s.isBalanced(num="24123"))
