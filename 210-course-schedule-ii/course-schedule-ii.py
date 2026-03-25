class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        ans = []
        adj = [[] for _ in range(numCourses)]

        n = len(prerequisites)
        for i,j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        
        while q:
            cur = q.popleft()
            ans.append(cur)
            for neighbour in adj[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return ans if len(ans) == numCourses else []
