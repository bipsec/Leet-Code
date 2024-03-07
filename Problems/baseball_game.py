class Solution:
    def calPoints(self, ops: list[str]) -> int:

        stack = []

        for i in ops:
            if i == "D":
                stack.append(stack[-1] * 2)

            elif i == "C":

                stack.pop()
            elif i == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(i))

        return sum(stack)


s = Solution()
print(s.calPoints(["5", "2", "C", "D", "+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
print(s.calPoints(["1", "C"]))
