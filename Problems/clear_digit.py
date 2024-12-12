class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for item in s:
            if stack and item.isdigit():
                stack.pop()
            else:
                stack.append(item)

        return "".join(stack)


s = Solution()
print(s.clearDigits(s="cb34"))
print(s.clearDigits(s="abc"))
print(s.clearDigits(s="abc3"))
