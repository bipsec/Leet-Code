class Solution:

    def get_diff(self, arr):
        max_diff = 0
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff > max_diff:
                max_diff = diff

        return max_diff

    def maximumGap(self, nums):
        nums.sort()
        n = len(nums)

        if len(nums) < 2:
            return 0
        else:
            left_part = nums[:n // 2 + 1]
            right_part = nums[n // 2:]
            left_diff = self.get_diff(left_part)
            right_diff = self.get_diff(right_part)

            if left_diff > right_diff:
                return left_diff
            return right_diff




s = Solution()
print(s.maximumGap(nums=[3, 6, 9, 1]))
print(s.maximumGap(nums=[10]))
print(s.maximumGap(nums=[1, 3, 100]))

# https://leetcode.com/problems/maximum-gap/submissions/1316044880/
