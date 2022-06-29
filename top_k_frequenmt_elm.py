import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        res = [-elm for elm in nums]
        heapq.heapify(res)
        for i in range(k-1):
            heapq.heappop(res)
        return -heapq.heappop(res)



s = Solution()
# print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
# print(s.topKFrequent([1, 2, 3, 4, 2, 1, 3, 2, 2, 1], 1))
print(s.topKFrequent([4, 2, 9, 7, 5, 6, 7, 1, 3], 4))
# print(s.topKFrequent([1], 1))

