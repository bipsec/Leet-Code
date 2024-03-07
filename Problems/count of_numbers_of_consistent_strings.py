class Solution:
    def isOkay(self, letter, allowed):

        for i in range(len(letter)):
            if letter[i] not in allowed:
                return False
            else:
                continue
        return True

    def countConsistentStrings(self, allowed: str, words) -> int:
        count = 0
        for item in words:
            getRes = self.isOkay(item, allowed)
            if getRes:
                count += 1
        return count


s = Solution()
# print(s.isOkay("ad", "ab"))
# print(s.isOkay("bd", "ab"))
# print(s.isOkay("aaab", "ab"))
# print(s.isOkay("baa", "ab"))
# print(s.isOkay("badab", "ab"))
print(s.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(s.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(s.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
