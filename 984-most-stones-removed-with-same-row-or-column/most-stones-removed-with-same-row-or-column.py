class disjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def findParent(self, node):
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
    def removeStones(self, stones: List[List[int]]) -> int:
        mrow = 0
        mcol = 0
        n = len(stones)
        for i,j in stones:
            mrow = max(mrow,i)
            mcol = max(mcol,j)
        ds = disjointSet(mrow+mcol+2)
        for i,j in stones:
            row = i
            col = mrow + j + 1
            ds.unionBySize(row,col)
        ct = 0
        for i in range(mrow+mcol+2):
            if ds.parent[i] == i and ds.size[i]>1:
                ct += 1
        return n-ct
