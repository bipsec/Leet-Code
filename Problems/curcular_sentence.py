class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        flag = True
        if len(sentence) <= 1:
            return sentence[0][0] == sentence[0][-1]
        else:
            if sentence[0][0] != sentence[-1][-1]:
                return False
            else:
                for i in range(1, len(sentence)):
                    if sentence[i - 1][-1] != sentence[i][0]:
                        flag = False
            return flag


s = Solution()
# print(s.isCircularSentence(sentence="leetcode exercises sound delightful"))
print(s.isCircularSentence(sentence="eetcode"))
# print(s.isCircularSentence(sentence="Leetcode is cool"))
print(s.isCircularSentence(sentence="leetcode"))
