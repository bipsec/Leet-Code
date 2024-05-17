class Solution:
    def vowelStrings(self, words, left, right):

        vowel = ["a", "e", "i", "o", "u"]
        count = 0
        for item in range(left, right + 1):
            if words[item][0] in vowel and words[item][-1] in vowel:
                count += 1
            left += 1
        return count


s = Solution()
print(s.vowelStrings(words=["are", "amy", "u"], left=0, right=2))
print(s.vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4))
