class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        product = 1
        result = 0
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            product *= nums[i]
            result = max(result, product)
            if nums[i] == 0:
                product = 1
        product = 1

        for i in range(len(nums)-1,-1, -1):
            product *= nums[i]
            result = max(result, product)
            if nums[i] == 0:
                product = 1

        return result


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([2, -5, -2, -4, 3]))
