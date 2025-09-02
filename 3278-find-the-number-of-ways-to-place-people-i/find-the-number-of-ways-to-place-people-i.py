class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0],-x[1]))
        n = len(points)
        ans = 0
        for i in range(n-1):
            x1,y1 = points[i]
            lb = -1
            for j in range(i+1,n):
                x2,y2 = points[j]
                if lb < y2 <= y1:
                    ans += 1
                    lb = y2
                if lb == y1:
                    break
        return ans
                