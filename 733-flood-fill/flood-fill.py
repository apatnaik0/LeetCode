class Solution:

    def bfs(self,sr,sc,color,old,newimage,n,m,vis):
        q = deque()
        q.append([sr,sc])
        vis[sr][sc]=1
        delc = [0,1,0,-1]
        delr = [-1,0,1,0]
        while q:
            node = q.popleft()
            newimage[node[0]][node[1]] = color
            for i in range(4):
                if node[0]+delr[i]>=0 and node[0]+delr[i]<n and node[1]+delc[i]>=0 and node[1]+delc[i]<m and newimage[node[0]+delr[i]][node[1]+delc[i]]==old and vis[node[0]+delr[i]][node[1]+delc[i]]!=1:
                    q.append([node[0]+delr[i],node[1]+delc[i]])
                    vis[node[0]+delr[i]][node[1]+delc[i]]=1
        return newimage


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        newimage = image[:]
        n = len(newimage)
        m = len(newimage[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        return self.bfs(sr,sc,color,old,newimage,n,m,vis)
        