# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, nums1,m, nums2, n):
        nums1[m:] = nums2

        for item in range(1, len(nums1)):
            key = nums1[item]
            j = item - 1
        
            while j >= 0 and key < nums1[j]:
                nums1[j + 1] = nums1[j]
                j = j - 1
            
            nums1[j + 1] = key
        return nums1


s = Solution()
print(s.mergeTwoLists([1,2,3, 0,0,0],3, [4,5,6], 3))
print(s.mergeTwoLists([1,2,4, 0, 0, 0],3, [1,3,4], 3))
