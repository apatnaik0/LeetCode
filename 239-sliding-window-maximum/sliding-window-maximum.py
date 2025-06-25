
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        for i in range(n):
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
            if i>=k and nums[i-k]==q[0]:
                q.popleft()
            if i>=k-1:
                ans.append(q[0])
        return ans
        