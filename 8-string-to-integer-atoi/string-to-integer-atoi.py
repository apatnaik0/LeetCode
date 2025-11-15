class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        maxi = 2**31 - 1
        mini = -2**31

        i = 0
        n = len(s)

        while i<n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0

        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit

            if sign * res <= mini:
                return mini
            if sign * res >= maxi:
                return maxi
            
            i += 1
        
        return res*sign
