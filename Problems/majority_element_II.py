class Solution:
    def majorityElement(self, nums):

        dupes = {}

        for item in nums:
            if item not in dupes:
                dupes[item] = 1
            else:
                dupes[item] += 1

        res = []

        upTo = len(nums) // 3

        for element, count in dupes.items():
            if count > upTo:
                res.append(element)

        return res


s = Solution()
print(s.majorityElement(nums=[3, 2, 3]))
print(s.majorityElement(nums = [1,2]))
