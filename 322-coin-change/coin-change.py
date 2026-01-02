class Solution:
    def solve(self,dp,coins,i,amt):
        if i == 0:
            if amt % coins[i] == 0:
                return amt // coins[i]
            else:
                return float('inf')
        
        if dp[i][amt]!=0:
            return dp[i][amt]
        
        pick = float('inf')
        if amt >= coins[i]:
            pick = 1+self.solve(dp,coins,i,amt-coins[i])
        not_pick = self.solve(dp,coins,i-1,amt)
        
        dp[i][amt] = min(pick,not_pick)
        return dp[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        ans = self.solve(dp,coins,n-1,amount)

        for amt in range(amount+1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt // coins[0]
            else:
                dp[0][amt] = float('inf')
        
        for i in range(1,n):
            for amt in range(amount+1):
                pick = float('inf')
                if amt >= coins[i]:
                    pick = 1+dp[i][amt-coins[i]]
                not_pick = dp[i-1][amt]
                
                dp[i][amt] = min(pick,not_pick)

        if dp[n-1][amt] >= float('inf'):
            return -1
        else:
            return dp[n-1][amt]