class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1
    if n < 0:
      return 1/self.myPow(x, -n)

    res = self.myPow(x*x, n // 2)

    return x*res if n % 2 else res

# not mine









s = Solution()
print(s.myPow(x = 2.00000, n = 10))
print(s.myPow(x = 2.10000, n = 3))
print(s.myPow(x = 2.00000, n = -2))