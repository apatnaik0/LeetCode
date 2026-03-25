class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        q = deque()
        q.append((0,0))
        directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        vis = [[-1 for _ in range(n)] for _ in range(n)]
        vis[0][0] = 1

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<n and 0<=nc<n and vis[nr][nc] == -1 and grid[nr][nc] == 0:
                    vis[nr][nc] = vis[r][c] + 1
                    q.append((nr,nc))
        
        return vis[n-1][n-1]
