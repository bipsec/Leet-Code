class Solution:
    def maxDistance(self, arrays):
        minVal = float("-inf")
        maxVal = float("inf")

        for item in arrays:
            for j in item:
                if j > minVal:
                    minVal = j
                if j < maxVal:
                    maxVal = j

        return abs(maxVal - minVal)


s = Solution()
print(s.maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]))
print(s.maxDistance(arrays=[[1], [1]]))
print(s.maxDistance([[1, 4], [0, 5]]))
