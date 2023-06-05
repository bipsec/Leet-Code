class Solution:
    def maximumWealth(self, accounts) -> int:
        getMax = 0

        for items in accounts:
            getSum = 0
            for val in items:
                getSum += val
            if getSum > getMax:
                getMax = getSum
        return getMax


s = Solution()
print(s.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(s.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
print(s.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
