class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += i
            if ans > n:
                print(ans-1)

        # print(ans)







s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))