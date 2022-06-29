class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n ==2:
            return 2

        result = {}

        if n not in result:
            result[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return result[n]




s = Solution()
print(s.climbStairs(6))
