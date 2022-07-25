class Solution:
  def repeatedCharacter(self, s: str) -> str:
    stack = []
    for i in range(len(s)):
      if s[i] not in stack:
        stack.append(s[i])
      if s[i+1] in stack:
        return s[i+1]


      # stack.pop()




s = Solution()
print(s.repeatedCharacter(s = "abccbaacz"))
print(s.repeatedCharacter(s = "abcdd"))
print(s.repeatedCharacter(s = "abacdaa"))
print(s.repeatedCharacter(s = "nwcn"))