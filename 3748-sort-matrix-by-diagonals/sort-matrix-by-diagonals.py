class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag = [[] for _ in range(n*2-1)]
        for i in range(n):
            for j in range(n):
                diag[i-j+n-1].append(grid[i][j])
        # print(diag)
        for k in range(len(diag)):
            if k < n-1:  
                diag[k].sort()
            elif k >= n-1:
                diag[k].sort(reverse=True)
        for i in range(n):
            for j in range(n):
                d = diag[i-j+n-1]
                grid[i][j] = d.pop(0)
        return grid
        
