class Solution:
    def dfs(self, graph, color, i, n , col):
        color[i] = col
        for k in graph[i]:
            if color[k] == 0:
                if self.dfs(graph,color,k,n,col*-1) == False:
                    return False
            elif color[k] == color[i]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0 for _ in range(n)]
        for i in range(n):
            if color[i] == 0:
                if self.dfs(graph, color, i, n, 1) == False:
                    return False
        return True