class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hmap = {}
        l = 0
        ans = 0

        for r in range(n):
            if s[r] in hmap:
                l = max(l,hmap[s[r]]+1)
            hmap[s[r]] = r
            ans = max(ans,r-l+1)

        return ans
