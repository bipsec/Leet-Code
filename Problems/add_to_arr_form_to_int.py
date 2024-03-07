class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        res = "".join(str(i) for i in num)
        res = int(res) + k
        return [str(i) for i in str(res)]


s = Solution()
print(s.addToArrayForm([1, 2, 0, 0], 34))
print(s.addToArrayForm([2, 7, 4],  181))
