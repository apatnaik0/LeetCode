class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(i,pi):
            if i==n:
                return 0
            if dp[i][pi]!=-1:
                return dp[i][pi]
            ans = solve(i+1,pi)
            if pi==-1 or nums[i]>nums[pi]:
                ans = max(ans, 1 + solve(i+1,i))
            return ans
        # dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # prev = [0 for _ in range(n+1)]
        # return solve(0,-1)
        # for i in range(n-1,-1,-1):
        #     cur = [0 for _ in range(n+1)]
        #     for pi in range(i-1,-2,-1):
        #         cur[pi+1] = prev[pi+1]
        #         if pi==-1 or nums[i]>nums[pi]:
        #             cur[pi+1] = max(cur[pi+1], 1 + prev[i+1])
        #     prev = cur
        # return prev[0]

        # Return LIS

        # dp = [1]*n
        # ha = [i for i in range(n)]
        # maxi = int(-1e9)
        # for cur in range(n):
        #     for prev in range(cur):
        #         if nums[cur] > nums[prev] and dp[prev] + 1 > dp[cur]:
        #             dp[cur] = dp[prev] + 1
        #             ha[cur] = prev
        #     if dp[cur]>maxi:
        #         maxi = dp[cur]
        #         lastindex = cur
        # ans = [nums[lastindex]]
        # while(lastindex != ha[lastindex]):
        #     lastindex = ha[lastindex]
        #     ans.append(nums[lastindex])
        
        # return len(ans[::-1])

        # Binary Search for Length of LIS

        def lower_bound(arr,num):
            r = len(arr)-1
            l = 0
            ans = 0
            while l<=r:
                mid = (l+r)//2
                if arr[mid]==num:
                    return mid
                elif arr[mid]>num:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            return ans
        
        res = [nums[0]]
        for i in range(1,n):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                ind = lower_bound(res,nums[i])
                res[ind] = nums[i]
            # print(res)
        return len(res)

        
                

