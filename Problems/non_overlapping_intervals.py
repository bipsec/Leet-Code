class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove_count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                remove_count += 1
            else:
                end = intervals[i][1]

        return remove_count

# not mine


s = Solution()
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
print(s.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))
