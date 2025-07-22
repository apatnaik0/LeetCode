class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        price = [1e9]*n
        price[src]=0
        q.append([0,src,0])
        adj = [[] for _ in range(n)]
        for i in flights:
            adj[i[0]].append([i[1],i[2]])
        while q:
            stops, node, cost = q.popleft()
            if stops>k:
                continue
            for i in adj[node]:
                nxt = i[0]
                dist = i[1]
                if cost + dist < price[nxt] and stops<=k:
                    price[nxt] = cost + dist
                    q.append([stops+1,i[0],cost + dist])
        if price[dst] == 1e9:
            return -1
        else:
            return price[dst]
