class Solution:
    def separateDigits(self, nums):
        res = "".join(str(i) for i in nums)
        return list(int(i) for i in res)





s = Solution()
print(s.separateDigits(nums=[13, 25, 83, 77]))
