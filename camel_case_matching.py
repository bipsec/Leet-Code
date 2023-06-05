class Solution:
    def isOkay(self, elem: str, pat):
        getUpperCaseValue = ""
        for val in elem:
            if val.isupper():
                getUpperCaseValue += val
        if len(getUpperCaseValue) == 2 and getUpperCaseValue[0] == pat[0] and getUpperCaseValue[1] == pat[1]:
            return True
        return False

    def camelMatch(self, queries, pattern):
        res = []
        for item in queries:
            if self.isOkay(item, pattern):
                res.append("True")
            else:
                res.append("False")

        return res


s = Solution()
print(s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
print(s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa"))
