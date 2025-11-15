class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        ans = []

        for i in range(n):
            while q and nums[i]>q[-1]:
                q.pop()
            q.append(nums[i])

            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            
            if i >= k-1:
                ans.append(q[0])
            
        return ans