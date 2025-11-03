class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        ml = 0
        vis = [-1]*256
        while r < n:
            if vis[ord(s[r])]!=-1:
                l = max(l, vis[ord(s[r])]+1)
            vis[ord(s[r])]=r
            ml = max(ml,r-l+1)
            r += 1
        return ml