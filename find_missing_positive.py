class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        res = set()

        for i in range(0, len(nums)):
            res.add(nums[i-1])
            # print(res)
        for j in range(1, len(res)+1):
            if j not in res:
                return j
        return j+1
        

s = Solution()
# print(s.firstMissingPositive([1,2,0]))
# print(s.firstMissingPositive([3,4,-1,1]))
# print(s.firstMissingPositive([7,8,9,11,12]))
# print(s.firstMissingPositive([1]))
# print(s.firstMissingPositive([0]))
# print(s.firstMissingPositive([2]))
print(s.firstMissingPositive([2, 1]))
# print(s.firstMissingPositive([2, 2]))
