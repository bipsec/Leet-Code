class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1.sort()
        nums2.sort()
        dupes = []

        start = end = 0

        while start < len(nums1) and end < len(nums2):
            if nums1[start] < nums2[end]:
                start += 1
            elif nums1[start] > nums2[end]:
                end += 1
            else:
                dupes.append(nums1[start])
                start += 1
                end += 1
        return dupes


s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))
