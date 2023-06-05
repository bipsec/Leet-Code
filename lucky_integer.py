from collections import defaultdict


class Solution:
    def findLucky(self, arr) -> int:
        dupes = {}
        getMax = float("-inf")
        for i in range(len(arr)):
            if arr[i] in dupes:
                dupes[arr[i]] += 1
            else:
                dupes[arr[i]] = 1
        # print(dupes)
        for key, val in dupes.items():
            if key == val:
                getMax = max(key, getMax)

        return -1 if getMax <= 0 else getMax


s = Solution()
print(s.findLucky(arr=[2, 2, 3, 4]))
print(s.findLucky(arr=[1, 2, 2, 3, 3, 3]))
print(s.findLucky(arr=[2, 2, 2, 3, 3]))
print(s.findLucky([4, 3, 2, 2, 4, 1, 3, 4, 3]))
