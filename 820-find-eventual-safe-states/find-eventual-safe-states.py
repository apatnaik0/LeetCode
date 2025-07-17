class Solution:
    def dfs(self,i,graph,vis,ans,check):
        vis[i]=2
        check[i] = 0
        for j in graph[i]:
            if vis[j]==0:
                if self.dfs(j,graph,vis,ans,check) == True:
                    check[j]=0
                    return True

            elif vis[j]==2:
                check[j]=0
                return True

        check[i] = 1
        vis[i] = 1
        return False
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        vis = [0]*n
        check = [0]*n
        ans = []
        for i in range(n):
            if vis[i]==0:
                self.dfs(i,graph,vis,ans,check)
        ans = []
        for i in range(n):
            if check[i]==1:
                ans.append(i)
        return ans