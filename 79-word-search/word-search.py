class Solution:
    def solve(self,board,i,j,k,word,vis,m,n):
        if k == len(word):
            return True
        
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        for v in range(4):
            ni = i + dr[v]
            nj = j + dc[v]
            if 0<= ni < m and 0 <= nj < n and vis[ni][nj]==0 and word[k]==board[ni][nj]:
                vis[ni][nj] = 1
                if self.solve(board,ni,nj,k+1,word,vis,m,n):
                    return True
                vis[ni][nj] = 0

        return False
        
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis = [[0 for _ in range(n)] for _ in range(m)]
                    vis[i][j] = 1
                    if self.solve(board,i,j,1,word,vis,m,n):
                        return True
        
        return False
