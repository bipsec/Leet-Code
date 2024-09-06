class Solution:
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #
    #     res = 1
    #     dupes = []
    #     for i in range(0, len(nums)):
    #         dupes.append(res)
    #         res = res * nums[i]
    #     res = 1
    #     # print(dupes)
    #     for i in range(len(nums) - 1, -1, -1):
    #         dupes[i] = dupes[i] * res
    #         res = res * nums[i]
    #     return dupes

    def productExceptSelf(self, nums):

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] *= nums[i - 1] * result[i - 1]

        res = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= res
            res *= nums[i]

        return result


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4, 5]))
# print(s.product([1, 2, 3, 4, 5]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
# print(s.product([-1, 1, 0, -3, 3]))
