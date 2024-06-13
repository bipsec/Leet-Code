class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        seats.sort()
        students.sort()
        c, n = 0, len(seats)
        for i in range(n):
            c += abs(seats[i] - students[i])
        return c


s = Solution()
print(s.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
