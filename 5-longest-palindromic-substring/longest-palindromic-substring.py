class Solution:
    def efc(self,l,r,s):
        while l>= 0 and r<len(s) and s[l]==s[r]:
            l -=1
            r+=1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        maxi = ''

        for i in range(len(s)-1):
            odd = self.efc(i,i,s)
            even = self.efc(i,i+1,s)

            if len(even) > len(maxi):
                maxi = even
            if len(odd) > len(maxi):
                maxi = odd
        return maxi
