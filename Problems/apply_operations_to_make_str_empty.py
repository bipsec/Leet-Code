class Solution:

    def lastNonEmptyString(self, s: str) -> str:

        dupes = {}
        for i in range(len(s)):
            if s[i] in dupes:
                dupes[s[i]] += 1
            else:
                dupes[s[i]] = 1
        md = []
        mx = max(dupes.values())
        for c in reversed(s):
            if mx == dupes[c]:
                md.append(c)
                dupes[c] -= 1
        return ''.join(md[:: -1])


s = Solution()
print(s.lastNonEmptyString(s="aabcbbca"))
print(s.lastNonEmptyString(s="abcd"))
