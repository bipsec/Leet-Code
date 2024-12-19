class Solution:

    def intersection(self, lst1, lst2):
        return [value for value in lst1 if value in lst2]

    def twoOutOfThree(self, nums1, nums2, nums3):
        arr = self.intersection(set(nums1), set(nums2))
        arr2 = self.intersection(set(nums2), set(nums3))
        arr3 = self.intersection(set(nums1), set(nums3))

        for item in arr2:
            if item not in arr:
                arr.append(item)

        for item in arr3:
            if item not in arr:
                arr.append(item)

        return arr





s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
print(s.twoOutOfThree(nums1=[1, 2], nums2=[4, 3, 3, 3], nums3=[5, 8, 9, 1, 2, 3, 4, 5, 6]))
print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
