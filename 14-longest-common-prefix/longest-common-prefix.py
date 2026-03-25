class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        n = len(strs)

        for st in strs[1:]:
            l = len(prefix)
            while prefix != st[:l]:
                l -= 1
                prefix = prefix[:l]
            if prefix == "":
                return prefix
        
        return prefix