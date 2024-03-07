from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        dupes = defaultdict()
        pass


s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
print(s.twoOutOfThree(nums1=[1, 2], nums2=[4, 3, 3], nums3=[5, 8, 9, 1, 2, 3, 4, 5, 6]))
