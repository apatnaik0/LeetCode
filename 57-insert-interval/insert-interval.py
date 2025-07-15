class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        i = 0
        while i<n and newInterval[0]>intervals[i][1]:
            ans.append(intervals[i])
            i += 1
        while i<n and newInterval[1]>=intervals[i][0]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1
        ans.append(newInterval)
        while i<n:
            ans.append(intervals[i])
            i += 1
        return ans


        