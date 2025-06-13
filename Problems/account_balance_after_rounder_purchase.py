class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:

        flag = True

        while flag:
            if purchaseAmount <= 10:
                return 100 - 10
            else:
                pass


s = Solution()
print(s.accountBalanceAfterPurchase(9))
print(s.accountBalanceAfterPurchase(15))
print(s.accountBalanceAfterPurchase(10))
