class Solution:
    def level(self,v,n):
        for i in range(n):
            v.append('0')
        return v

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        n1 = len(v1)
        n2 = len(v2)

        if n1 > n2:
            v2 = self.level(v2,n1-n2)
        elif n2 > n1:
            v1 = self.level(v1,n2-n1)
        
        for i in range(max(n1,n2)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
        
        return 0

