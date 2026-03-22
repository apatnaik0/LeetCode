class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        l = 0
        maxi = 0
        n = len(s)

        for r in range(n):
            if s[r] in hmap:
                l = max(l,hmap[s[r]] + 1)
            hmap[s[r]] = r
            maxi = max(maxi,r-l+1)
        
        return maxi
