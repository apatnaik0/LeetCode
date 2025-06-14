class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        def poss(arr,c,n):
            num=1
            cap=0
            for i in arr:
                print(num,cap)
                if cap+i>c:
                    num+=1
                    cap=i
                else:
                    cap+=i
            print(num,n)
            if num<=n:
                return True
            return False

        ans = high
        while low<=high:
            mid = (low+high)//2
            print(low,mid,high)
            if poss(nums,mid,k):
                ans = mid
                print(ans)
                high = mid-1
            else:
                low = mid+1
        return ans