class Solution:
    def findKthPositive(self, arr, k):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k


# bujhi nai beparta

s = Solution()
print(s.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(s.findKthPositive(arr=[1, 2, 3, 4], k=2))
