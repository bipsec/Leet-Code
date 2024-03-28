class Solution:
    def generate_sorted_arr(self, nums):
        sums = []
        for i in range(len(nums)):
            val = 0
            for j in range(i, len(nums)):
                val += nums[j]
                sums.append(val)
        sums.sort()
        return sums

    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        result = self.generate_sorted_arr(nums)
        ans = 0
        for i in range(left - 1, right):
            ans += result[i]
        return ans % 1_000_000_007


s = Solution()
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=3, right=4))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=10))
