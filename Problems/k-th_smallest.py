class Solution:
    def kthSmallest(self, matrix, k) -> int:
        res = []
        for l in matrix:
            res += l
        return res[k-1]


s = Solution()
print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
