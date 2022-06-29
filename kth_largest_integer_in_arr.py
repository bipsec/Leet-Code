import heapq


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:

        res = []
        for i in range(len(nums)):
            res.append(int(nums[i]))

        arr = [-elm for elm in res]
        heapq.heapify(arr)

        for i in range(k-1):
            heapq.heappop(arr)
        return str(- heapq.heappop(arr))






s = Solution()
print(s.kthLargestNumber(["3", "6", "7", "10"], 4))
print(s.kthLargestNumber(["2","21","12","1"], 3))
