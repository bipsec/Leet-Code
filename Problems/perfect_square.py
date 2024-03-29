import math


class Solution:
    def least_squares_sum(self, n):
        # claude AI
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                square = j ** 2
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

    def numSquares(self, n: int) -> int:
        # ChatGPT
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1

        return dp[n]



s = Solution()
print(s.numSquares(12))
print(s.least_squares_sum(12))