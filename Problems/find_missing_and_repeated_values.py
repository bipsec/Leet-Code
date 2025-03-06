class Solution:
    def findMissingAndRepeatedValues(self, grid):
        res = []

        for items in grid:
            for item in items:
                res.append(item)

        answer = [i for i in range(1, len(res) + 1)]

        ans = []
        dupes = []
        for i in range(1, len(res) + 1):
            if res[i - 1] not in ans:
                ans.append(res[i - 1])
            else:
                dupes.append(res[i - 1])

        for val in answer:
            if val not in res:
                dupes.append(val)

        return dupes


s = Solution()
print(s.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]))
print(s.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
