from math import inf as oo

class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        total = sum(arr)
        kadanes = self.maxSubArraySum(arr)
        if (k < 2): return kadanes % (10 ** 9 + 7)
        if (total > 0): return (kadanes + (k - 1) * total) % (10 ** 9 + 7)
        stitchedKadanes = self.maxSubArraySum(arr * 2)
        return stitchedKadanes % (10 ** 9 + 7)

    def maxSubArraySum(self, a):
        size = len(a)
        max_sum = -oo
        count = 0

        for i in a:
            count += i
            if count < 0: count = 0
            max_sum = max(max_sum, count)

        return max_sum


s = Solution()
print(s.kConcatenationMaxSum(arr=[1, 2], k=3))
print(s.kConcatenationMaxSum(arr=[1, -2, 1], k=5))
print(s.kConcatenationMaxSum(arr=[-1, -2], k=7))
print(s.kConcatenationMaxSum(arr=[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000], k=100000))