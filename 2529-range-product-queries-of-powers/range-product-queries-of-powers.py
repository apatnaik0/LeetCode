class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = 10**9 + 7
        for i in range(31):
            if n>>i & 1:
                powers.append(2**i)
        prepro = [powers[0]]
        for i in powers[1:]:
            prepro.append(prepro[-1]*i)
        ans = []
        for i,j in queries:
            if i==0:
                ans.append(prepro[j]%mod)
            else:
                high = j
                low = i-1 if i>0 else 0
                ans.append((prepro[high]//prepro[low])%mod)
        return ans

