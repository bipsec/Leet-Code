class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        result = []

        for i in range(len(words)-1, -1, -1):
            result.append(len(words[i]))
        return result[0]


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("  fly me   to   the moon "))
print(s.lengthOfLastWord("luffy is still joyboy"))
print(s.lengthOfLastWord("I love to code on leetcode"))