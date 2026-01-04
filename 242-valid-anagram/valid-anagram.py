class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        tmap = defaultdict(int)
        smap = defaultdict(int)

        for i,j in zip(s,t):
            smap[i] += 1
            tmap[j] += 1
        
        if len(tmap)!=len(smap):
            return False
        
        for i in tmap.keys():
            if tmap[i] != smap[i]:
                return False
        
        return True