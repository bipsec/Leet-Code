class Solution:
    def findDuplicates(self, nums):
        seen = set()

        dupes = []

        for x in nums:
            if x in seen:
                dupes.append(x)
            else:
                seen.add(x)
        return dupes


s = Solution()
print(s.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
