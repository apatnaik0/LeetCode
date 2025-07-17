class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for i in prerequisites:
            adj[i[1]].append(i[0])
            indegree[i[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i]==0:
                    q.append(i)
        
        return len(topo) == numCourses

        

        