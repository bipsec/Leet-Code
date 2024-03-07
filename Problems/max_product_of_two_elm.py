import heapq


class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        res = 1
        arr = [-elm for elm in nums]
        heapq.heapify(arr)

        for i in range(3-1):
            val = heapq.heappop(arr) + 1
            res *= val

        return res


s = Solution()
print(s.maxProduct([1, 2, 3, 4, 5]))
print(s.maxProduct([3, 4, 5, 2]))
print(s.maxProduct([1, 5, 4, 5]))
print(s.maxProduct([3, 7]))
print(s.maxProduct([3, 2]))
