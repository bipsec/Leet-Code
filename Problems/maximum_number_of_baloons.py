class Solution:
    def counter(self, text):
        dupes = {}

        for i in range(len(text)):
            if text[i] not in dupes:
                dupes[text[i]] = 1
            else:
                dupes[text[i]] += 1

        return dupes

    def check_multiples(self, dict1, dict2):
        format = []

        for key in dict1.keys():
            val = dict1[key]
            if key not in dict2.keys():
                return 0
            else:
                val2 = dict2[key]
            # print(val, "====", val2)
            if val == 0:
                format.append(0)
            format.append(val2 // val)
        return min(format)

    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        res = self.counter(word)
        dupes = self.counter(text)

        val = self.check_multiples(res, dupes)
        return val



s = Solution()
print(s.maxNumberOfBalloons(text="nlaebolko"))
print(s.maxNumberOfBalloons(text="loonbalxballpoon"))
print(s.maxNumberOfBalloons(text="leetcode"))
print(s.maxNumberOfBalloons(text="vuiarweihomqwoefoiwyfiubalioauwernballonballonballoon"))
print(s.maxNumberOfBalloons(text="llllllllbbbbbbbbooooooonnnnnnnnnnnnnnnnnnnnnnnnnnnnnkkkkkkkkkkkkkllllllllllllllyyyyyoooooooooooooo"))
