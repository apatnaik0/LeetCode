class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        hmap = {}
        for i,j in zip(basket1,basket2):
            hmap[i] = hmap.get(i,0)+1
            hmap[j] = hmap.get(j,0)+1
        
        for i in hmap.values():
            if i & 1:
                return -1

        swap = []
        hmap1 = {}
        for i in basket1:
            hmap1[i] = hmap1.get(i,0)+1

        for fruit, ct in hmap.items():
            t = ct//2
            diff = abs(hmap1.get(fruit,0) - t)
            for i in range(diff):
                swap.append(fruit)
        
        swap.sort()
        cost = 0
        swaps = len(swap)//2
        mini = min(hmap.keys())
        for i in range(swaps):
            cost += min(swap[i],2*mini)
        return cost