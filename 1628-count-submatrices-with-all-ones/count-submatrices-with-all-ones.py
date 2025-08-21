class Solution:
    def solve(self,arr):
        st = []
        ct = 0
        for i in range(len(arr)):
            while st and arr[i]<arr[st[-1]]:
                bar = st.pop()
                nse = i - bar
                pse = bar - (st[-1] if st else -1)
                ct += arr[bar] * nse * pse
            st.append(i)
        
        while st:
            bar = st.pop()
            nse = len(arr)-bar
            pse = bar - (st[-1] if st else -1)
            ct += arr[bar] * nse * pse
            
        
        return ct

    def numSubmat(self, mat: List[List[int]]) -> int:
        hist = [0]*len(mat[0])
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    hist[j] += 1
                else:
                    hist[j] = 0
            count += self.solve(hist)
        return count

        


