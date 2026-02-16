class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ct= 0
        n = len(intervals)
        prev = intervals[0]
        for i in range(1,n):
            if prev[1] > intervals[i][0]:
                ct += 1
                # prev[1] = max(prev[1],intervals[i][1])
            else:
                prev = intervals[i]
        return ct