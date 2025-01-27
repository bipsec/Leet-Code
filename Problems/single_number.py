class Solution:
    def singleNumber(self, nums) -> int:

        dupes = {}
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes[nums[i]] = 1
            else:
                dupes[nums[i]] += 1

        for key, val in dupes.items():
            if val == 1:
                return key


s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 1, 2, 1, 2]))
print(s.singleNumber([1]))
