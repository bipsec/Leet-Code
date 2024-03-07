class Solution:
    def isValid(self, s: str) -> bool:

        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            if i in d.keys():
                if len(stack) == 0 or (d[i] != stack.pop()):
                    return False
        return len(stack) == 0


s = Solution()
# print(s.isValid("()"))
# print(s.isValid("()[]{}"))
# print(s.isValid("[({[({}]}}]"))
print(s.isValid("(]"))
