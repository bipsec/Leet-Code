class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []

        for i in range(1, len(temperatures)):
            count = 0
            c = 0
            if temperatures[i - 1] < temperatures[i]:
                count += 1
            res.append(count)

        print(res)


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 40, 50, 60]))
print(s.dailyTemperatures([30, 60, 90]))
