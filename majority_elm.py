class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        item, count = nums[0], 1

        for num in nums[1:]:
            if num != item:
                count -= 1
                if count == 0:
                    item = num
                    count = 1
            else:
                count += 1
        return item


s = Solution()
# print(s.majorityElement([3,3,4]))
# print(s.majorityElement([3,2,3]))
print(s.majorityElement([6,5,5]))
# print(s.majorityElement([2,2,1,1,1,2,2]))
