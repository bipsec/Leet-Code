class Solution:
    def topKFrequent(self, nums, k):
        dupes = {}
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes[nums[i]] = 1
            else:
                dupes[nums[i]] += 1
        dupes, seen = (list(t) for t in zip(*sorted(zip(dupes.values(), dupes.keys()))))
        return seen[-k:]


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(s.topKFrequent(nums=[1], k=1))
print(s.topKFrequent([3, 0, 1, 0], k=1))
print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], k=2))
