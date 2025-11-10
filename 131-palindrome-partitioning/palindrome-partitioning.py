class Solution:
    def rec(self, ind, ans, sub, s):
        if ind == len(s):
            ans.append(sub[:])
            return ans
        
        for i in range(ind,len(s)):
            s1 = s[ind:i+1]
            if s1[:] == s1[::-1]:
                sub.append(s1)
                self.rec(i+1,ans,sub,s)
                sub.pop()
        return ans

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        sub = []
        ans = self.rec(0,ans,sub,s)
        return ans