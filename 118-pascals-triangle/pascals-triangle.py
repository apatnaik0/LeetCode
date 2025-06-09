class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def row(n):
            ans = [1]
            val = 1
            for i in range(1,n):
                val = val * (n-i)
                val = val // i
                ans.append(val)
            return ans

        fin_ans=[]
        for i in range(1,numRows+1):
            fin_ans.append(row(i))
        return fin_ans

            
        