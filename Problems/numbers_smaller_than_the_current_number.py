class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        res = {}
        dupes = []

        for key, value in enumerate(sorted(nums)):
            if value not in res:
                res[value] = key
        # print(res)

        for i in nums:
            dupes.append(res[i])
        return dupes


s = Solution()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(s.smallerNumbersThanCurrent([6, 5, 4, 8]))
print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))
