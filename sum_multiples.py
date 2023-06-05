class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0

        for item in range(1, n+1):
            if item % 3 == 0 or item % 5 == 0 or item % 7 == 0:
                ans += item

        return ans


s = Solution()
print(s.sumOfMultiples(n=7))
print(s.sumOfMultiples(n=10))
print(s.sumOfMultiples(n=9))
