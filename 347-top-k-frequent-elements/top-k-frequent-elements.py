class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1
        
        pq = []
        # print(hmap)

        for key,val in hmap.items():
            heappush(pq,(val,key))
            # print(pq)
            if len(pq) > k:
                heappop(pq)
        
            # print(pq)

        ans = []
        while pq:
            ans.append(heappop(pq)[1])

        return ans