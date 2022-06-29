class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        output = []
        count = 0
        n = len(nums)-1

        stack = []
        for i in range(n-1, -1, -1):
            stack.append(nums[i])
            if nums[i-1] > stack[0]:
                stack.pop()



        return stack, count


s = Solution()
# print(s.totalSteps([5, 3, 4, 6, 7, 8, 3, 9, 1, 11, 11]))
print(s.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
# print(s.totalSteps([4, 5, 7, 7, 13]))
