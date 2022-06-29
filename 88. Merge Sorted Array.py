class Solution:
    def merge(self, nums1, m, nums2, n):
        # nums1 = nums1[:m]
        nums2 = nums2[:n]
        nums1 = nums1[:m+n-1]
        print(nums1)


s = Solution()
print(s.merge([0], 0, [1], 1))
