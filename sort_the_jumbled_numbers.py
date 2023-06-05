class Solution:
    def sort_list(self, list1, list2):
        indices = [i for i, x in sorted(enumerate(list2), key=lambda x: x[1])]
        arr = [list1[i] for i in indices]
        return arr

    def sortJumbled(self, mapping, nums):

        numberDict = {}
        for item in range(len(mapping)):
            numberDict[item] = mapping[item]
        changed_num = ""
        stack = []

        for item in nums:
            left, right = 0, len(str(item))
            while left < right:
                item = str(item)
                changed_num += str(numberDict[int(item[left])])
                left += 1
            stack.append(int(changed_num))
            changed_num = ""

        res = self.sort_list(nums, stack)
        return res


s = Solution()
print(s.sortJumbled(mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]))
print(s.sortJumbled(mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]))
