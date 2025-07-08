class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n= len(coins)
        def solve(ind,target):
            if ind == 0:
                if target == 0:
                    return 1
                if target%coins[0]==0:
                    return 1
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            notpick = solve(ind-1,target)
            pick = 0
            if target>=coins[ind]:
                pick = solve(ind,target-coins[ind])
            dp[ind][target] = pick + notpick
            return dp[ind][target]
        dp = [[-1 for i in range(amount+ 1)] for j in range(n)]
        return solve(n-1,amount)