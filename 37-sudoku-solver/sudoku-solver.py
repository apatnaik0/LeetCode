class Solution:
    def boxind(self,i,j):
        return (i//3)*3 + j//3

    def rec(self, ind, board, row, col, box , empty):
        if ind == len(empty):
            return True

        r,c = empty[ind]
        
        for i in '123456789':
            if i not in row[r] and i not in col[c] and i not in box[self.boxind(r,c)]:
                board[r][c] = i
                row[r].add(i)
                col[c].add(i)
                box[self.boxind(r,c)].add(i)
                if self.rec(ind+1, board, row, col, box , empty):
                    return True
                board[r][c] = '.'
                row[r].discard(i)
                col[c].discard(i)
                box[self.boxind(r,c)].discard(i)
        return

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty = []
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    empty.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[self.boxind(i,j)].add(board[i][j])
            
        self.rec(0, board, row, col, box, empty)
        

        