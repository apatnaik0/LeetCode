class Solution:
    def frequencySort(self, s: str) -> str:

        hmap = defaultdict(int)
        pq = []

        for char in s:
            hmap[char] += 1
        
        for key,val in hmap.items():
            heappush(pq,(-val,key))
        
        ans = ''
        while pq:
            freq,char = heappop(pq)

            ans += char*(-freq)
        
        return ans
        