class Solution:
    def sortedSquares(self, s):

        start, end = 0, len(s)-1

        while start < end:
            if (abs(s[start])) > (abs(s[end])):
                s[start], s[end] = s[end], s[start]
                s[end] = s[end] ** 2
                end -= 1
            else:
                s[end] = s[end] ** 2
                end -= 1

        s[start] = s[start] ** 2
        s = sorted(s)
        return s


s = Solution()
print(s.sortedSquares([-5, -3, -2, -1]))


class Solve:
    def alter(self, s):
        res = []
        for i in s:
            res.append(i**2)
        res = sorted(res)
        return res


r = Solve()
print(r.alter([-4, -1, 0, 3, 10]))
