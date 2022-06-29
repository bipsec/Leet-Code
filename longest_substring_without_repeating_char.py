class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        count = 0
        start = 1
        global_max = float("-inf")
        stack.append(s[0])

        for i in range(1, len(s)):
            # print(s[i])
            if stack[-1] != s[i] and s[i] not in stack:
                stack.append(s[i])
                count += 1
            elif stack[-1] == s[i]:
                stack.pop()
                count = 0
            if count > global_max:
                global_max = max(count, global_max)
        return global_max+1, stack







s = Solution()
print(s.lengthOfLongestSubstring("abcabcaa"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("bbbb"))
print(s.lengthOfLongestSubstring("aaabcd"))
print(s.lengthOfLongestSubstring("akldunp"))

