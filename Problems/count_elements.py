class Solution:
    def countElements(self, nums) -> int:
        nums.sort()
        a, b = nums[0], nums[-1]
        count = 0

        for i in range(len(nums)):
            if nums[i] != a and nums[i] != b:
                count += 1

        return count


s = Solution()
print(s.countElements([11, 7, 2, 15]))
print(s.countElements([-3, 3, 3, 90]))
print(s.countElements([11, 7, 2, 15, 23, 34]))
print(s.countElements([-71, -71, 93, -71, 40]))
