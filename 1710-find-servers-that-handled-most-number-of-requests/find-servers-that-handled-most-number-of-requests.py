class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))
        busy = []
        ans = [0]*k

        for i,a in enumerate(arrival):
            while busy and busy[0][0] <= a:
                j, x = heappop(busy)
                heappush(free, i + (x-i)%k)
            
            if free:
                server = heappop(free) % k
                heappush(busy, (a + load[i],server))
                ans[server] += 1
        
        a = max(ans)
        return [ i for i in range(k) if ans[i] == a]
        