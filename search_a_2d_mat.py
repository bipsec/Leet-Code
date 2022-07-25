class Solution:
  def searchMatrix(self, matrix, target) -> bool:
    n = len(matrix)

    for row in range(n):
      for col in range(n):
        hasvalue = False
        for i in range(n):
          if matrix[row][i] == target and matrix[i][col] == target:
            hasvalue = True
        if hasvalue:
          return hasvalue
    return hasvalue


s = Solution()
print(s.searchMatrix(
  matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],[3, 6, 9, 16, 22]\
    , [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
  target=5))
print(s.searchMatrix(
  matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]\
    , [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
  target=20))
