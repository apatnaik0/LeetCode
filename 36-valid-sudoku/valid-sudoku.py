class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = [set() for _ in range(9)]
        col_count = [set() for _ in range(9)]
        box_count = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in row_count[i]:
                        return False
                    else:
                        row_count[i].add(board[i][j])

                    if board[i][j] in col_count[j]:
                        return False
                    else:
                        col_count[j].add(board[i][j])
                    
                    if board[i][j] in box_count[(i//3)*3 + j//3]:
                        return False
                    else:
                        box_count[(i//3)*3 + j//3].add(board[i][j])
        
        return True
