class Solution:
    def isPossibleToSplit(self, nums) -> bool:
        
        nums.sort()

        firstArr = []
        secondArr = []

        for i in range(len(nums)):
            if i % 2 == 0:
                secondArr.append(nums[i])
            else:
                firstArr.append(nums[i])

        if len(set(firstArr)) != len(firstArr) or len(set(secondArr)) != len(secondArr):
            return False
        else:
            return True



s = Solution()
print(s.isPossibleToSplit(nums = [1,1,2,2,3,4]))
print(s.isPossibleToSplit(nums = [1,1,1,1,1,1]))
print(s.isPossibleToSplit(nums = [1,2]))
print(s.isPossibleToSplit(nums = [6,1,3,1,1,8,9,2]))