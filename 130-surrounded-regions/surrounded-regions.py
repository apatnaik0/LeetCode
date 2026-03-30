class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        points = deque()

        m = len(board)
        n = len(board[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        for i in range(m):
            if board[i][0] == 'O':
                points.append((i,0))
                vis[i][0] = 1
            if board[i][n-1] == 'O':
                points.append((i,n-1))
                vis[i][n-1] = 1

        for i in range(1,n-1):
            if board[0][i] == 'O':
                points.append((0,i))
                vis[0][i] = 1
            if board[m-1][i] == 'O':
                points.append((m-1,i))
                vis[m-1][i] = 1

        while points:
            r,c = points.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0<= nr < m and 0<= nc<n and vis[nr][nc]==0 and board[nr][nc] == 'O':
                    vis[nr][nc] = 1
                    points.append((nr,nc))
                
        for i in range(m):
            for j in range(n):
                if vis[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        
        

        