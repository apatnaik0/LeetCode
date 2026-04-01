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
        # dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        prev = [0 for _ in range(amount+1)]

        # ans = self.helper(dp,n,coins,amount,n-1)

        for i in range(amount+1):
            if i%coins[0] == 0:
                prev[i] = i//coins[0]
            else:
                prev[i] = float('inf')

        for i in range(1,n):
            cur = [0 for _ in range(amount+1)]
            for j in range(amount+1):
                pick = float('inf')
                if coins[i]<=j:
                    pick = 1 + cur[j-coins[i]]
                notpick = prev[j]
                cur[j] = min(pick,notpick)
            prev = cur
        if prev[amount] >= float('inf'):
            return -1
        return prev[amount]

        # if ans >= float('inf'):
        #     return -1
        # else:
        #     return ans