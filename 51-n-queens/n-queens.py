class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def rec(col,board,n,left,udiag,ldiag):
            if col == n:
                ans.append(board[:])
                return
            for row in range(n):
                if left[row]==0 and ldiag[row+col]==0 and udiag[n-1+col-row]==0:
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    left[row]=1
                    ldiag[row+col]=1
                    udiag[n-1+col-row]=1
                    rec(col+1,board,n,left,udiag,ldiag)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]
                    left[row]=0
                    ldiag[row+col]=0
                    udiag[n-1+col-row]=0

        ans = []
        board = []
        for i in range(n):
            board.append('.'*n)
        left = [0]*n
        udiag = [0]*(2*n-1)
        ldiag = [0]*(2*n-1)
        rec(0,board,n,left,udiag,ldiag)
        return ans