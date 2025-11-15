class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        pre = strs[0]

        for i in strs[1:]:
            while pre != i[:len(pre)]:
                pre = pre[:-1]
            if pre == '':
                return ''
        
        return pre