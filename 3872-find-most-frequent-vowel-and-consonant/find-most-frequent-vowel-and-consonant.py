class Solution:
    def maxFreqSum(self, s: str) -> int:
        hm = defaultdict(int)
        for c in s:
            hm[c]+=1
        
        vm,cm = 0,0
        for k,v in hm.items():
            if k in set('aeiou'):
                vm = max(vm,v)
            else:
                cm = max(cm,v)
        
        return vm + cm
