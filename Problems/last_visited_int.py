class Solution:
    def lastVisitedIntegers(self, nums):
        seen = []
        ans = []
        k = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                seen.insert(0, nums[i])
            else:
                if k < len(seen) and nums[i - 1] == -1:
                    k += 1
                    ans.append(seen[k - 1])
                elif k < len(seen):
                    k = 1
                    ans.append(seen[0])
                else:
                    ans.append(-1)

        return ans


s = Solution()
print(s.lastVisitedIntegers(nums=[1, 2, -1, -1, -1]))
print(s.lastVisitedIntegers(nums=[1, -1, 2, -1, -1]))
