class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        topo = []
        indegree = [0] * numCourses
        for i in prerequisites:
            course = i[0]
            prereq = i[1]
            adj[prereq].append(course)
            indegree[course]+=1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)

        while q:
            node = q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i]==0:
                    q.append(i)
        
        return topo if len(topo)==numCourses else []
        