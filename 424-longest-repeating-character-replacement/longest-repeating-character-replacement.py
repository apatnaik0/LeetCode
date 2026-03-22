class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        max_freq = 0
        n = len(s)
        l = 0
        ans = 0

        for r in range(n):
            hmap[s[r]] += 1
            max_freq = max(max_freq,hmap[s[r]])
            if r - l + 1 - max_freq > k:
                hmap[s[l]] -= 1
                l += 1

            ans = max(ans,r-l+1)
        
        return ans
            