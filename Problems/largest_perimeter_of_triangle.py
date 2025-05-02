class Solution:
    def largestPerimeter(self, nums) -> int:

        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0


s = Solution()
print(s.largestPerimeter(nums=[2, 1, 2]))
print(s.largestPerimeter(nums=[1, 2, 1, 10]))
print(s.largestPerimeter(nums=[3,2,3,4]))
