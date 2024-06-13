class Solution:
    def findJudge(self, n: int, trust) -> int:
        l = [[0, 0] for x in range(n + 1)]
        for i in trust:
            l[i[1]][1] += 1
            l[i[0]][0] += 1
        for i in range(1, len(l)):
            if l[i][0] == 0 and l[i][1] == n - 1:
                return i
        return -1


# not mine

s = Solution()
print(s.findJudge(n=2, trust=[[1, 2]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
