class Solution:
    def rec(self,i,sub,ans,a,t):
        if t == 0:
            ans.append(sub[:])
            return ans
                
        for ix in range(i,len(a)):
            if ix>i and a[ix]==a[ix-1]:
                continue
            if a[ix]<=t:
                sub.append(a[ix])
                self.rec(ix+1,sub,ans,a,t-a[ix])
                sub.pop()
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub = []
        i = 0
        candidates.sort()
        ans = self.rec(i,sub,ans,candidates, target)
        return ans