class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        def palin(st):
            l = 0
            r = len(st)-1
            while l<r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True

        def solve(i,j):
            # print('func start')
            # print(i,j)
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            mini = float('inf')
            for k in range(i,j+1):
                if palin(s[i:k+1]):
                    # print('ispalin',s[i:k+1])
                    # print(i,k)
                    # dp[i] = 1 + solve(k+1,j)
                    mini = min(mini,1 + solve(k+1,j))
                    # print(mini)
            dp[i] = mini
            # print('func end')
            return dp[i]
            

        dp = [0 for _ in range(n+1)]
        # return solve(0,n-1)-1

        for i in range(n-1,-1,-1):
            mini = float('inf')
            for j in range(i,n):
                # if palin(s[i:j+1]):
                # print(s[i:j+1],s[j:i-1:-1])
                if s[i:j+1] == s[i:j+1][::-1]:
                    mini = min(mini,1 + dp[j+1])
            dp[i] = mini
        return dp[0]-1
                
                