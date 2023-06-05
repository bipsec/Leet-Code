class Solution:

    def countMatches(self, items, ruleKey, ruleValue):
        res = 0
        dict = {"type": 0, "color": 1, "name": 2}
        for i in items:
            if i[dict[ruleKey]] == ruleValue:
                res += 1
        return res


s = Solution()
print(s.countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                     ruleKey="color",
                     ruleValue="silver"))
print(s.countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                     ruleKey="type", ruleValue="phone"))
