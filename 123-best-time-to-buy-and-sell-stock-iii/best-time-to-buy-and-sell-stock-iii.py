class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for k in range(1,3):
                dp[i][1][k] = max(-prices[i]+dp[i+1][0][k],dp[i+1][1][k])
                dp[i][0][k] = max(prices[i]+dp[i+1][1][k-1],dp[i+1][0][k])
        return dp[0][1][2]