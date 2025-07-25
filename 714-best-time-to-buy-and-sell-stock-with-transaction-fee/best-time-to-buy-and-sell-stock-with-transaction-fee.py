class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        def solve(i,buy):
            if i==n:
                return 0
            if dp[i][buy] != 0:
                return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i] + solve(i+1,0),solve(i+1,1))
            else:
                dp[i][buy] = max(prices[i] - fee + solve(i+1,1),solve(i+1,0))
            return dp[i][buy]
        # dp = [[0 for _ in range(2)] for _ in range(n+1)]
        prev = [0 for _ in range(2)]
        cur = [0 for _ in range(2)]
        # return solve(0,1)
        for i in range(n-1,-1,-1):
            cur[1] = max(-prices[i] + prev[0],prev[1])
            cur[0] = max(prices[i] - fee + prev[1],prev[0])
            prev = cur
        return prev[1]