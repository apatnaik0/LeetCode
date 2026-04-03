class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1

        heap = []

        for key,val in hmap.items():
            heappush(heap,(val,key))
            if len(heap)>k:
                heappop(heap)

        return list(x[1] for x in heap)