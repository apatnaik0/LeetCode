class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            vis[i]=True
            for j in graph[i]:
                if not vis[j]:
                    dfs(j)

        n = len(isConnected)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        vis = [False]*n
        provinces = 0

        for i in range(n):
            if not vis[i]:
                dfs(i)
                provinces += 1
        
        return provinces