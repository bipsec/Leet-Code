class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        dupes = {}
        count = 0
        start, end = 0, len(brokenLetters) - 1
        while start <= end:
            for i in range(len(text)):
                if brokenLetters[start] not in text[i]:
                    dupes[text[i]] = 1
                start += 1
        print(dupes)


s = Solution()
print(s.canBeTypedWords(text="hello world i would Like to know the details about the recent event organized by the foundation", brokenLetters="adsfgjkpiuytrwqzxcvbnm"))
