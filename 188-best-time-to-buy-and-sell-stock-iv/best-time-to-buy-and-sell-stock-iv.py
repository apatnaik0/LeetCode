class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def solve(i,t):
            if t==0 or i==n:
                return 0
            if dp[i][t]!=0:
                return dp[i][t]
            if t%2==0:
                dp[i][t] = max(-prices[i]+solve(i+1,t-1),solve(i+1,t))
            else:
                dp[i][t] = max(prices[i]+solve(i+1,t-1),solve(i+1,t))
            return dp[i][t]

        n = len(prices)
        # dp = [[0 for _ in range(2*k+1)] for _ in range(n+1)]
        prev = [0 for _ in range(2*k+1)]
        # return solve(0,2*k)
        for i in range(n-1,-1,-1):
            cur = [0 for _ in range(2*k+1)]
            for t in range(1,2*k+1):
                if t%2==0:
                    cur[t] = max(-prices[i]+prev[t-1],prev[t])
                else:
                    cur[t] = max(prices[i]+prev[t-1],prev[t])
            prev = cur
        return prev[2*k]
