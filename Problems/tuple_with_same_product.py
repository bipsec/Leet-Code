from collections import defaultdict


class Solution:

    def tupleSameProduct(self, nums):
        product_map = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                count += product_map[product]
                product_map[product] += 1

        return count * 8


s = Solution()
print(s.tupleSameProduct([1, 2, 3, 4]))
print(s.tupleSameProduct([1, 2, 4, 5, 8, 12, 14, 16]))
print(s.tupleSameProduct([2, 3, 4, 6]))
print(s.tupleSameProduct(nums=[1, 2, 4, 5, 10]))
