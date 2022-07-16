class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]
        res = []
        for e in nums:
            temp = nums[:]
            temp.remove(e)
            res.extend([[e] + r for r in self.permute(temp)])

        return res


s = Solution()
print(s.permute([1, 2, 3]))
