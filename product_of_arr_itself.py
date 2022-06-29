class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = 1
        dupes = []
        for i in range(0, len(nums)):
            dupes.append(res)
            res = res * nums[i]
        res = 1
        print(dupes)
        for i in range(len(nums)-1, -1, -1):
            dupes[i] = dupes[i] * res
            res = res * nums[i]
        return dupes


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4, 5]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))


