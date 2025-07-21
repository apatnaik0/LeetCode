class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        pq = [(0,0,0)]
        maxi = 0
        vis = set()
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        while pq:
            eff, row, col = heappop(pq)
            maxi = max(maxi,eff)
            if (row,col) == (rows-1,cols-1):
                return maxi
            vis.add((row,col))
            for i in range(4):
                new_row,new_col = row+dr[i],col+dc[i]
                if new_row>=0 and new_row<rows and new_col>=0 and new_col<cols and (new_row,new_col) not in vis:
                    new_eff = abs(heights[new_row][new_col]-heights[row][col])
                    heappush(pq,(new_eff,new_row,new_col))
        return 0
