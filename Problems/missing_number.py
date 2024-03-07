class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        res = set()

        for i in range(0, len(nums)):
            res.add(nums[i])
        # print(res)
        for i in range(0, len(nums)+1):
            if i not in res:
                return i




s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))