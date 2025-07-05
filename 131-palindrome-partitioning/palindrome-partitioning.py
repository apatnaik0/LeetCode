class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(s):
            l = 0
            r = len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def solve(ind):
            if ind == len(s):
                ans.append(sub[:])
                return
            for i in range(ind,len(s)):
                if ispalin(s[ind:i+1]):
                    sub.append(s[ind:i+1])
                    solve(i+1)
                    sub.pop()

        sub = []
        ans = []
        solve(0)
        return ans
        