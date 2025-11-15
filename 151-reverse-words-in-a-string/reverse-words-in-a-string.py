class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        arr = []
        for i in li:
            if i != '':
                arr.append(i)
        
        ans = ''
        for i in arr:
            ans = i + ' ' + ans
        
        return ans[:-1]
        
        
