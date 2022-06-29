class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []

        def dfs(temp, index):
            result.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(temp, i+1)
                temp.pop()

        dfs([], 0)
        # print(result)




s = Solution()
# print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 2]))
