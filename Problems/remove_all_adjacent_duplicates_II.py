class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= k and all(stack[-1] == stack[-j - 1] for j in range(k)):
                for j in range(0, k):
                    stack.pop()

        return "".join(stack)

    def removeDuplicatesII(self, s: str, k: int) -> str:
        stack = []
        for elem in s:
            stack.append(elem)
            if len(stack) >= k and stack[-k:] == [elem] * k:
                stack = stack[:-k]
        return "".join(stack)


s = Solution()
print(s.removeDuplicates(s="abcd", k=2))
print(s.removeDuplicates(s="deeedbbcccbdaa", k=3))
print(s.removeDuplicates(s="pbbcggttciiippooaais", k=2))
print(s.removeDuplicatesII(s="abcd", k=2))
print(s.removeDuplicatesII(s="deeedbbcccbdaa", k=3))
print(s.removeDuplicatesII(s="pbbcggttciiippooaais", k=2))