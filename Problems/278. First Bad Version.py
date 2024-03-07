# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# from operator import truediv


class Solution:
    def firstBadVersion(self, n: int) -> int:

        def isBadVersion(version: int) -> bool:
            pass

        left = 1
        right = n
        # val = (5-4) // 2
        # print(val)

        while left < right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    









s = Solution()
print(s.firstBadVersion(5))