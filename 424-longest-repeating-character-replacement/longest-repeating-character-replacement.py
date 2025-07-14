class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        vis = [0]*26
        l = 0
        r = 0
        mf = 0
        ml = 0
        while r<n:
            vis[ord(s[r])-ord('A')] += 1
            mf = max(mf,vis[ord(s[r])-ord('A')])
            if r-l+1 - mf > k:
                vis[ord(s[l])-ord('A')] -= 1
                l+=1
            else:
                ml = max(ml,r-l+1)
            r += 1
        return ml
