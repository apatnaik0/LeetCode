class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        n = len(image)
        m = len(image[0])
        q = deque()
        q.append((sr,sc))
        old_color = image[sr][sc]
        image[sr][sc] = color
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        while q:
            r,c = q.popleft()
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    q.append((nr,nc))
        
        return image
