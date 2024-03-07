class Solution:
    def isHappy(self, n: int) -> bool:

        dupes = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in dupes:
                return False
            else:
                dupes.add(n)
        else:
            return True

    #     if n < 10:
    #         return False
    #     val = self.add(n)
    #     if val == 1:
    #         return True
    #     self.add(val)
    #     return False
    #
    # def add(self, n):
    #     result = 0
    #     num = str(n)
    #
    #     return result
    #

s = Solution()
print(s.isHappy(19))
print(s.isHappy(1))
print(s.isHappy(68))
print(s.isHappy(100))
