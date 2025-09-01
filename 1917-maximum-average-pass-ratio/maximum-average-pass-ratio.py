class Solution:
    def jump(self,p,t):
        return -((p+1)/(t+1)-p/t)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for p,t in classes:
            heappush(pq,(self.jump(p,t),p,t))
        
        for i in range(extraStudents):
            j,p,t = heappop(pq)
            p += 1
            t += 1
            heappush(pq,(self.jump(p,t),p,t))
        
        print(pq)
        ans = 0
        for i in range(len(pq)):
            j,p,t = heappop(pq)
            ans += p/t
        
        return ans/len(classes)


        
        
        