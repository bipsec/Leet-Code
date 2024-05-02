class Solution:
    def findMaxK(self, nums) -> int:
        nums.sort()

        stack = []
        maxVal = float('-inf')
        for item in nums:
            if item < 1:
                stack.append(item)
                pos = item * -1
                if item > maxVal and pos in nums[:]:
                    maxVal = item * -1
                    return maxVal
        return -1


s = Solution()
print(s.findMaxK(nums=[-1, 2, -3, 3]))
print(s.findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
print(s.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
