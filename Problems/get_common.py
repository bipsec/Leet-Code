class Solution:
    def getCommon(self, nums1, nums2) -> int:

        common_nums = list(set(nums1) & set(nums2))
        return -1 if len(common_nums) < 1 else min(common_nums)
    
    
        
    
    
    
         

        
        




s = Solution()
print(s.getCommon(nums1 = [1,2,3], nums2 = [2,4]))
