class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        count = 0

        for item in arr:
            if item % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True
        return False


s = Solution()
print(s.threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(s.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))
