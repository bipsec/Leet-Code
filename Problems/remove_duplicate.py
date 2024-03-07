class Solution:
  def removeDuplicateLetters(self, s: str) -> str:

    stack = []
    result = set()
    seen = {}
    for i in range(len(s)):
      seen[s[i]] = i

    for idx, ch in enumerate(s):
      if ch in result:
        continue
      else:
        while stack and stack[-1] > ch and seen[stack[-1]] > idx:
          remove_char = stack.pop()
          result.remove(remove_char)
        result.add(ch)
        stack.append(ch)
    return "".join(stack)


s = Solution()
print(s.removeDuplicateLetters(s="bcabc"))
print(s.removeDuplicateLetters(s="cbacdcbc"))
