class Solution:
    def getCommon(self, nums1, nums2) -> int:
        common_nums = []
        dupes = {}

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                dupes[nums1[i]] = "from-1"
            else:
                common_nums.append(nums1[i])
        print(dupes)
        print(common_nums)


s = Solution()
# print(s.getCommon(nums1=[1, 2, 3], nums2=[2, 4]))
# print(s.getCommon(nums1=[1, 2], nums2=[4, 2, 3, 4, 5, 6]))
# print(s.getCommon(nums1=[1, 1], nums2=[1, 1, 2, 3]))
# print(s.getCommon(nums1=[-1, 1], nums2=[1, 1, 2, 3]))

