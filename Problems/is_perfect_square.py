class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = start + (end - start) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                end = mid -1
            else:
                start = mid + 1
        return False