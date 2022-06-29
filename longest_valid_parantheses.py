class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start, end = 0, 0
        maxlength = 0

        for i in range(len(s)):
            if s[i] == "(":
                start += 1
            else:
                end += 1
            if end == start:
                maxlength = max(maxlength, start * 2)
            elif end > start:
                start = end = 0
        start = end = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                start += 1
            else:
                end += 1
            if start == end:
                maxlength = max(maxlength, start * 2)
            elif start > end:
                start = end = 0
        return maxlength



s = Solution()
print(s.longestValidParentheses("(((()))"))
print(s.longestValidParentheses("(((()))()))"))
print(s.longestValidParentheses(")((()))()))()))"))
print(s.longestValidParentheses(""))
