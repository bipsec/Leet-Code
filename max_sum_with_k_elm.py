class Solution:
    def maximizeSum(self, nums, k):
        nums.sort()
        for i in range(k - 1):
            nums.append(nums[-1] + 1)
        return sum(nums[-k:])


s = Solution()
print(s.maximizeSum(nums=[1, 2, 3, 4, 5], k=3))
print(s.maximizeSum(nums=[5, 5, 5], k=2))
print(s.maximizeSum([1, 2, 6, 9, 2, 4, 5], k=3))
