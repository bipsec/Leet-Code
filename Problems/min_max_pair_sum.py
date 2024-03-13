class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        maxNum = float('-inf')
        start, end = 0, len(nums) - 1
        
        while start <= end:
            val = nums[start] + nums[end]
            if val > maxNum:
                maxNum = val
            start += 1
            end -= 1

        return maxNum




s = Solution()
# print(s.minPairSum(nums = [3,5,2,3]))
# print(s.minPairSum(nums = [3,5,4,2,4,6]))
print(s.minPairSum(nums = [2,1,5,9,2,1,4,5]))