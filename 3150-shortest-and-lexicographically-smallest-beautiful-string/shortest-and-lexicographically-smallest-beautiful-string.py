class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        r = 0
        ct = 0
        ans = ''
        while r <n:
            if s[r] == '1':
                ct += 1
            while k == ct:
                curr = s[l:r+1]

                if (
                    ans == ''
                    or len(curr) < len(ans)
                    or (len(curr) == len(ans) and curr < ans)
                ):
                    ans = s[l:r+1]
                if s[l] == '1':
                    ct -= 1
                l += 1
            r += 1
        
        return ans