class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        start = end = 1
        mid = start + end
        result = [0] * numRows
        print(result)
        i = 0
        j = numRows
        while start < numRows and end < numRows:
            result[i] = start
            result[j-1] = end
            result[mid] = result[start] + result[end]
            i += 1
            j -= 1
        return result


s = Solution()
print(s.generate(4))
