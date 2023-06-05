class Solution:
    def thirdMax(self, nums) -> int:
        unique_nums = sorted(set(nums), reverse=True)
        # print(unique_nums)

        if len(unique_nums) >= 3:
            return unique_nums[2]
        elif len(unique_nums) == 2:
            return unique_nums[0]
        else:
            return nums[0]


s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
