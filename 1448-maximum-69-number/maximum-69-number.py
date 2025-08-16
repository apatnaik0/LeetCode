class Solution:
    def maximum69Number (self, num: int) -> int:
        snum = str(num)
        for i in range(len(snum)):
            if snum[i]=='6':
                snum = snum[:i]+'9'+snum[i+1:]
                break
        return int(snum)
        