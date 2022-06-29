class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        start, end = 0, len(nums)-1
        mid = len(nums) // 2
        res = {}

        while start < mid:
            if nums[start] == nums[mid]:
                return nums[start]
            elif nums[start] == nums[end]:
                return nums[start]

            elif nums[start] != nums[mid]:
                if nums[start] not in res.keys():
                    res[nums[start]] = 77
                    # print(res)
                else:
                    return nums[start]
            start += 1

        while mid < end:
            if nums[mid] == nums[end]:
                return nums[mid]

            elif nums[mid] != nums[end]:
                if nums[mid] not in res.keys():
                    res[nums[mid]] = 77
                    # print(res)
                else:
                    return nums[mid]
            mid += 1


        ######### Second Approach########
        # res = {}
        #
        # for i in nums:
        #     if i in res:
        #         return i
        #     res[i] = 77


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
print(s.findDuplicate([2, 1, 2]))
