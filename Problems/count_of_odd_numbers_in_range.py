class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0 and high % 2 == 0:
            if (high - low) % 2 == 0:
                return (high - low) // 2
            else:
                return (high - low) // 2 + 1
        elif low % 2 == 1 and high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2


s = Solution()
print(s.countOdds(low=3, high=7))
print(s.countOdds(low=8, high=10))
