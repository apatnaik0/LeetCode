class Solution:
    def solve(self,i,j,cuts,dp):
        if i > j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini = float('inf')
        for ind in range(i,j+1):
            mini = min(mini, cuts[j+1] - cuts[i-1] + self.solve(i,ind-1,cuts,dp) + self.solve(ind+1,j,cuts,dp))
        dp[i][j] = mini
        return dp[i][j]

    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[-1 for _ in range(c+2)] for _ in range(c+2)]
        return self.solve(1,c,cuts,dp)