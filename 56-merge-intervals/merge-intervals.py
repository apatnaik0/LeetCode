class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        n = len(intervals)
        ans = []

        for i in range(1,n):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1],prev[1])
            else:
                ans.append(prev)
                prev = intervals[i]
        
        ans.append(prev)
        return ans