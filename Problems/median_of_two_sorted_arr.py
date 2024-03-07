class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        return (nums[len(nums) // 2] + nums[(len(nums) // 2)-1]) / 2

    # m, n = len(nums1), len(nums2)
    # nums = nums1[:m]
    # nums += nums2[:n]
    # nums.sort()
    #
    # if len(nums) % 2 != 0:
    #     mid = len(nums) // 2
    #     res = nums[mid]
    #
    # else:
    #     mid = len(nums) // 2
    #     res = (nums[mid] + nums[mid - 1]) / 2
    # return res


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
