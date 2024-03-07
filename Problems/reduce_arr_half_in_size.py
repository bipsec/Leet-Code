from collections import Counter


class Solution:
    def minSetSize(self, arr) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()

        res, deleted, half = 0, 0, len(arr) // 2
        while deleted < half:
            res += 1
            deleted += frequencies.pop()
        return res


s = Solution()
print(s.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
