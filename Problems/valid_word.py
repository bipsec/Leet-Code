class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiouAEIOU"
        special_chars = "[@_!#$%^&*()<>?/\|}{~:]"

        if len(word) < 3:
            return False
        else:
            flag = True
            has_vowel = False
            has_consonant = False
            for i in range(len(word)):
                if word[i] in vowels:
                    has_vowel = True
                elif word[i].isalpha():
                    has_consonant = True

                if not word[i].isalpha() and not word[i].isdigit():
                    if word[i] in special_chars:
                        flag = False
            return flag and has_vowel and has_consonant


s = Solution()
print(s.isValid(word="234Adas"))
print(s.isValid(word="b3"))
print(s.isValid(word="a3$e"))
print(s.isValid(word="abe"))
print(s.isValid(word="3pp"))
