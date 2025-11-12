class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        
        pq = []
        for i,j in hmap.items():
            heappush(pq,(j,i))
        
        n = len(pq)
        ind = n - k
        ans = []
        for i in range(ind):
            heappop(pq)
        
        ans = []
        for i in range(k):
            ans.append(pq[i][1])
        return ans
