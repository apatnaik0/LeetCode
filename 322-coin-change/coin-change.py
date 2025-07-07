class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        def solve(ind,target):
            if target == 0:
                return 0
            if ind == 0:
                if target%coins[ind]==0:
                    return target//coins[ind]
                return 1e9
            if dp[ind][target]!=-1:
                return dp[ind][target]
            pick = 1e9
            if target>=coins[ind]:
                pick = 1 + solve(ind,target-coins[ind])
            notpick = solve(ind-1,target)
            dp[ind][target] = min(pick,notpick)
            return dp[ind][target]
        
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        ans = solve(n-1,amount)
        if ans>=1e9:
            return -1
        return ans
            