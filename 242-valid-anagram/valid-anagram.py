class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        smap = defaultdict(int)
        tmap = defaultdict(int)

        for i,j in zip(s,t):
            smap[i] += 1
            tmap[j] += 1
        
        if len(smap) != len(tmap):
            return False
        
        for k in smap.keys():
            if smap[k] != tmap[k]:
                return False
        
        return True
