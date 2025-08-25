class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat), len(mat[0])
        i,j = 0,0
        ans = []
        d = 1
        while i<n and j<m:
            ans.append(mat[i][j])
            i = i - d
            j = j + d
            if i < 0 or j >= m:
                d = d*-1
                if j>=m:
                    i += 2
                    j -= 1
                elif i<0:
                    i += 1
            elif i >= n or j < 0:
                d = d*-1
                if i>=n:
                    j += 2
                    i -= 1
                elif j<0:
                    j += 1
        return ans