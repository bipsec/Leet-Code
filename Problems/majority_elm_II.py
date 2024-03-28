class Solution:
    def majorityElement(self, nums):
        candidate = -1
        count = 0
        n = len(nums) // 3
        votes = 0
        for i in range(n):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if nums[i] == candidate:
                    votes += 1
                else:
                    votes -= 1

        for i in range(n):
            if nums[i] == candidate:
                count += 1

        if count > n // 3:
            return [candidate]
        else:
            return nums



# not solved
s = Solution()
print(s.majorityElement(nums=[3, 2, 3]))
print(s.majorityElement(nums=[1]))
print(s.majorityElement(nums=[1, 2]))
print(s.majorityElement(nums=[2, 2]))
