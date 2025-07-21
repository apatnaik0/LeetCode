class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque()
        q.append([0,0,1])
        dist = [[False for _ in range(n)] for _ in range(n)]
        while q:
            x,y,d = q.popleft()
            if x == n-1 and y==n-1:
                return d
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i!=0 or j!=0:
                        nx = x + i
                        ny = y + j
                        # print(nx,ny)
                        if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny]==0 and not dist[nx][ny]:
                            # print('inside if',nx,ny)
                            dist[nx][ny] = True
                            q.append([nx,ny,d+1])
        return -1
