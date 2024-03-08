class Solution:

    def reverse(self,start, end, arr):
        res = []
        for i in range(start, len(arr)):
            while start < end:
                res.append(arr[start])
                start -= 1
        print(res)
        return res



    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        res = nums[-k:]
        init = nums[0:k+1]
        nums = res + init
        
        
        return nums



s = Solution()
print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(s.rotate(nums = [-1,-100,3,99], k = 2))