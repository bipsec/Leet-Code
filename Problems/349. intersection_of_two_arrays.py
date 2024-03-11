class Solution:
    def intersection(self, nums1, nums2):
        dupes = {}
        res = []

        for i in range(len(nums1)):
            dupes[nums1[i]] = dupes.get(nums1[i], 0) + 1
        
        for num in set(nums2):
            if num in dupes:
                res.append(num)
            
        return res




s = Solution()
print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))