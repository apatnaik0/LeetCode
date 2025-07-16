class Solution:
    def dfs(self,i,j,board,vis,n,m):
        vis[i][j]=1
        # print(i,j)
        delr = [0,0,1,-1]
        delc = [1,-1,0,0]
        for k in range(4):
            nr = i + delr[k]
            nc = j + delc[k]
            if nr>=0 and nr<n and nc>=0 and nc<m and board[nr][nc]=='O' and vis[nr][nc]==0:
                self.dfs(nr,nc,board,vis,n,m)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            if vis[0][i]==0 and board[0][i]=='O':
                self.dfs(0,i,board,vis,n,m)
            if vis[n-1][i]==0 and board[n-1][i]=='O':
                self.dfs(n-1,i,board,vis,n,m)
        for i in range(n):
            if vis[i][0]==0 and board[i][0]=='O':
                self.dfs(i,0,board,vis,n,m)
            if vis[i][m-1]==0 and board[i][m-1]=='O':
                self.dfs(i,m-1,board,vis,n,m)
        # print(vis)
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and board[i][j]=='O':
                    board[i][j] = 'X'
        
        

        