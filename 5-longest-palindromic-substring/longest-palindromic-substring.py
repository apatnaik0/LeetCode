class Solution:
    def expand(self,s,l,r):
        while l>=0 and r <len(s) and s[l]==s[r]:
            l -= 1
            r += 1

        return s[l+1:r]
            
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        ans = ""

        for i in range(n):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)

            if len(odd)>len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even

        return ans