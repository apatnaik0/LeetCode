class Solution:
    def ed(self,x,y,positions):
        ans = 0
        for i,j in positions:
            ans += ((i-x)**2+(j-y)**2)**0.5
        return ans

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x = sum(x for x,y in positions)/(len(positions))
        y = sum(y for x,y in positions)/(len(positions))
        ans = self.ed(x,y,positions)
        st = 100
        while st > 1e-6:
            for dx,dy in (-1,0),(0,-1),(0,1),(1,0):
                nx = x + st*dx
                ny = y + st*dy
                nd = self.ed(nx,ny,positions)
                if nd<ans:
                    ans = nd
                    x = nx
                    y = ny
                    break
            else:
                st /= 2
        return self.ed(x,y,positions)