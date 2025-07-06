class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # def solve(i,j):
        #     if j<0 or j>=n:
        #         return int(1e9)
        #     if i==0:
        #         return matrix[i][j]
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up = matrix[i][j] + solve(i-1,j)
        #     ld = matrix[i][j] + solve(i-1,j-1)
        #     rd = matrix[i][j] + solve(i-1,j+1)
        #     dp[i][j] = min(up,ld,rd)
        #     return dp[i][j]
        mini = int(1e9)
        prev = [-1 for _ in range(n)]
        # for i in range(n):
        #     mini = min(mini,solve(n-1,i))
        for i in range(n):
            prev[i] = matrix[0][i]
        for i in range(1,n):
            cur = [-1 for _ in range(n)]
            for j in range(n):
                up = matrix[i][j] + prev[j]
                ld = matrix[i][j] 
                if j>0:
                    ld += prev[j-1]
                else:
                    ld += int(1e9)
                rd = matrix[i][j]
                if j<n-1:
                    rd += prev[j+1]
                else:
                    rd += int(1e9)
                cur[j] = min(up,ld,rd)
            prev = cur
        for i in range(n):
            mini = min(mini,prev[i])
        return mini
            
        