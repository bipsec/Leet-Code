class Solution:
    def sumOfUnique(self, nums) -> int:
        dupes = {}

        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes[nums[i]] = 1
            else:
                dupes[nums[i]] += 1
        res = 0
        if len(nums) == 1:
            return nums[0]
        else:
            for key, val in dupes.items():
                if len(dupes) > 1:
                    if val == 1:
                        res += key
            return res


s = Solution()
print(s.sumOfUnique(nums=[1, 2, 3, 2]))
print(s.sumOfUnique(nums=[1, 1, 1, 1, 1]))
print(s.sumOfUnique(nums=[1, 2, 3, 4, 5]))
print(s.sumOfUnique(nums=[2, 2, 2, 2, 2]))
print(s.sumOfUnique(nums=[10]))
print(s.sumOfUnique(nums=[72, 72, 72, 72, 72, 72, 72, 72, 72, 72]))
