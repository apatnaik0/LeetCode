class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(ind,target):
            if target == 0:
                ans.append(sub[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                sub.append(candidates[i])
                rec(i+1,target-candidates[i])
                sub.pop()
        ans = []
        sub = []
        candidates.sort()
        rec(0,target)
        return ans
        