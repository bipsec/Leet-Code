class Solution:
    def countPairs2(self, nums, target: int) -> int:
        res = [(nums[i],nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums))]
        count = 0
        for item in res:
            if sum(item) < target:
                count += 1
        
        return count



s = Solution()
print(s.countPairs(nums = [-1,1,2,3,1], target = 2))
print(s.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))