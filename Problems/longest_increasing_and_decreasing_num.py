class Solution:
    def longestMonotonicSubarray(self, nums) -> int:

        max_count = 1
        max_neg_count = 1

        count = 1
        neg_count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                neg_count = 1
            elif nums[i - 1] < nums[i]:
                neg_count += 1
                count = 1
            else:
                count = 1
                neg_count = 1
            if count > max_count:
                max_count = count
            if neg_count > max_neg_count:
                max_neg_count = neg_count

        return max_count if max_count > max_neg_count else max_neg_count


# had to reset the counter: this was the major hack!!

s = Solution()
print(s.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]))
print(s.longestMonotonicSubarray(nums=[3, 3, 3, 3]))
print(s.longestMonotonicSubarray(nums=[3, 2, 1]))
print(s.longestMonotonicSubarray(nums=[1, 10, 10]))
print(s.longestMonotonicSubarray(nums=[1]))
print(s.longestMonotonicSubarray(nums=[1, 5, 2, 7]))
