class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        result = 0
        end = len(prices)-1
        start = 0

        for i in range(end, 0, -1):
            if start < i:
                temp = prices[i] - prices[start]
                print(temp)
                result = max(temp, result)
                start += 1
        i -= 1

        return result


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
# print(s.maxProfit([7, 1, 5, 3, 6, 4, 8, 9, 11, 12]))
# print(s.maxProfit([7, 6, 4, 3, 1]))
# print(s.maxProfit([7, 1]))
