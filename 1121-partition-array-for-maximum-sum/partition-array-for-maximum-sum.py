class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        def solve(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            l = 0
            maxisum = float('-inf')
            maxi = float('-inf')
            for ind in range(i,min(n,i+k)):
                l+=1
                maxi = max(maxi,arr[ind])
                maxisum = max(maxisum, l*maxi + solve(ind+1))
            dp[i] = maxisum
            return dp[i]

        n = len(arr)
        dp = [-1 for _ in range(n)]
        return solve(0)