class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        newimage = image[:]
        old = image[sr][sc]
        if old == color:
            return image
        n = len(image)
        m = len(image[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        newimage[sr][sc] = color
        q.append((sr,sc))
        delr = [0,0,1,-1]
        delc = [1,-1,0,0]

        while q:
            l = len(q)
            for _ in range(l):
                r,c = q.popleft()
                
                for d in range(4):
                    nr = r + delr[d]
                    nc = c + delc[d]

                    if 0 <= nr < n and 0<= nc < m and vis[nr][nc]==0 and newimage[nr][nc] == old:
                        newimage[nr][nc] = color
                        q.append((nr,nc))
                        vis[nr][nc] = 1
        return newimage
                
