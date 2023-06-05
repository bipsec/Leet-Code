class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandy = max(candies)

        for i in range(len(candies)):
            addExtra = candies[i] + extraCandies
            if addExtra >= maxCandy:
                candies[i] = True
            else:
                candies[i] = False
        return candies


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(s.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
