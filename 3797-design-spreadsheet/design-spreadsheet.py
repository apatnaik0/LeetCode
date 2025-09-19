class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])-1
        self.spreadsheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])-1
        self.spreadsheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        refs = formula[1:].split('+')
        if refs[0].isnumeric() and refs[1].isnumeric():
            return int(refs[0])+int(refs[1])
        elif refs[0].isnumeric():
            col = ord(refs[1][0]) - ord('A')
            row = int(refs[1][1:])-1
            return int(refs[0])+self.spreadsheet[row][col]
        elif refs[1].isnumeric():
            col = ord(refs[0][0]) - ord('A')
            row = int(refs[0][1:])-1
            return int(refs[1])+self.spreadsheet[row][col]
        else:
            col1 = ord(refs[0][0]) - ord('A')
            row1 = int(refs[0][1:])-1
            col2 = ord(refs[1][0]) - ord('A')
            row2 = int(refs[1][1:])-1
            return self.spreadsheet[row1][col1]+self.spreadsheet[row2][col2]

         



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)