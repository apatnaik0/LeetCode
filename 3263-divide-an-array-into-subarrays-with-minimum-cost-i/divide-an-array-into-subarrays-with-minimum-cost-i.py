class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        mini = float('inf')
        mini2 = float('inf')

        for num in nums[1:]:
            if num <= mini:
                mini2 = mini
                mini = num
            elif num < mini2:
                mini2 = num

        return nums[0] + mini + mini2