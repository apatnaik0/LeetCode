class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        neighbors = defaultdict(list)
        ans = []

        for i,j in prerequisites:
            indegree[i] += 1
            neighbors[j].append(i)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return True if len(ans) == numCourses else False
