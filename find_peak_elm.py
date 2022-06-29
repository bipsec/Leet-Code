class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        left = 0
        right = left + 1

        if len(nums) < 4:
            return nums.index(max(nums))

        for i in range(0, len(nums)-1):

            if nums[left] < nums[right]:
                left += 1
                right += 1
            # elif nums[left]
        return right-1


s = Solution()
print(s.findPeakElement([1, 2, 1, 3, 4, 5, 6]))
# print(s.findPeakElement([1, 2, 3, 1]))
# print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
# print(s.findPeakElement([1, 3, 5, 6, 4]))
# print(s.findPeakElement([1]))
# print(s.findPeakElement([1, 0]))
# print(s.findPeakElement([1, 0, 3]))
# print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 3, 4]))
