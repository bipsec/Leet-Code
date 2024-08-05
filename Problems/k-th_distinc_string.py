class Solution:
    def kthDistinct(self, arr, k):
        dupes = {}

        for item in arr:
            if item in dupes:
                dupes[item] += 1
            else:
                dupes[item] = 1
        count = 0
        for key, val in dupes.items():
            if val == 1:
                count += 1
            if count == k:
                return key

        return ""


s = Solution()
print(s.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2))
print(s.kthDistinct(arr=["aaa", "aa", "a"], k=1))
