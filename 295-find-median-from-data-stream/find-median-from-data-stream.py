class MedianFinder:

    def __init__(self):
        self.low_pq = []
        self.high_pq = []

    def addNum(self, num: int) -> None:
        heappush(self.low_pq, -num)
        heappush(self.high_pq, -heappop(self.low_pq))
        if len(self.high_pq) > len(self.low_pq):
            heappush(self.low_pq, -heappop(self.high_pq))
        
    def findMedian(self) -> float:
        if len(self.low_pq)>len(self.high_pq):
            return -self.low_pq[0]
        else:
            return (-self.low_pq[0]+self.high_pq[0])/2
    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()