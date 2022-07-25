class Solution:
  def equalPairs(self, grid) -> int:
    n = len(grid)
    res = 0
    for row in range(n):
      for col in range(n):
        hasPair = True
        for i in range(n):
          if grid[row][i] != grid[i][col]:
            hasPair = False
            break
        if hasPair:
          res += 1
    return res
# not mine


s = Solution()
print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))