class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        s = 0

        n1 = len(a)
        n2 = len(b)

        n = min(n1,n2)

        ans = ''

        for i in range(n):
            v1 = int(a[n1-i-1])
            v2 = int(b[n2-i-1])
            s = (v1 ^ v2) ^ c
            c = (v1 & v2) | (v1 & c) | (v2 & c)
            ans = str(s) + ans

        # print(ans)
        
        while n1>n:
            v1 = int(a[n1-n-1])
            s = v1 ^  c
            c = v1 & c
            ans = str(s) + ans
            # print(ans)
            n += 1
        
        
        while n2 > n:
            v2 = int(b[n2-n-1])
            s = v2 ^ c
            c = v2 & c
            ans = str(s) + ans
            n += 1
        
        if c:
            ans = str(c) + ans
        
        return ans
