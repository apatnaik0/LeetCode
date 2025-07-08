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
        # dp = [[0 for i in range(amount+ 1)] for j in range(n)]
        prev = [0 for i in range(amount+ 1)] 
        # return solve(n-1,amount)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=1
        for i in range(1,n):
            cur = [0 for i in range(amount+ 1)] 
            for j in range(amount+1):
                notpick = prev[j]
                pick = 0
                if j>=coins[i]:
                    pick = cur[j-coins[i]]
                cur[j] = pick + notpick
            prev = cur
        return prev[amount]
            