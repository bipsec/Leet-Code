class Solution:
    def getSneakyNumbers(self, nums):
        res = []
        nums.sort()

        for item in range(len(nums)):
            if nums[item] == nums[item+1]:
                res.append(nums[item])
            if len(res) == 2:
                return res


s = Solution()
print(s.getSneakyNumbers(nums=[0, 1, 1, 0]))
print(s.getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2]))
print(s.getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
