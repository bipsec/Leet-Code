class Solution:

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            arr = [i for i in range(1, n+1)]

            prefixSum = [0] * (n + 1)
            suffixSum = [0] * (n + 1)
            for i in range(1, n + 1):
                prefixSum[i] = prefixSum[i - 1] + arr[i - 1]
                suffixSum[n - i] = suffixSum[n - i + 1] + arr[n - i]

            for i in range(1, n):
                if prefixSum[i] == suffixSum[i+1]:
                    return i + 1
            return -1


s = Solution()
print(s.pivotInteger(8))
print(s.pivotInteger(1))
print(s.pivotInteger(4))
print(s.pivotInteger(3))
print(s.pivotInteger(232))
        
        

