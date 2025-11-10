class Solution:
    def rec(self, col, board, ans, l ,ld, ud, n):
        if col == n:
            ans.append(board[:])
            return ans
        
        for row in range(n):
            if l[row] == 0 and ld[row+col]==0 and ud[n-1+col-row]==0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                l[row] = 1
                ld[row+col] = 1
                ud[n-1+col-row] = 1
                self.rec(col+1, board, ans, l, ld, ud, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                l[row] = 0
                ld[row+col] = 0
                ud[n-1+col-row] = 0
        return ans


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = []
        for i in range(n):
            s = '.'*n
            board.append(s)
        
        l = [0]*n
        ld = [0]*(2*n-1)
        ud = [0]*(2*n-1)

        ans = self.rec(0,board,ans,l,ld,ud,n)
        return ans