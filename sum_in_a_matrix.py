class Solution:
    def matrixSum(self, nums) -> int:

        n = len(nums)
        arr = []
        for i in range(len(nums)):
            # print(nums[i])
            for j in range(0, len(nums[i])):
                print(nums[i][j])
#                 headpify korte hobe, pari na heapify










s = Solution()
print(s.matrixSum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
print(s.matrixSum([[1]]))
