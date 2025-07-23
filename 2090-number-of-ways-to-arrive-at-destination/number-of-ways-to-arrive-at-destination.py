from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append([v, t])
            adj[v].append([u, t])

        q = [[0, 0]]  # (time, node)
        time = [float('inf')] * n
        ways = [0] * n
        time[0] = 0
        ways[0] = 1
        mod = 10**9 + 7

        while q:
            t, node = heappop(q)

            for v, t_ in adj[node]:
                if t + t_ < time[v]:
                    time[v] = t + t_
                    heappush(q, [t + t_, v])
                    ways[v] = ways[node]
                elif t + t_ == time[v]:
                    ways[v] = (ways[v] + ways[node]) % mod

        return ways[n - 1]
