class Solution:
    def dfs(self,r,c,vis,m,n,heights):
        if (r,c) in vis:
            return
        vis.add((r,c))
        for nr, nc in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
            if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                self.dfs(nr,nc,vis,m,n,heights)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        for row in range(m):
            self.dfs(row,0,pacific,m,n,heights)
            self.dfs(row,n-1,atlantic,m,n,heights)

        for col in range(n):
            self.dfs(0,col,pacific,m,n,heights)
            self.dfs(m-1,col,atlantic,m,n,heights)

        return list(pacific & atlantic)
