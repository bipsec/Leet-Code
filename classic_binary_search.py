from operator import truediv


class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums)


        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right =  mid
            else:
                left = mid + 1 
        return left
        



s = Solution()
print(s.binarySearch([1,3,5,6],2))