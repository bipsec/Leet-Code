class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ")":
                res = []
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()
                stack.extend(res)
            else:
                stack.append(s[i])

        return ''.join(stack)


s = Solution()
print(s.reverseParentheses(s="(abcd)"))
print(s.reverseParentheses(s="(u(love)i)"))
