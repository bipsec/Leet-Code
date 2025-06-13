class Solution:

    def checker(self, nums, days):
        res = []
        for i in range(1, days + 1):
            if i not in range(nums[0], nums[1] + 1):
                res.append(i)

        return res

    def countDays(self, days: int, meetings) -> int:
        res = []
        for items in meetings:
            res.append(self.checker(items, days))

        ans = set(res.pop()).intersection(*map(set, res))

        return len(ans)



s = Solution()
print(s.countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]))
print(s.countDays(days=5, meetings=[[2, 4], [1, 3]]))
print(s.countDays(days=6, meetings=[[1, 6]]))
