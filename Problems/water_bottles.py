class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            ans += numBottles // numExchange
            numBottles = numBottles // numExchange + (numBottles % numExchange)

        return ans


s = Solution()
print(s.numWaterBottles(numBottles=9, numExchange=3))
print(s.numWaterBottles(numBottles=15, numExchange=4))
print(s.numWaterBottles(numBottles=2, numExchange=2))


