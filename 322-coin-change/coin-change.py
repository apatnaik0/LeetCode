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

        # ans = self.helper(dp,n,coins,amount,n-1)

        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float('inf')

        for i in range(1,n):
            for j in range(amount+1):
                pick = float('inf')
                if coins[i]<=j:
                    pick = 1 + dp[i][j-coins[i]]
                notpick = dp[i-1][j]
                dp[i][j] = min(pick,notpick)
        if dp[n-1][amount] >= float('inf'):
            return -1
        return dp[n-1][amount]

        # if ans >= float('inf'):
        #     return -1
        # else:
        #     return ans