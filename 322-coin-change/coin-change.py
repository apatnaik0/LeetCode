class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # def solve(ind,target):
        #     if ind == 0:
        #         if target%coins[ind]==0:
        #             return target//coins[ind]
        #         return 1e9
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     pick = 1e9
        #     if target>=coins[ind]:
        #         pick = 1 + solve(ind,target-coins[ind])
        #     notpick = solve(ind-1,target)
        #     dp[ind][target] = min(pick,notpick)
        #     return dp[ind][target]
        
        prev = [-1 for _ in range(amount+1)]
        # ans = solve(n-1,amount)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i] = i//coins[0]
            else:
                prev[i] = 1e9
        for i in range(1,n):
            cur = [-1 for _ in range(amount+1)]
            for j in range(amount+1):
                pick = 1e9
                if j>=coins[i]:
                    pick = 1 + cur[j-coins[i]]
                notpick = prev[j]
                cur[j] = min(pick,notpick)
            prev = cur
        if prev[amount]>=1e9:
            return -1
        return prev[amount]
            