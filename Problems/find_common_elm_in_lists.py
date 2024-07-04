class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count, count_1 = 0, 0
        for item in nums1:
            if item in nums2:
                count += 1
        for item in nums2:
            if item in nums1:
                count_1 += 1

        return [count, count_1]
