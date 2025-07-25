class disjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def findParent(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        elif self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = disjointSet(n*n)
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        mx = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col]==1:
                    # print(row,col)
                    for d in range(4):
                        nrow = row + dr[d]
                        ncol = col + dc[d]
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                            onode = row*n + col
                            nnode = nrow*n + ncol
                            # print(onode,nnode)
                            ds.unionBySize(onode,nnode)
        # print(ds.parent, ds.size)
        
        for row in range(n):
            for col in range(n):
                if grid[row][col]==0:
                    neighbors = set()
                    for d in range(4):
                        nrow = row + dr[d]
                        ncol = col + dc[d]
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                            nnode = nrow*n + ncol
                            neighbors.add(ds.findParent(nnode))
                    s = 0
                    # print(neighbors)
                    for i in neighbors:
                        s += ds.size[i]
                    mx = max(mx,s+1)
                    # print(mx)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    mx = max(mx,ds.size[ds.findParent(row*n+col)])
        
        return mx
                           
            

