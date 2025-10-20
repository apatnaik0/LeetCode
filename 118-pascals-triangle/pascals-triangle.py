class Solution:
    def row(self,n):
        ans = [1]
        val = 1
        for i in range(1,n):
            val = val * (n-i) // i
            ans.append(val)
        return ans
        
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            r = self.row(i)
            ans.append(r)
        return ans
    