class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)
        for i in range(n):
            res = target - nums[i]
            if res in hmap:
                return [hmap[res],i]
            hmap[nums[i]] = i
