# import collections
#
#
# class Solution:
#
#     def counter(self, elm, count):
#         return [elm] * count
#
#     def relativeSortArray(self, arr1, arr2):
#         not_in = []
#         res = []
#         for i in range(len(arr1)):
#             if arr1[i] not in arr2:
#                 not_in.append(arr1[i])
#
#         counter = collections.Counter(arr1)
#
#         for item in arr2:
#             for key, val in counter.items():
#                 if key == item:
#                     res.extend(self.counter(key, val))
#         not_in.sort()
#         res.extend(not_in)
#         return res


class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr = []
        for item in arr2:
            while item in arr1:
                arr.append(item)
                arr1.remove(item)

        return arr + sorted(arr1)


s = Solution()
print(s.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
print(s.relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
