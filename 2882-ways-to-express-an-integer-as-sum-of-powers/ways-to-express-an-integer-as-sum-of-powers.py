class Solution:
    def solve(self,n,x,dp,ct):
        # print(n,x,ct)
        if n==0:
            return 1
        if ct>n:
            return 0
        mod = 10**9 + 7
        if dp[n][ct]!=-1:
            return dp[n][ct]
        pick = 0
        if pow(ct,x)<=n:
            pick = self.solve(n-pow(ct,x),x,dp,ct+1)
        notpick = self.solve(n,x,dp,ct+1)
        dp[n][ct] = (pick + notpick)%mod
        return dp[n][ct]

    def numberOfWays(self, n: int, x: int) -> int:
        
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        ans = self.solve(n,x,dp,1)
        return ans