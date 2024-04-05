class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for char in s:
            if stack and stack[-1] == char.swapcase():
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


s = Solution()
print(s.makeGood(s="leEeetcode"))
print(s.makeGood(s="s"))
print(s.makeGood(s="abBAcC"))
