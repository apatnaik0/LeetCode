class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        lb = 1e-6

        def solve(nums: List[float]):
            n = len(nums)
            if n==1:
                return abs(nums[0] - 24.0)<lb
            for i in range(n):
                for j in range(i+1,n):
                    rest = [nums[k] for k in range(n) if k!=i and k!=j]
                    a = nums[i]
                    b = nums[j]
                    newvals = []
                    newvals.append(a+b)
                    newvals.append(a-b)
                    newvals.append(b-a)
                    newvals.append(a*b)
                    if a>lb:
                        newvals.append(b/a)
                    if b>lb:
                        newvals.append(a/b)
                    
                    for val in newvals:
                        if solve(rest+[val]):
                            return True
            return False
        return solve([float(x) for x in cards])
