class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ind = n-k
        heapify(nums)
        for i in range(ind):
            heappop(nums)
        
        return heappop(nums)