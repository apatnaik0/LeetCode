class Solution:
    def rec(self,sub, i, ans, candidates, target):
        if i == len(candidates):
            if target == 0:
                ans.append(sub[:])
            return ans
        if candidates[i] <= target:
            sub.append(candidates[i])
            self.rec(sub, i, ans, candidates, target - candidates[i])
            sub.pop()
        self.rec(sub, i+1, ans, candidates, target)
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub = []
        i = 0
        ans = self.rec(sub,i, ans, candidates, target)
        return ans