class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
