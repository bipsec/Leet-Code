class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        ans = 0
        sub = 0
        for i in range(len(n)):
            if i % 2 == 0:
                ans += int(n[i])
            else:
                sub += int(n[i])
        return ans - sub


s = Solution()
print(s.alternateDigitSum(n=521))
print(s.alternateDigitSum(n=111))
print(s.alternateDigitSum(n=886996))
print(s.alternateDigitSum(n=982375619875))
