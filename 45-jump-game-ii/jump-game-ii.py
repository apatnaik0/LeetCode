class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        far = 0
        farthest = 0
        jumps = 0
        n = len(nums)

        while far < len(nums)-1:
            for i in range(near,far+1):
                farthest = max(farthest,i+nums[i])
            near = far + 1
            far = farthest
            jumps += 1
        return jumps

            