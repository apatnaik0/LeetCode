class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hmap = {}
        for i in dominoes:
            key = tuple(sorted(i))
            hmap[key] = hmap.get(key,0)+1
        ans = 0
        for i in hmap.values():
            ans += i*(i-1)//2
        return ans

        