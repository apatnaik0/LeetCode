class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        vis = [[0]*n for _ in range(m)]
        maxi = 0
        pq = [(grid[0][0],0,0)]
        while pq:
            h, r, c = heapq.heappop(pq)
            if vis[r][c]==1:
                continue
            vis[r][c] = True
            maxi = max(maxi,h)
            if r == m-1 and c == n-1:
                return maxi
            d = [1,0,-1,0,1]
            for delta in range(4):
                nr = r + d[delta]
                nc = c + d[delta+1]
                if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc]:
                    heapq.heappush(pq,(grid[nr][nc],nr,nc))
        return maxi