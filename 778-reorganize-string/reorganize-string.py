class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = defaultdict(int)
        for c in s:
            char_map[c] += 1
        
        pq = [(-f,c) for c,f in char_map.items()]
        heapify(pq)

        ans = []
        prev_c, prev_f = '',0

        while pq:
            f,c = heappop(pq)
            ans.append(c)

            if prev_f < 0:
                heappush(pq,(prev_f,prev_c))

            f += 1
            prev_c, prev_f = c,f

        if len(ans) != len(s):
            return ''
        return ''.join(ans)