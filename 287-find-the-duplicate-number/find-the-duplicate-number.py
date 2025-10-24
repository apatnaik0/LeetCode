class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()
        for i in nums:
            if i in hset:
                return i
            else:
                hset.add(i)