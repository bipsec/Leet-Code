class Solution:
    def subArrayRanges(self, nums):

        res = 0
        n = len(nums)

        for i in range(n):
            min_element = nums[i]
            max_element = nums[i]
            for j in range(i, n):
                min_element = min(min_element, nums[j])
                max_element = max(max_element, nums[j])
                res += (max_element - min_element)

        return res


s = Solution()
print(s.subArrayRanges(nums=[1, 2, 3]))
