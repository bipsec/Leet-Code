class Solution:
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]

        x1 = coordinates[1][0]
        y1 = coordinates[1][1]

        dx = x1 - x0
        dy = y1 - y0

        for i in range(n):
            x = coordinates[i][0]
            y = coordinates[i][1]

            if dx * (y - y1) != dy * (x - x1):
                return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
