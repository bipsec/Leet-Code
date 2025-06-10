from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:

        maxOdd = 0
        minEven = float('inf')
        count = Counter(s)
        for i in count:
            if count[i] % 2 == 0 and count[i] < minEven:
                minEven = count[i]
            elif count[i] % 2 != 0 and count[i] > maxOdd:
                maxOdd = count[i]
        return maxOdd - minEven


s = Solution()
print(s.maxDifference(s="aaaaabbc"))
print(s.maxDifference(s="abcabcab"))
