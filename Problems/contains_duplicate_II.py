class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:

        dupes = sorted(range(len(nums)), key=lambda i: nums[i])
        nums = [nums[i] for i in dupes]
        start, end = 0, 1

        while end < len(nums):
            if diff := nums[end] - nums[start] <= t:
                if abs(nums[start] - nums[end]) <= k:
                    return True
                end += 1
            else:
                start += 1
                end = start + 1
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([0], 0, 0))
print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
