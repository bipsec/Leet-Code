class Solution:
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            current_array = arrays[i]
            max_distance = max(max_distance, abs(current_array[-1] - min_val), abs(max_val - current_array[0]))

            min_val = min(min_val, current_array[0])
            max_val = max(max_val, current_array[-1])

        return max_distance


s = Solution()
# print(s.maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]))
# print(s.maxDistance(arrays=[[1], [1]]))
# print(s.maxDistance([[1, 4], [0, 5]]))
# print(s.maxDistance([[1, 4, 5], [0, 2]]))
# print(s.maxDistance([[-1, 5], [1, 4, 6], [4, 5, 6]]))
print(s.maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]))
