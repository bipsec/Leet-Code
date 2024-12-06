class Solution:
    def maxCount(self, banned, n: int, maxSum: int) -> int:

        # it gives TLE because it's iterating the whole array and making the sum unnecessary

        count = 0
        val = 0
        dupes = []

        for i in range(1, n + 1):
            if i not in banned:
                dupes.append(i)

        for i in range(len(dupes)):
            val += dupes[i]
            count += 1
            if val > maxSum:
                return count - 1
        return count

    def maxCount(self, banned, n: int, maxSum: int) -> int:     # good approach

        count = 0
        val = 0
        dupes = set(banned)

        for i in range(1, n + 1):
            if i not in dupes:
                if val + i > maxSum:
                    break
                val += i
                count += 1
        return count


s = Solution()
print(s.maxCount(banned=[1, 6, 5], n=5, maxSum=6))
print(s.maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1))
print(s.maxCount(banned=[11], n=7, maxSum=50))
