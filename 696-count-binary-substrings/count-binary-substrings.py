class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = 0
        stk = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                stk += 1
            else:
                prev = stk
                stk = 1
            if stk <= prev:
                ans +=1
        return ans
