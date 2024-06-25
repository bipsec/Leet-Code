class Solution:

    def backtrack(self, word):
        res = []
        for char in word:
            if char == "#":
                if res:
                    res.pop()
            else:
                res.append(char)
        return ''.join(res)

    def backspaceCompare(self, s: str, t: str) -> bool:

        if self.backtrack(s) == self.backtrack(t):
            return True
        return False


s = Solution()
print(s.backspaceCompare(s="ab#c", t="ad#c"))
print(s.backspaceCompare(s="ab##", t="c#d#"))
