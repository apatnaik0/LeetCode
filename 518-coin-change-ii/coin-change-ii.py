class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n= len(coins)
        # def solve(ind,target):
        #     if ind == 0:
        #         if target == 0:
        #             return 1
        #         if target%coins[0]==0:
        #             return 1
        #         return 0
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     notpick = solve(ind-1,target)
        #     pick = 0
        #     if target>=coins[ind]:
        #         pick = solve(ind,target-coins[ind])
        #     dp[ind][target] = pick + notpick
        #     return dp[ind][target]
        dp = [[0 for i in range(amount+ 1)] for j in range(n)]
        # return solve(n-1,amount)
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(1,n):
            for j in range(amount+1):
                notpick = dp[i-1][j]
                pick = 0
                if j>=coins[i]:
                    pick = dp[i][j-coins[i]]
                dp[i][j] = pick + notpick
        return dp[n-1][amount]
            