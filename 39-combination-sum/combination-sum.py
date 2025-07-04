class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(i,t):
            if i == len(candidates):
                if t == 0:
                    final.append(ans[:])
                return
            if candidates[i]<=t:
                ans.append(candidates[i])
                rec(i,t-candidates[i])
                ans.pop()
            rec(i+1,t)

        final = []
        ans = []
        rec(0,target)
        return final