class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        if num == 0:
            return count

        while num != 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
            else:
                num = num - 1
                count += 1
        return count



s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))
