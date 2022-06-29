class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
        return -1
        

s = Solution()
print(s.binarySearch([-1,0,2,3,4,6,9,5],9))
print(s.binarySearch([4,5,6,7,0,1,2], 0))
# print(s.binarySearch([-1, 0, 3, 5, 9, 12], 9))
# print(s.binarySearch([-1,0,3,5,9,12], 2))
# print(s.binarySearch([5], 5))