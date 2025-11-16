class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        nl = len(needle)
        hl = len(haystack)

        for i in range(hl-nl+1):
            if needle == haystack[i:i+nl]:
                return i

        return -1
