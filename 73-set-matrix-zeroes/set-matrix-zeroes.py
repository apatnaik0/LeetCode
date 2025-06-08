class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        r1z = False
        c1z = False

        for i in range(rows):
            if matrix[i][0]==0:
                c1z = True
                break

        for i in range(cols):
            if matrix[0][i]==0:
                r1z = True
                break
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        
        if c1z:
            for i in range(rows):
                matrix[i][0]=0
        
        if r1z:
            for i in range(cols):
                matrix[0][i]=0


        