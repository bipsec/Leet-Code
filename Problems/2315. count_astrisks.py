class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        stack = []

        for i in range(len(s)):
            if s[i] == "|":
                stack.append(s[i])
                if len(stack) == 2:
                    stack.clear()
            elif s[i] == "*" and len(stack) == 0:
                cnt += 1

        return cnt



s = Solution()
print(s.countAsterisks("l|*e*et|c**o|*de|"))
print(s.countAsterisks("iamprogrammer"))
print(s.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))