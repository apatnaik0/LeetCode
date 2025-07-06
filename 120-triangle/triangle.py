class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        # def solve(i,j):
        #     if i == n-1:
        #         return triangle[i][j]
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     down = triangle[i][j] + solve(i+1,j)
        #     diag = triangle[i][j] + solve(i+1,j+1)
        #     dp[i][j] = min(down,diag)
        #     return dp[i][j]
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + dp[i+1][j]
                diag = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,diag)
        return dp[0][0]