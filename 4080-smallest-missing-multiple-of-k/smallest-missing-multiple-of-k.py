class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set()

        for num in nums:
            s.add(num)
        check = k
        while True:
            if check not in s:
                return check
            check += k
        
        return -1