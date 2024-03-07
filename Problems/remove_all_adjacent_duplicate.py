class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa", 2))
print(s.removeDuplicates("pbbcggttciiippooaais", 3))
print(s.removeDuplicates("abbaca", 3))
