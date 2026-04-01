class Solution:

    def helper(self,dp,n,coins,amount,i):

        if i == 0:
            if amount % coins[i] == 0:
                return amount//coins[i]
            else:
                return float('inf')

        if dp[i][amount]!=0:
            return dp[i][amount]

        pick = float('inf')
        if coins[i] <= amount:
            pick = 1 + self.helper(dp,n,coins,amount-coins[i],i)
        notpick = self.helper(dp,n,coins,amount,i-1)

        dp[i][amount] = min(pick,notpick)

        return dp[i][amount]



    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]

        ans = self.helper(dp,n,coins,amount,n-1)

        if ans >= float('inf'):
            return -1
        else:
            return ans