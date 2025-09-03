class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0],-x[1]))
        ans = 0
        n = len(points)
        for i in range(n-1):
            x1,y1 = points[i]
            prev = float('-inf')
            for j in range(i+1,n):
                x2,y2 = points[j]
                if prev < y2 <= y1:
                    ans += 1
                    prev = y2
                if prev == y1:
                    break
        return ans