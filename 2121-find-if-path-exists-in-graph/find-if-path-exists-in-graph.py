class Solution:
    def dfs(self,source,graph, destination,visited):
        if source == destination:
            return True
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor not in visited:
                if self.dfs(neighbor,graph,destination,visited):
                    return True
        return False


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(source,graph,destination,visited)
        