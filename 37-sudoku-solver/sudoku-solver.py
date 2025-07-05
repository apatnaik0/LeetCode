class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and collect empty positions
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    c = board[i][j]
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[(i // 3) * 3 + (j // 3)].add(c)

        def solve(idx):
            if idx == len(empty):
                return True  # Done!

            i, j = empty[idx]
            b = (i // 3) * 3 + (j // 3)

            for c in '123456789':
                if c not in rows[i] and c not in cols[j] and c not in boxes[b]:
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[b].add(c)

                    if solve(idx + 1):
                        return True

                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[b].remove(c)

            return False

        solve(0)
