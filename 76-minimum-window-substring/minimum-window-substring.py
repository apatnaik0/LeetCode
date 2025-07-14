class Solution:
    def minWindow(self, s: str, t: str) -> str:
        thash = {}
        for i in t:
            thash[i] = thash.get(i,0) + 1
        
        l = 0
        r = 0
        ind = -1
        mini = float('inf')
        ct = 0
        while r<len(s):
            if thash.get(s[r],0)>0:
                ct += 1
            thash[s[r]] = thash.get(s[r],0) - 1
            while ct==len(t):
                if r-l+1<mini:
                    mini = r-l+1
                    ind = l
                thash[s[l]] = thash.get(s[l],0) + 1
                if thash[s[l]]>0:
                    ct-=1
                l+=1
            r+=1
        return "" if ind == -1 else s[ind:ind+mini]
            