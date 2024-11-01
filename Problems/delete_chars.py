class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # print(s[i], "---", s[i-1])
                count += 1
                if count < 3:
                    # print("OK")
                    ans += s[i]
                # print(stack)
            else:
                count = 1
                ans += s[i]

        return ans


s = Solution()
print(s.makeFancyString(s="leeetcode"))
print(s.makeFancyString(s="aaabaaaa"))
