class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)
        for i in range(n):
            res = target - nums[i]
            # print(res, target, nums[i])
            if res in hmap.keys():
                # print('enter if')
                return [hmap[res], i]
            else:
                # print('enter else')
                hmap[nums[i]] = i
            # print(hmap)
        