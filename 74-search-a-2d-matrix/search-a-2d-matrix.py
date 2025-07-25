class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows*cols-1
        while low<=high:
            mid = (low+high)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high = mid-1
            else:
                low = mid+1
        return False
        