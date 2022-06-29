class Solution:
    def twoSumLessThanK(self, A, K):
        
        # start = 0
        # end  = len(A)-1
        # result = 0

        # while start < end:
        #     if A[start] + A[end] <= K:
        #         temp  = A[start] + A[end]
        #         result = max(temp, result)
        #     end -= 1

        # return result
        a = ['a', 'b', 'c', 3, 4, 'd', 6, 7, 8]
        b = [0, 1, 2, 4, 6, 7, 8]
        b = [a[i] for i in b]
        return b


s = Solution()
print(s.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 160))
