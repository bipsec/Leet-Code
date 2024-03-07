class Solution:
  def compress(self, chars) -> int:
    if len(chars) == 1:
      return chars

    start, end = 0, len(chars) - 1
    count = 0
    for i in range(len(chars)):
      while start <= end:
        if chars[start] == chars[start+1]:
          count += 1
        chars.insert(i, count)
        start += 1
    return chars


s = Solution()
print(s.compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(chars=["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a", "c"]))
print(s.compress(chars=["a", "b", "c", "d", "a", "v", "c"]))
print(s.compress(chars=["a"]))
