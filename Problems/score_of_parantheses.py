class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        flag = True
        for i in range(len(s)):
            if s[i] == "(":
                flag = True
                stack.append(s[i])
            elif s[i] == ")":
                if flag:
                    count += 2 ** (len(stack) - 1)
                    flag = False
                stack.pop()

        return count


s = Solution()
print(s.scoreOfParentheses(s="()"))
print(s.scoreOfParentheses(s="(()(()))"))

# print(s.scoreOfParentheses(s="(())"))
# print(s.scoreOfParentheses(s="()()"))
