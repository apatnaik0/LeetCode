class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        possible = 0
        endt = float('-inf')
        for i in intervals:
            if i[0]>=endt:
                possible += 1
                endt = i[1]
        return len(intervals)-possible
