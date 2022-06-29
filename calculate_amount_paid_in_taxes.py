class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        res = 0
        elm = 0
        for a, b in brackets:
            res += (min(a, income) - elm) * (b/100)
            if a > income:
                break
            elm = a
        return res


s = Solution()
print(s.calculateTax([[3, 50], [7, 10], [12, 25]], 10))
# print(s.calculateTax([[2, 50]], 0))
