class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for item in sentence:
            if item[0:len(searchWord)] == searchWord:
                return sentence.index(item) + 1
        return -1


s = Solution()
print(s.isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))
print(s.isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro"))
print(s.isPrefixOfWord(sentence="i am tired", searchWord="you"))
