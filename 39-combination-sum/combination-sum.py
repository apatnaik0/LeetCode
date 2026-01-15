class Solution:
    def solve(self,i,sub,ans,candidates,target):
        if i == len(candidates):
            if target == 0:
                ans.append(sub[:])
            return ans
        if candidates[i] <= target:
            sub.append(candidates[i])
            self.solve(i,sub,ans,candidates,target-candidates[i])
            sub.pop()
        self.solve(i+1,sub,ans,candidates,target)
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans = []
        # sub = []
        return self.solve(0,[],[],candidates,target)
        