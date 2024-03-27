from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k: int):
        count = 0
        sum_freq = defaultdict(int)
        current_sum = 0
        sum_freq[0] = 1

        for num in nums:
            current_sum += num
            count += sum_freq[current_sum - k]
            sum_freq[current_sum] += 1

        return count


s = Solution()
print(s.subarraySum(nums=[1, 1, 1], k=2))
print(s.subarraySum(nums=[1, 2, 3], k=3))
print(s.subarraySum(nums=[-1, -2, 1], k=2))
print(s.subarraySum(nums=[-3, -6, 9], k=9))
