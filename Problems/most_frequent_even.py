class Solution:
    def mostFrequentEven(self, nums) -> int:
        nums.sort()
        dupes = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in dupes:
                    dupes[nums[i]] += 1
                else:
                    dupes[nums[i]] = 1

        for key, value in dupes.items():
            res = max(dupes.values())
            if res == value:
                return key
        return -1


s = Solution()
print(s.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]))
print(s.mostFrequentEven(nums=[4, 4, 4, 9, 2, 4]))
