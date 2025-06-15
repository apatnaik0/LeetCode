class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def maxincol(mat,col,n):
            maxi = 0
            ans = -1
            for i in range(n):
                # print(maxi,mat[i][col])
                if maxi < mat[i][col]:
                    maxi = mat[i][col]
                    ans = i
                # print(maxi,i)
            return ans
        nrow = len(mat)
        ncol = len(mat[0])

        low = 0
        high = ncol-1

        while low<=high:
            mid = (low+high)//2
            # print(low,mid,high)
            maxi = maxincol(mat,mid,nrow)
            # print(maxi)
            left = mat[maxi][mid-1] if mid>0 else -1
            right = mat[maxi][mid+1] if mid<ncol-1 else -1
            # print(left,right)
            if mat[maxi][mid]>left and mat[maxi][mid]>right:
                return [maxi,mid]
            elif mat[maxi][mid]>left:
                low = mid+1
            else:
                high = mid-1
        return [-1,-1]
        