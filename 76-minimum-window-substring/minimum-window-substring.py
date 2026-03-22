class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = defaultdict(int)
        for char in t:
            tmap[char] += 1
        ct = len(t)

        n = len(s)
        l = 0
        ans = float('inf')
        
        for r in range(n):
            if s[r] in tmap:
                if tmap[s[r]] > 0:
                    ct -= 1
                tmap[s[r]] -= 1
            
            while ct == 0:

                if r - l + 1 < ans:
                    ans = r-l+1
                    start = l
                
                if s[l] in tmap:
                    tmap[s[l]] += 1
                    if tmap[s[l]] > 0:
                        ct += 1
                
                l += 1

        return "" if ans == float('inf') else s[start:start+ans]