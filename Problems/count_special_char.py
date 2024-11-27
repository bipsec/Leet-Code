class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        dupes = {}
        seen = set()
        for i in range(len(word)):
            char = word[i]
            if char.isalpha():
                other_case = char.swapcase()
                if other_case in seen:
                    dupes[char] = other_case
                if other_case not in seen:
                    seen.add(char)
        return len(dupes)


s = Solution()
print(s.numberOfSpecialChars(word="aaAbcBC"))
print(s.numberOfSpecialChars(word="abc"))
print(s.numberOfSpecialChars(word="abBCab"))
print(s.numberOfSpecialChars(word="Cc"))
print(s.numberOfSpecialChars(word="aaAbcBCvvb"))