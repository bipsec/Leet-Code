class Solution:

    def check_power(self, num, count=0):

        if num == 1:
            return count
        elif num % 2 == 0:
            return self.check_power(num // 2, count + 1)
        elif num % 2 != 0:
            return self.check_power(3 * num + 1, count + 1)

    def getKth(self, lo: int, hi: int, k: int) -> int:

        dupes = {}

        for i in range(lo, hi + 1):
            val = self.check_power(i)
            dupes[i] = val

        dupes = dict(sorted(dupes.items(), key=lambda x: x[1]))
        keys = list(dupes.keys())
        return keys[k-1]


s = Solution()
print(s.getKth(lo=12, hi=15, k=2))
print(s.getKth(lo=7, hi=11, k=4))
print(s.getKth(lo=1, hi=101, k=11))
