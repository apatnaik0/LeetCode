class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque()
        dist = [[-1 for _ in range(n)] for _ in range(m)]

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        # Start BFS from all 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0

        while q:
            r, c = q.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist