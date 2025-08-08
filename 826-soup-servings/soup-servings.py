class Solution:
    def solve(self,a,b,dp):
        if a <= 0 and b > 0:
            return 1.0
        if a <= 0 and b <= 0:
            return 0.5
        if a > 0 and b <= 0:
            return 0.0
        
        if dp[a][b] != -1:
            return dp[a][b]
        
        o1 = 0.25 * self.solve(a-4,b,dp)
        o2 = 0.25 * self.solve(a-3,b-1,dp)
        o3 = 0.25 * self.solve(a-2,b-2,dp)
        o4 = 0.25 * self.solve(a-1,b-3,dp)

        dp[a][b] = o1 + o2 + o3 + o4
        return dp[a][b]

    def soupServings(self, n: int) -> float:
        if n>4450:
            return 1.0
        n=(n+24)//25
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.solve(n,n,dp)