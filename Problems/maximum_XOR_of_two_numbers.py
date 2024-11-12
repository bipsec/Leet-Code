class Solution:
    def findMaximumXOR(self, nums):

        maxVal = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = nums[i] ^ nums[j]
                if val > maxVal:
                    maxVal = val

        return maxVal

    # for larger array it gives TLE :O(n**2)


s = Solution()
# print(s.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))
# print(s.findMaximumXOR(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
# print(s.findMaximumXOR(nums=[14, 15, 9, 3, 2]))
# print(s.findMaximumXOR(nums=[10, 23, 20, 18, 28]))

