class Solution:
    def dfs(self,node,parent,ini,low,timer,vis,adj,ans):
        ini[node] = timer
        low[node] = timer
        vis[node] = 1
        timer += 1
        for i in adj[node]:
            if i!=parent:
                if vis[i]!=1:
                    self.dfs(i,node,ini,low,timer,vis,adj,ans)
                    low[node] = min(low[node],low[i])
                    if low[i] > ini[node]:
                        ans.append([node,i])
                else:
                    low[node] = min(low[node],low[i])   

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i,j in connections:
            adj[i].append(j)
            adj[j].append(i)
        
        ini = [0]*n
        low = [0]*n
        timer = 1
        vis = [0]*n
        ans = []
        self.dfs(0,-1,ini,low,timer,vis,adj,ans)
        return ans