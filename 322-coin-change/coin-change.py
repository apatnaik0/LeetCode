class Solution:
    def solve(self,coins,amt,i,dp):
        if i == 0:
            if amt%coins[i] == 0:
                return amt//coins[i]
            else:
                return float('inf')
        if dp[i][amt]!=0:
            return dp[i][amt]
        pick = float('inf')
        if amt >= coins[i]:
            pick = 1+self.solve(coins,amt-coins[i],i,dp)
        not_pick = self.solve(coins,amt,i-1,dp)
        dp[i][amt] = min(pick,not_pick)
        return dp[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        # ans = self.solve(coins,amount,n-1,dp)
        prev = [0 for _ in range(amount+1)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                prev[i] = i//coins[0]
            else:
                prev[i] = float('inf')

        for i in range(1,n):
            curr = [0 for _ in range(amount+1)]
            for j in range(1,amount+1):
                pick = float('inf')
                if j >= coins[i]:
                    pick = 1+curr[j-coins[i]]
                not_pick = prev[j]
                curr[j] = min(pick,not_pick)
            prev = curr
        if prev[amount] >= float('inf'):
            return -1
        else:
            return prev[amount]