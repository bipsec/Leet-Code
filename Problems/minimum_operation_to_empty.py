class Solution:
    def minOperations(self, nums):

        dupes = {}

        for i in range(len(nums)):
            if nums[i] in dupes:
                dupes[nums[i]] += 1
            else:
                dupes[nums[i]] = 1
        ans = 0
        for item in list(dupes.values()):
            if item == 1:
                return -1
            ans += (item + 2) // 3
        return ans


s = Solution()
print(s.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(s.minOperations(nums=[2, 1, 2, 2, 3, 3]))
