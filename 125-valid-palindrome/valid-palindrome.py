class Solution:
    def isPalindrome(self, s: str) -> bool:

        def rec(i):
            if i>=n[0]//2:
                return True
            if st[i]!=st[n[0]-i-1]:
                return False
            return rec(i+1)
        st = ''.join(c.lower() for c in s if c.isalnum())
        n = [len(st)]
        return rec(0)
        
        