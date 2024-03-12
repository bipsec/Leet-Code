
class Solution:
    def countNumbersWithUniqueDigits(self, n):

        def count(k):
            if k == max(10 - n, 0):
                return 0
            return k*(1 + count(k - 1))
        if n == 0:
            return 1
        return 9*count(9) + 10
    
    # not mine :(
         


s = Solution()
print(s.countNumbersWithUniqueDigits(2))
print(s.countNumbersWithUniqueDigits(0))
print(s.countNumbersWithUniqueDigits(3))
