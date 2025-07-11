class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini = int(1e9)
            for ind in range(i,j+1):
                mini = min(mini,cuts[j+1] - cuts[i-1] + solve(i,ind-1) + solve(ind+1,j))
            dp[i][j] = mini
            return dp[i][j]            


        c = len(cuts)
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0 for _ in range(c+2)] for _ in range(c+2)]
        # return solve(1,c)
        for i in range(c,0,-1):
            for j in range(i,c+1):
                # if i > j:
                #     continue
                mini = float('inf')
                for k in range(i,j+1):
                    mini = min(mini,cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j])
                dp[i][j] = mini
        return dp[1][c]