class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        # def solve(i,j,dp):
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     if i<0 or j<0:
        #         return int(1e9)
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     left = grid[i][j] + solve(i,j-1,dp)
        #     up = grid[i][j] + solve(i-1,j,dp)
        #     dp[i][j] = min(left,up)
        #     return dp[i][j]
        # dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        # return solve(m,n,dp)
        prev = [-1 for _ in range(n+1)]
        for i in range(m+1):
            cur = [-1 for _ in range(n+1)]
            for j in range(n+1):
                if i==0 and j==0:
                    cur[j]=grid[i][j]
                else:
                    left = grid[i][j]
                    if j>0:
                        left += cur[j-1]
                    else:
                        left += int(1e9)
                    up = grid[i][j]
                    if i>0:
                        up += prev[j]
                    else:
                        up += int(1e9)
                    cur[j] = min(left,up)
            prev = cur
        return prev[n]
        
        