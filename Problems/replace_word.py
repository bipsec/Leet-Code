class Solution:
    def check_and_replace(self, text, table):
        for key in range(len(table)):
            length = len(table[key])
            if table[key] == text[:length]:
                return table[key]
        return text

    def replaceWords(self, dictionary, sentence):
        dictionary.sort()
        sentence = sentence.split()
        res = ""
        for item in range(1, len(sentence)+1):
            res += self.check_and_replace(sentence[item-1], dictionary)
            res += " "
        return res.strip()


s = Solution()
print(s.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
print(s.replaceWords(dictionary=["catt","cat","bat","rat"], sentence="the cattle was rattled by the battery"))
print(s.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
# print(s.check_and_replace("the", ["cat", "bat", "rat"]))
# print(s.check_and_replace("cattle", ["cat", "bat", "rat"]))
# print(s.check_and_replace("was", ["cat", "bat", "rat"]))
# print(s.check_and_replace("rattled", ["cat", "bat", "rat"]))
