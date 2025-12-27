class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)
        for i in range(n):
            d = target - nums[i]
            if d in hmap:
                return [i,hmap[d]]
            else:
                hmap[nums[i]] = i
        return 