class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        maxdiag = 0
        for i,j in dimensions:
            diag = (i**2+j**2)**0.5
            if diag > maxdiag:
                maxdiag = diag
                ans = i*j
            elif diag == maxdiag:
                ans = max(i*j,ans)
        return ans