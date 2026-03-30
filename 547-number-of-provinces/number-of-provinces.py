class Solution:
    def dfs(self,vis,adj,i):
        vis[i] = True
        for j in adj[i]:
            if not vis[j]:
                self.dfs(vis,adj,j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    # adj.append(j)
        
        vis = [False]*n
        provinces = 0

        for i in range(n):
            if not vis[i]:
                self.dfs(vis,adj,i)
                provinces += 1
        
        return provinces