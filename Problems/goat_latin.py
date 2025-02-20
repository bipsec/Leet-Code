class Solution:

    def toGoatLatin(self, sentence: str) -> str:
        res = ""
        vowels = "aeiouAEIOU"
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] in vowels:
                # print(sentence[i])
                new_word = sentence[i][:] + "ma" + "a" * (i + 1)
            else:
                new_word = sentence[i][1:] + sentence[i][0] + "ma" + "a" * (i + 1)
            res += new_word
            res += " "

        return res.strip()


s = Solution()
print(s.toGoatLatin(sentence="I speak Goat Latin"))
print(s.toGoatLatin(sentence="The quick brown fox jumped over the lazy dog"))
