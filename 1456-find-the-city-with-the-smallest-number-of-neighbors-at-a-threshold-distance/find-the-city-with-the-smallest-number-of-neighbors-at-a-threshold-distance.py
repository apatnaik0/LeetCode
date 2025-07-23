class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[1e9 for _ in range(n)] for _ in range(n)]
        for u,v,w in edges:
            adj[u][v] = w
            adj[v][u] = w

        for i in range(n):
            adj[i][i] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[via][j] == 1e9 or adj[i][via] == 1e9:
                        continue
                    adj[i][j] = min(adj[i][j], adj[i][via] + adj[via][j])
        
        ansct = 1e9
        anscity = -1
        for i in range(n):
            ct = 0
            for j in range(n):
                if adj[i][j]<=distanceThreshold:
                    ct+=1
            if ct<=ansct:
                ansct = ct
                anscity = i
        print(adj)
        return anscity
        