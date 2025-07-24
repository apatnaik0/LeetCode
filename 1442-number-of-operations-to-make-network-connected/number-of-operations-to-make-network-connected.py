class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [0]*n

    def findParent(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return False
        elif self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1

        ds = DisjointSet(n)
        extra = 0
        for u,v in connections:
            if ds.unionBySize(u,v) == False:
                extra += 1

        comps = sum(1 for i in range(n) if ds.findParent(i)==i)

        return comps-1 if extra>= comps-1 else -1