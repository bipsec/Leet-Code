class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # mem = [0] * (len(nums) + 1)
        # # print(mem)
        # queue = []
        # for n in nums:
        #     mem[n] = 1
        #     print(mem)
        # for k in range(1, len(mem)):
        #     if not mem[k]:
        #         queue.append(k)
        # return queue

        # result = {}
        #
        # for i in range(0, len(nums)):
        #     result[i+1] = nums[i]
        # keys = list(result.keys())
        #
        # return list(set(keys) ^ set(nums))

        map = {}
        ans = []

        for i in range(len(nums)):
            map[nums[i]] = 1
            # print(map)
        for j in range(1, len(nums)+1):
            if j not in map.keys():
                ans.append(j)
        return ans


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
# print(s.findDisappearedNumbers([1, 1]))
# print(s.findDisappearedNumbers([1]))
