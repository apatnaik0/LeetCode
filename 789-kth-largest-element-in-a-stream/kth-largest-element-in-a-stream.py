class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.cap = k
        for num in nums:
            heappush(self.pq,num)
            if len(self.pq) > self.cap:
                heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq,val)
        if len(self.pq) > self.cap:
            heappop(self.pq)
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)