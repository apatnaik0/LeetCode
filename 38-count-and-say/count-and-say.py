class Solution:
    def rle(self, n):
        if n == '0':
            return '1'
        ans = ''
        prev = n[0]
        ct = 1
        for i in range(1,len(n)):
            if prev == n[i]:
                ct+=1
            else:
                ans += str(ct)+prev
                prev = n[i]
                ct = 1
        
        ans += str(ct)+prev 
        return ans
        


    def countAndSay(self, n: int) -> str:
        ans = ''
        rle = '0'
        for i in range(n):
            rle = self.rle(rle)
            print(rle)
        return rle
            
        