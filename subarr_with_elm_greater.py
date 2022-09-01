class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:

        # nums.sort()
        dupes = []
        # print(nums)
        c = 1
        for i in range(len(nums)-1, -1, -1):
            val = threshold / c
            if nums[i] > val:
                return c
            c += 1
        return -1


s = Solution()
print(s.validSubarraySize([1, 3, 4, 3, 1], 6))
print(s.validSubarraySize([6, 5, 6, 5, 8], 7))
# print(s.validSubarraySize([2, 3, 4, 5, 7], 10))
# print(s.validSubarraySize([1, 0], 1))
# print(s.validSubarraySize([1234, 1100, 1456, 879], 5))
print(s.validSubarraySize([818, 232, 595, 418, 608, 229, 37, 330, 876, 774, 931, 939, 479, 884, 354, 328], 3790))
