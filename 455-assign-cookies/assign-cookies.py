class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gl = len(g)
        sl = len(s)
        gi = 0
        si = 0
        while si<sl:
            if s[si]>=g[gi]:
                gi += 1
            si += 1
            if gi==gl:
                return gl
        return gi