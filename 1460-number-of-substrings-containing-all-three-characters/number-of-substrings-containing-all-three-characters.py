class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ind = [-1,-1,-1]
        ct = 0
        for i in range(len(s)):
            ind[ord(s[i])-ord('a')] = i
            if ind[0]!=-1 and ind[1]!=-1 and ind[2]!=-1:
                ct += 1 + min(ind[0],ind[1],ind[2])
        return ct