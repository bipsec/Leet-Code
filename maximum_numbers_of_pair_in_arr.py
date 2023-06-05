class Solution:
    def numberOfPairs(self, nums):
        dupes = {}
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes[nums[i]] = 1
            else:
                dupes[nums[i]] += 1

        pass
    # it's  an easy problem, I will do this on my next attempt.


s = Solution()
print(s.numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2]))
print(s.numberOfPairs(nums=[1, 1]))
print(s.numberOfPairs(nums=[0]))
print(s.numberOfPairs(nums=[-1, -2, -3]))
print(s.numberOfPairs(nums=[1, 2, 3]))
