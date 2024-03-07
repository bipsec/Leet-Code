class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        cnt = 0

        for item in nums:
            if item - 1 in nums:
                continue
            c = 1
            while item + c in nums:
                c += 1
            cnt = max(cnt, c)
        return cnt


s = Solution()
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([]))
print(s.longestConsecutive([-1, -4, -6, 5, 8, 9, 10]))
print(s.longestConsecutive([-1, 0, 1]))
print(s.longestConsecutive([0]))
print(s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
