class Solution:
    def boxind(self,row,col):
            return (row//3)*3 + col//3

    def solve(self,ind,board,empty, row, col, box):
        if ind == len(empty):
            return True
        r,c = empty[ind]

        for num in '123456789':
            if num not in row[r] and num not in col[c] and num not in box[self.boxind(r,c)]:
                board[r][c] = num
                row[r].add(num)
                col[c].add(num)
                box[self.boxind(r,c)].add(num)

                if self.solve(ind+1,board,empty, row, col, box):
                    return True

                board[r][c] = '.'
                row[r].remove(num)
                col[c].remove(num)
                box[self.boxind(r,c)].remove(num)

        return False


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    empty.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[self.boxind(i,j)].add(board[i][j])

        self.solve(0,board,empty, row, col, box)
        return board
        