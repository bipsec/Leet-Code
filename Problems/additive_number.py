class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    num = list(num)
    stack = []


    for i in range(1, len(num)):
      stack.append(num[i-1])
      if i < len(num)-1 and num[i] + stack[-1] == num[i+1]:
        stack.pop()
    print(stack)



s = Solution()
print(s.isAdditiveNumber("112358"))
print(s.isAdditiveNumber("199100199"))
