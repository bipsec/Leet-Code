class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        

        # dupes = []

        # for i in range(0, len(nums1)):
        #     if nums1[i] in nums2 and nums1[i] not in dupes:
        #         dupes.append(nums1[i])
        return set(nums1).intersection(set(nums2))












        while start < len(nums1) and end < len(nums2):
            if nums1[start] < nums2[end]:
                start += 1

            elif nums1[start] > nums2[end]:
                end += 1

            elif nums1[start] == nums2[end]:

                if nums1[start] not in seen:
                    # seen[new] = nums1[start]
                    dupes.append(nums1[start])
                    # new += 1

                else:
                    seen[new] = nums1[start]

                start += 1
                end += 1

        return dupes


s = Solution()
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(s.intersection([1, 2, 2, 1], [2, 2]))
