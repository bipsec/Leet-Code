class Solution:
    def arrayRankTransform(self, arr):

        dupes = {}
        for key, val in enumerate(sorted(set(arr))):
            dupes[val] = key + 1

        output = [dupes[item] for item in arr]
        return output


s = Solution()
print(s.arrayRankTransform(arr=[40, 10, 20, 30]))
print(s.arrayRankTransform(arr=[100, 100, 100]))
print(s.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12])) # [5,3,4,2,8,6,7,1,3]
