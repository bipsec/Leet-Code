class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        dupes = {}
        for i, j in enumerate(nums):
            if j in dupes and i - dupes[j] <= k:
                return True
            dupes[j] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))

