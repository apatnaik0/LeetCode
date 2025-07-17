class Solution:
    def bfs(self,i,n,graph,color):
        q = deque()
        color[i] = 1
        q.append(i)
        while q:
            node = q.popleft()
            for k in graph[node]:
                if color[k]==0:
                    q.append(k)
                    color[k] = -1*color[node]
                elif color[k]==color[node]:
                    return False
        return True

    def dfs(self,i,n,graph,color,col):
        color[i] = col
        for k in graph[i]:
            if color[k]==0:
                if self.dfs(k,n,graph,color,col*-1) == False:
                    return False
            elif color[k]==color[i]:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        for i in range(n):
            if color[i]==0:
                if self.dfs(i,n,graph,color,1) == False:
                    return False
        return True