class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        q_pacific = deque()
        q_atlantic = deque()

        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            q_pacific.append((i, 0))
            pacific.add((i, 0))

            q_atlantic.append((i, n - 1))
            atlantic.add((i, n - 1))

        for j in range(n):
            q_pacific.append((0, j))
            pacific.add((0, j))

            q_atlantic.append((m - 1, j))
            atlantic.add((m - 1, j))

        while q_pacific:
            l = len(q_pacific)
            for _ in range(l):
                r,c = q_pacific.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0<= nr < m and 0<= nc <n and (nr,nc) not in pacific and heights[nr][nc] >= heights[r][c]:
                        pacific.add((nr,nc))
                        q_pacific.append((nr,nc))

        while q_atlantic:
            l = len(q_atlantic)
            for _ in range(l):
                r,c = q_atlantic.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0<= nr < m and 0<= nc <n and (nr,nc) not in atlantic and heights[nr][nc] >= heights[r][c]:
                        atlantic.add((nr,nc))
                        q_atlantic.append((nr,nc))
        
        return list(pacific.intersection(atlantic))
        
