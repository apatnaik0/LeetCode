class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)
        # dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        prev = [0 for _ in range(n2+1)]

        # for i in range(n1+1):
        #     dp[i][0] = i
        for i in range(n2+1):
            prev[i] = i



        for i in range(1,n1+1):
            cur = [0 for _ in range(n2+1)]
            cur[0] = i
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = 1 + min(prev[j-1], cur[j-1], prev[j])
            prev = cur
        return prev[n2]
    