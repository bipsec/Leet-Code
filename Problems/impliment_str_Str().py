class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr(haystack="hello", needle="ll"))
print(s.strStr(haystack="aaaaa", needle="bba"))
print(s.strStr(haystack="aaaaa", needle=""))
print(s.strStr("aaa", "aaaa"))
print(s.strStr("aaa", "aab"))
print(s.strStr("aaaiiikkiii", "iiikk"))
print(s.strStr("lllllab", "abk"))
print(s.strStr("llilllab", "lllab"))
print(s.strStr("mississippi", "issip"))
