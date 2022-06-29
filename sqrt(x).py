class Solution:
    def mySqrt(self, x: int) -> int:

        # def isBadVersion(version: int) -> bool:
        #     pass

        left = 1
        right = x + 1

        while left < right:
            mid = left + (right-left)//2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left-1


s = Solution()
print(s.mySqrt(49))

''' Binary Search Problems:

Link: https: // towardsdatascience.com/powerful-ultimate-binary-search-template-and-many-leetcode-problems-1f850ef95651 '''
