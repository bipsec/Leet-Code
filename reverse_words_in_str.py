class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join([i for i in words][::-1])






s = Solution()
print(s.reverseWords("Hello World"))
print(s.reverseWords("  fly me   to   the moon "))
print(s.reverseWords("luffy is still joyboy"))
print(s.reverseWords("I love to code on leetcode"))
