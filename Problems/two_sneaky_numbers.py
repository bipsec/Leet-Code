class Solution:
    def getSneakyNumbers(self, nums):

        dupes = {}
        res = []

        for item in nums:
            if item not in dupes:
                dupes[item] = 1
            else:
                res.append(item)
        return res


s = Solution()
print(s.getSneakyNumbers(nums=[0, 1, 1, 0]))
print(s.getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2]))
print(s.getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
