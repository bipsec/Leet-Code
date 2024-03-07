class Solution:
        def game(self, nums, count):
            newnums = []
            n = len(nums) - 1
            count = 0

            i = 0
            while i < n:
                if count % 2 == 0:
                    newnums.append(min(nums[i], nums[i + 1]))
                else:
                    newnums.append(max(nums[i], nums[i + 1]))
                count += 1
                i += 2
            return newnums

        def minMaxGame(self, nums: list[int]) -> int:
            count = len(nums) // 2
            while count > 0:
                nums = self.game(nums, count)
                count = len(nums) // 2

            return nums[0]


s = Solution()
# print(s.minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]))
print(s.minMaxGame([1, 5, 7, 6, 7, 2, 1, 9]))
print(s.minMaxGame([9, 5, 7, 6, 7, 1, 7, 0]))
# print(s.minMaxGame([1]))