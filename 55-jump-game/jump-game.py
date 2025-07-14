class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = len(nums)-1
        # for i in range(len(nums)-2,-1,-1):
        #     if i + nums[i]>=goal:
        #         goal = i
        # return True if goal==0 else False

        maxind = 0
        for i in range(len(nums)):
            if i>maxind:
                return False
            maxind = max(maxind,i+nums[i])
            if maxind>=len(nums)-1:
                return True
        return True
