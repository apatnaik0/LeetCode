class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        visited = [[0] * n for _ in range(m)]
        pq = []

        for i in range(m):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = 1

        for j in range(n):
            heapq.heappush(pq, (heightMap[0][j], 0, j))
            heapq.heappush(pq, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = 1

        res = 0
        dirs = [1, 0, -1, 0, 1]

        while pq:
            h, x, y = heapq.heappop(pq)
            for k in range(4):
                nx, ny = x + dirs[k], y + dirs[k+1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if heightMap[nx][ny] < h:
                        res += h - heightMap[nx][ny]
                    heapq.heappush(pq, (max(heightMap[nx][ny], h), nx, ny))
        return res