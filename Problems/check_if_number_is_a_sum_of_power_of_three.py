class Solution:

    def subArraySum(self, numbers, target, index=0, current_sum=0):
        if current_sum == target:
            return True
        if index >= len(numbers):
            return False

        return self.subArraySum(numbers, target, index + 1, current_sum + numbers[index]) or \
            self.subArraySum(numbers, target, index + 1, current_sum)

    def checkPowersOfThree(self, n: int) -> bool:
        res = []
        for i in range(0, 17):
            res.append(3 ** i)

        ans = self.subArraySum(res, n, 0, 0)
        return ans


s = Solution()
print(s.checkPowersOfThree(12))
print(s.checkPowersOfThree(91))
print(s.checkPowersOfThree(21))
print(s.checkPowersOfThree(27))
print(s.checkPowersOfThree(7627))
