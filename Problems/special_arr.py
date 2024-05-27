class Solution:
    def specialArray(self, nums):
        nums.sort()

        for item in range(len(nums)):
            n = len(nums) - item
            if (item == 0 or nums[item - 1] < n) and n <= nums[item]:
                return n
        return -1


s = Solution()
print(s.specialArray(nums=[3, 5]))
print(s.specialArray(nums=[0, 4, 3, 0, 4]))
print(s.specialArray([3, 6, 7, 7, 0]))
print(s.specialArray([0, 0]))
