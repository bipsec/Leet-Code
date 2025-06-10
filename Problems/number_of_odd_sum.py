import itertools


class Solution:

    def check(self, num):
        comb = []

        for i in range(len(num)):
            comb += itertools.combinations(num, i + 1)

        combs = [list(t) for t in comb]
        return combs

    def numOfSubarrays(self, arr) -> int:
        odds = []

        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                odds.append(arr[i])
        res = []
        if len(odds) < 1:
            return 0
        else:
            nums = self.check(odds)
        print(nums)

        for items in nums:
            val = 0
            for i in items:
                val += i
            res.append(val)
        print(res)

        ans = 0

        for i in range(len(res)):
            if i % 2 != 0 and res[i] % 2 != 0:
                ans += res[i]
        return ans


# can solve it, but it will take time!!!

s = Solution()
print(s.numOfSubarrays(arr=[1, 3, 5]))
print(s.numOfSubarrays(arr=[2, 4, 6]))
print(s.numOfSubarrays(arr=[1, 2, 3, 4, 5, 6, 7]))
