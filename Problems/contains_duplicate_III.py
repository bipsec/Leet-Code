from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:

        if t < 0:
            return False

        window = SortedList()

        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])

            pos1 = window.bisect_left(num - t)
            pos2 = window.bisect_right(num + t)

            if pos1 != pos2 and pos1 != len(window):
                return True

            window.add(num)

        return False


# not mine

s = Solution()
print(s.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
