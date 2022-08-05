class Solution:
  def maximumGroups(self, grades) -> int:
    grades.sort()

    total = 0
    get_val = 0

    while total <= len(grades):
      get_val += 1
      total += get_val
    return get_val - 1


s = Solution()
print(s.maximumGroups(grades=[10, 6, 12, 7, 3, 5]))
print(s.maximumGroups(grades=[8, 8]))
