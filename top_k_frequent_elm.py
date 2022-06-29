class Solution:
    def topk(self, nums: list[int], k:int)-> list[int]:
        res = {}
        dupes = []
        seen = []

        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1
        # print(res)
        for key, value in res.items():
            seen.append(key)
            dupes.append(value)
        # print(seen, dupes)

        dupes, seen = (list(t) for t in zip(*sorted(zip(dupes, seen))))

        return seen[-k:]


s = Solution()
print(s.topk([1, 1, 1, 2, 2, 3], 1))
print(s.topk([1, 2, 2, 2, 2, 2, 4, 3, 3, 3, 1, 1, 1], 1))
print(s.topk([3, 0, 1, 0], 1))
print(s.topk([1], 1))
