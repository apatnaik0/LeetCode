class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n+1)]
        def solve(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i] + solve(i+1,0), solve(i+1,1))
            else:
                dp[i][buy] = max(prices[i] + solve(i+2,1), solve(i+1,0))
            return dp[i][buy]
        return solve(0,1)