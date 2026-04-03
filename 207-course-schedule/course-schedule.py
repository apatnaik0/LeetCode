class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = defaultdict(list)
        topo = []

        for i,j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                topo.append(i)

        while q:
            course = q.popleft()
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    topo.append(neighbor)

        return True if len(topo) == numCourses else False