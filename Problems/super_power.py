class Solution:
  def superPow(self, a: int, b) -> int:
    return pow(a,  int("".join(map(str, b))), 1337)


s = Solution()
# print(s.superPow(a=2, b=[3]))
# print(s.superPow(a=2, b=[1, 0]))
# print(s.superPow(a=5, b=[1, 0]))
# print(s.superPow(a=1, b=[4, 3, 3, 8, 5, 2]))
print(s.superPow(a=1000, b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
