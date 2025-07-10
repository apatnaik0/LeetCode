class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def comp(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            i = 0
            j = 0
            while(i<len(s1)):
                if j<len(s2) and s1[i]==s2[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            return i==len(s1) and j==len(s2)

        words.sort(key=len)
        n = len(words)
        dp = [1]*n
        maxi = 1
        for i in range(1,n):
            for j in range(i):
                if comp(words[i],words[j]) and 1 + dp[j] > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i]>maxi:
                maxi = dp[i]
        return maxi