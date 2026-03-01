class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        n = len(s)
        ans = 0
        l = 0
        r = 0

        while r < n:
            if s[r] in hmap:
                l = max(l, hmap[s[r]] + 1)
            hmap[s[r]] = r
            ans = max(ans,r-l+1)
            r += 1
            
        
        return ans