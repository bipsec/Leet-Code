class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s= ""
        res = []
        for i in range(len(word)):
            if word[i].isdigit():
                s += str(word[i])
            if word[i].islower():
                res.append(s)
                s = ""
        res.append(s)

        ans = []

        for item in res:
            if item != "" and int(item) not in ans:
                ans.append(int(item))

        return len(ans)


s = Solution()
print(s.numDifferentIntegers(word="a123bc34d8ef34"))
print(s.numDifferentIntegers(word="leet1234code234"))
print(s.numDifferentIntegers(word="a1b01c001"))
print(s.numDifferentIntegers(word="1111"))
