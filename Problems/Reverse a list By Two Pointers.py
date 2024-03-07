class Solution:
    def reverseString(self, nums):
        start,end = 0, len(nums)-1
        while start< end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        return nums


s = Solution()
print(s.reverseString(["h","e","l","l","o"]))