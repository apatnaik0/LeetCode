class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k-1+maxPts:
            return 1.0
        dp = [0]*(n+1)
        windowsum = 1.0
        dp[0]=1.0
        result = 0.0
        for i in range(1,n+1):
            prob = windowsum/maxPts
            if i<k:
                windowsum += prob
            else:
                result += prob
            if i>=maxPts:
                windowsum -= dp[i%maxPts]
            dp[i%maxPts] = prob
        return result