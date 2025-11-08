class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = 0
        si = 0
        ct = 0
        gl = len(g)
        sl = len(s)
        while si < sl:
            if gi < gl and s[si] >= g[gi]:
                ct += 1
                gi += 1
            si += 1
        return ct