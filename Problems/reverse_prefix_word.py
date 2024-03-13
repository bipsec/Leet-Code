class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        rev = ""
        if ch not in word:
            return word
        else:
            index = word.index(ch) + 1
            prefix = word[:index]
            return prefix[::-1] + word[index:]
            




s =Solution()
print(s.reversePrefix(word = "abcdefd", ch = "d"))
print(s.reversePrefix(word = "xyxzxe", ch = "z"))
print(s.reversePrefix(word = "abcd", ch = "z"))
print(s.reversePrefix(word = "abcd", ch = "d"))
print(s.reversePrefix(word = "abcd", ch = "c"))
print(s.reversePrefix(word = "aa", ch = "A"))