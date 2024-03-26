class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        res = set()

        for i in range(0, len(nums)):
            res.add(nums[i - 1])
            # print(res)
        for j in range(1, len(res) + 1):
            if j not in res:
                return j
        return j + 1
