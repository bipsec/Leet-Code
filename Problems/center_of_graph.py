class Solution:
    def findCenter(self, edges) -> int:
        return list(set.intersection(*map(set, edges)))[0]
        # OR
        # return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


s = Solution()
print(s.findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
print(s.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))
