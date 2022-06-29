class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        dupes = []
        for i in range(len(grid)):
            for a, b, c, d in grid:
                print(a,b,c,d)
                if a != 0:
                    dupes.append(a)






s = Solution()
print(s.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
# print(s.countHousePlacements(2))
# print(s.countHousePlacements(3))
