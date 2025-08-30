class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == '.':
                    continue
                if ele in row[i] or ele in col[j] or ele in box[(i//3,j//3)]:
                    return False
                row[i].add(ele)
                col[j].add(ele)
                box[(i//3,j//3)].add(ele)
        return True