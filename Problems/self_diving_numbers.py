class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        res = []

        for i in range(left, right + 1):
            num = i
            flag = True

            while num > 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    flag = False
                    break
                num //= 10

            if flag:
                res.append(i)

        return res


s = Solution()
print(s.selfDividingNumbers(left=1, right=22))
print(s.selfDividingNumbers(left=47, right=85))
print(s.selfDividingNumbers(left=66, right=708))
