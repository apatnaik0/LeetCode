class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        l = 0
        r = 0
        n = len(s)
        ans = 0

        while r < n:
            hmap[s[r]] += 1
            while hmap[s[r]] > 2:
                hmap[s[l]] -= 1
                l += 1
            r += 1
            ans = max(ans,r-l)
        
        return ans
            