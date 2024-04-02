class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictForS = {}
        dictForT = {}

        for i in range(len(s)):
            if s[i] in dictForS and dictForS[s[i]] != t[i]:
                return False
            if t[i] in dictForT and dictForT[t[i]] != s[i]:
                return False
            dictForS[s[i]] = t[i]
            dictForT[t[i]] = s[i]
        return True



