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
                ans.append((prepro[j]//prepro[i-1])%mod)
        return ans

