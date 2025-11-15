class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ct = 0
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        vis = [[ -1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    vis[i][j] = 1
        
        if fresh == 0:
            return 0
        rot = 0
        while q:
            s = len(q)
            for i in range(s):
                r,c = q.popleft()
                dr = [0,0,1,-1]
                dc = [1,-1,0,0]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc]==1 and vis[nr][nc]!= 1:
                        q.append((nr,nc))
                        vis[nr][nc] = 1
                        rot += 1
            ct += 1
        
        return ct-1 if rot == fresh else -1

        

