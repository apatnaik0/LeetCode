class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x,y in points:
            dist = sqrt(x**2 + y**2)
            heappush(pq,(-dist,[x,y]))
            if len(pq) > k:
                heappop(pq)

        ans = []
        while pq:
            ans.append(heappop(pq)[1])

        return ans