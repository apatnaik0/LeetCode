class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # p=0
        # bp=prices[0]
        # for i in prices:
        #     if i>bp:
        #         p+= i-bp
        #     bp = i
        # return p
        def solve(i,buy):
            if i == n:
                return 0
            if dp[i][buy]!=0:
                return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i]+solve(i+1,0),solve(i+1,1))
            else:
                dp[i][buy] = max(prices[i]+solve(i+1,1),solve(i+1,0))
            return dp[i][buy]
        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n+1)]
        nxt = [0 for _ in range(2)]
        cur = [0 for _ in range(2)] 
        # return solve(0,1)
        for i in range(n-1,-1,-1):
            cur[1] = max(-prices[i]+nxt[0],nxt[1])
            cur[0] = max(prices[i]+nxt[1],nxt[0])
            nxt = cur
        return nxt[1]

        