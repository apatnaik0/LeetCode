class Solution:
    def solve(self,word1,word2,n1,n2,i,j,dp):
        if i < 0:
            return j+1
        if j < 0:
            return i+1
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            ans = self.solve(word1,word2,n1,n2,i-1,j-1,dp)
        else:
            ans = 1 + min(self.solve(word1,word2,n1,n2,i-1,j-1,dp),self.solve(word1,word2,n1,n2,i-1,j,dp), self.solve(word1,word2,n1,n2,i,j-1,dp))
        dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]
        # return self.solve(word1,word2,n1,n2,n1-1,n2-1,dp)
        # for i in range(n1+1):
        #     dp[i][0] = i
        prev = [-1 for _ in range(n2+1)]
        for j in range(n2+1):
            prev[j] = j
        
        for i in range(1,n1+1):
            curr = [-1 for _ in range(n2+1)]
            curr[0] = i
            for j in range(1,n2+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j-1],prev[j],curr[j-1])
            prev = curr
        return prev[n2]