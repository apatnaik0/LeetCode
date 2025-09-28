class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rmap = defaultdict(int)
        cmap = defaultdict(int)
        hmap = {}
        for i in range(n):
            for j in range(m):
                hmap[mat[i][j]] = (i,j)
        
        for i in range(len(arr)):
            r,c = hmap[arr[i]]
            rmap[r] += 1
            cmap[c] += 1
            if rmap[r]==m or cmap[c]==n:
                return i
        
