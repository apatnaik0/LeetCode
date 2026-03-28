class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heappush(pq,-stone)

        while len(pq) > 1:
            y = -heappop(pq)
            x = -heappop(pq)

            if x != y:
                heappush(pq,-(y-x))
        
        return -heappop(pq) if len(pq)!=0 else 0


