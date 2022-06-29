class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        res = nums[0]
        dupes = [nums[0]]

        for i in range(1, len(nums)):
            res += nums[i]
            dupes.append(res)

        return dupes


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))
