class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        if num == 0:
            return True
        num = str(num)

        if num.endswith("0"):
            return False
        return True


        # if len(str(num)) == 1:
        #     return True
        # num2 = str(num)
        # res = val = ""
        #
        # for i in range(len(num2)-1, -1, -1):
        #     if num2[i] == 0:
        #         continue
        #     res += num2[i]
        # res = str(int(res))
        # for i in range(len(res)-1, -1, -1):
        #     val += res[i]
        #
        # return num == int(val)



s = Solution()
print(s.isSameAfterReversals(1215))
print(s.isSameAfterReversals(1800))
print(s.isSameAfterReversals(1801))
print(s.isSameAfterReversals(180009))
print(s.isSameAfterReversals(109))

