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
        
        o1 = 0.25 * self.solve(a-100,b,dp)
        o2 = 0.25 * self.solve(a-75,b-25,dp)
        o3 = 0.25 * self.solve(a-50,b-50,dp)
        o4 = 0.25 * self.solve(a-25,b-75,dp)

        dp[a][b] = o1 + o2 + o3 + o4
        return dp[a][b]

    def soupServings(self, n: int) -> float:
        if n>4450:
            return 1.0
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.solve(n,n,dp)