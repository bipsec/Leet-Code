class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        seen = {}

        for index, ch in enumerate(s):
            seen[ch] = index
        # print(seen)

        for i, ch in enumerate(s):
            if ch not in stack:
                while stack and ch < stack[-1] and i < seen[stack[-1]]:
                    stack.pop()
                stack.append(ch)

        return "".join(stack)


s = Solution()
# print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))