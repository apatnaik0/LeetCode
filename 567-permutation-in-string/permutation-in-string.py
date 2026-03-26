class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        s1map = [0]*26

        for char in s1:
            s1map[ord(char)-ord('a')] += 1

        s2map = [0]*26

        left = 0

        
        for right in range(n2):
            s2map[ord(s2[right])-ord('a')] += 1

            if right - left + 1 > n1:
                s2map[ord(s2[left])-ord('a')] -= 1
                left += 1

            if right - left + 1 == n1 and s1map == s2map:
                return True
        
        return False

        