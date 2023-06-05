from collections import Counter


class Solution:
    def frequencySort(self, nums):
        dupes = Counter(nums).most_common()
        dupes.sort(key=lambda x: x[0], reverse=True)
        dupes.sort(key=lambda x: x[1])
        ans = []
        for i in dupes:
            a, b = i
            ans.extend([a] * b)
        return ans


s = Solution()
print(s.frequencySort(nums=[1, 1, 2, 2, 2, 3]))
print(s.frequencySort(nums=[2, 3, 1, 3, 2]))
print(s.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
