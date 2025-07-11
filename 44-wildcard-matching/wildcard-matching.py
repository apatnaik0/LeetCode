class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        # dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        prev = [False for _ in range(n2+1)]
        # def solve(i,j):
        #     if j==0 and i==0:
        #         return True
        #     elif j==0 and i>0:
        #         return False
        #     elif j>0 and i==0:
        #         while j>0:
        #             if p[j-1]!='*':
        #                 return False
        #             j-=1
        #         return True 
        #     if dp[i][j]!=0:
        #         return dp[i][j]
        #     if s[i-1]==p[j-1] or p[j-1]=='?':
        #         dp[i][j] = solve(i-1,j-1)
        #     elif p[j-1]=='*':
        #         dp[i][j] = solve(i-1,j) or solve(i,j-1)
        #     else:
        #         return False
        #     return dp[i][j]

        # return solve(n1,n2)
        prev[0] = True
        # for i in range(1,n1+1):
        #     dp[i][0] = False
        for j in range(1, n2 + 1):
            if p[j - 1] != '*':
                break
            else:
                prev[j] = True
                
        
        for i in range(1,n1+1):
            cur = [False for _ in range(n2+1)]
            for j in range(1,n2+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    cur[j] = prev[j-1]
                elif p[j-1]=='*':
                    cur[j] = prev[j] or cur[j-1]
                else:
                    cur[j] = False
            prev = cur
        return prev[n2]
