class Solution:
    def dfs(self,r,c,vis,heights,m,n):
        if (r,c) in vis:
            return
        vis.add((r,c))
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                self.dfs(nr,nc,vis,heights,m,n)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        for row in range(m):
            self.dfs(row,0,pacific,heights,m,n)
            self.dfs(row,n-1,atlantic,heights,m,n)

        for col in range(n):
            self.dfs(0,col,pacific,heights,m,n)
            self.dfs(m-1,col,atlantic,heights,m,n)
        
        return list(pacific & atlantic)