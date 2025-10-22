class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        prev = intervals[0]
        ans = []
        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(i[1],prev[1])
            else:
                ans.append(prev)
                prev = i
        ans.append(prev)
        return ans