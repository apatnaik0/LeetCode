class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        hmap = {}

        for i in range(len(rains)):
            if rains[i]>0:
                if rains[i] not in hmap:
                    hmap[rains[i]] = []
                hmap[rains[i]].append(i)

        heap = []
        ans = [-1]*len(rains)
        visit = set()

        for i in range(len(rains)):
            if rains[i]>0:
                if rains[i] in visit:
                    return []
                else:
                    visit.add(rains[i])
                    hmap[rains[i]].pop(0)
                    if hmap[rains[i]]:
                        heapq.heappush(heap, [hmap[rains[i]][0], rains[i]])
            elif rains[i] == 0:
                if heap:
                    next_occur, lake = heapq.heappop(heap)
                    ans[i] = lake
                    visit.remove(lake)
                else:
                    ans[i] = 1

        return ans