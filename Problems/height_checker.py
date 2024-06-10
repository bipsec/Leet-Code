class Solution:
    def heightChecker(self, heights) -> int:
        values = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if values[i] != heights[i]:
                count += 1

        return count


s = Solution()
print(s.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
print(s.heightChecker(heights=[5, 1, 2, 3, 4]))
print(s.heightChecker(heights=[1, 2, 3, 4, 5]))
