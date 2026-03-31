class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        pq = []

        hmap = defaultdict(int)

        for word in words:
            hmap[word] += 1
        
        for key,val in hmap.items():
            heappush(pq,(-val,key))
        
        ans = []
        for _ in range(k):
            ans.append(heappop(pq)[1])
        
        return ans