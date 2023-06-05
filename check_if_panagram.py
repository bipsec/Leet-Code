class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dupes = {}

        for i in range(len(sentence)):
            if sentence[i] not in dupes:
                dupes[sentence[i]] = 1
            dupes[sentence[i]] += 1

        alphabets = list(map(chr, range(97, 123)))

        if len(sentence) >= 26:
            for i in alphabets:
                if i not in dupes.keys():
                    return False
            return True
        else:
            return False


s = Solution()
print(s.checkIfPangram(sentence="leetcode"))
print(s.checkIfPangram(sentence="a"))
print(s.checkIfPangram(sentence="levaniurejpefmaefcwrehgfvnaoweirmaiwehvvnrhqonewe"))
print(s.checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram(sentence="thequickbrownfoxjlloppwwssjjkpsoverthelazydog"))
