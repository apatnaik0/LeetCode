class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def histogram(psum):
            st = []
            area = 0
            for i in range(len(psum)):
                while st and psum[i]<psum[st[-1]]:
                    bar = psum[st.pop()]
                    pse = st[-1] if st else -1
                    nse = i
                    area = max(area,(bar*(nse-pse-1)))
                st.append(i)
            while st :
                bar = psum[st.pop()]
                pse = st[-1] if st else -1
                nse = len(psum)
                area = max(area,(bar*(nse-pse-1)))
            return area

        nrow = len(matrix)
        ncol = len(matrix[0])
        psum = [0]*len(matrix[0])
        maxarea = 0
        for row in range(nrow):
            for col in range(ncol):
                if matrix[row][col]=='0':
                    psum[col] = 0
                elif matrix[row][col]=='1':
                    psum[col] += 1
            maxarea = max(maxarea,histogram(psum))

        return maxarea


